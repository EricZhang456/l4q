"""Search view."""

from flask import Blueprint, render_template, request

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("/")
def get_search_view():
    """Main search view."""
    search_addr = request.args.get("search")
    return render_template("search.html", search_addr=search_addr)
