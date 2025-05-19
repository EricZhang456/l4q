"""Search view."""

from socket import timeout, gaierror

import l4d2query
import a2s
from flask import Blueprint, render_template, request, make_response, current_app

from l4q.utils.server_data_utils import get_server_data, get_disp_data
from l4q.utils.player_list import get_player_list

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("/")
def get_search_view():
    """Main search view."""
    search_addr = request.args.get("search")
    if search_addr is not None:
        search_addr = search_addr.strip()
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
    if search_addr:
        response.headers.set("Cache-Control", "no-cache, no-store")
    response.headers.set("Vary", "x-fetch-subview")
    response.status = status
    return response

@bp.route("/player_list")
def get_player_list_view():
    """Returns a player list of the server."""
    search_addr = request.args.get("search")
    response = make_response()
    response.mimetype = "text/plain"
    if not search_addr:
        response.status = "400"
        return response
    search_addr = search_addr.strip()
    try:
        player_list = get_player_list(search_addr)
        response = make_response(render_template("player_list.html", player_list=player_list))
        response.mimetype = "text/html"
    except (a2s.BrokenMessageError, a2s.BufferExhaustedError, ConnectionRefusedError):
        response.status = "502"
    except timeout:
        response.status = "504"
    except (gaierror, ValueError):
        response.status = "400"
    response.headers.set("Cache-Control", "no-cache, no-store")
    return response
