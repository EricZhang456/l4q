"""Gets the latest L4D2 version."""

from socket import timeout

import a2s
from flask import Flask
from retry import retry

from l4q.extensions import scheduler
from l4q.utils.parse_hostname import parse_hostname


@scheduler.task("interval", id="get_l4d2_version", hours=5)
def get_l4d2_version_task():
    """Background task that fetches the latest L4D2 version at an interval."""
    get_l4d2_version(scheduler.app)


@retry(timeout, delay=1, tries=5)
def get_l4d2_version(app: Flask):
    """Gets the latest L4D2 version and store it in config.

    :param Flask app: A Flask application with the L4D2_ADDRESS config pointing to
                      a valid L4D2 server.
    """
    address = parse_hostname(app.config["L4D2_ADDRESS"])
    server_info: a2s.SourceInfo = a2s.info(address)
    if server_info.app_id != 550 or type(server_info).__name__ == "GoldSrcInfo":
        raise RuntimeError("L4D2_ADDRESS is not a L4D2 server.")
    app.config["L4D2_VERSION"] = server_info.version.replace(".", "")
