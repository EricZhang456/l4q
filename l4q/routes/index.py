"""Index view."""

from quart import Blueprint, redirect, url_for

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/")
async def get_index():
    """Redirects to search page when fetching index."""
    return redirect(url_for("search.get_search_view"))
