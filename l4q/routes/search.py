"""Search view."""

from socket import timeout, gaierror

import l4d2query
from flask import Blueprint, render_template, request, make_response, current_app

from l4q.utils.server_data_utils import get_server_data, get_disp_data

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("/")
def get_search_view():
    """Main search view."""
    search_addr = request.args.get("search").strip()
    server_data = None
    disp_data = None
    error_text = None
    status = "200"
    if search_addr:
        try:
            server_data = get_server_data(search_addr, int(current_app.config["L4D2_VERSION"]))
            disp_data = get_disp_data(server_data)
        except l4d2query.BufferExhaustedError:
            error_text = "Cannot decode response from game server."
            status = "502"
        except timeout:
            error_text = "Timed out when fetching game server data."
            status = "504"
        except (gaierror, ValueError):
            error_text = "Invalid server address."
            status = "400"
    subview_header = request.headers.get("x-fetch-subview")
    if subview_header is not None and (subview_header.isnumeric() and int(subview_header) == 1):
        if error_text:
            response = make_response(error_text)
            response.mimetype = "text/plain"
        else:
            response = make_response(render_template("server_item.html",
                                                     server_data=server_data,
                                                     disp_data=disp_data))
    else:
        response = make_response(render_template("search.html",
                                                 search_addr=search_addr,
                                                 server_data=server_data,
                                                 disp_data=disp_data,
                                                 error_text=error_text))
    response.status = status
    return response
