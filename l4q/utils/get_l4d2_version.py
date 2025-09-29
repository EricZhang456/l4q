"""Gets the latest L4D2 version."""

from socket import timeout

import a2s
from quart import Quart, current_app
from retry import retry

from l4q.extensions import scheduler
from l4q.utils.parse_hostname import parse_hostname


@scheduler.cron("0 */5 * * *")
async def get_l4d2_version_task():
    """Background task that fetches the latest L4D2 version at an interval."""
    await get_l4d2_version(current_app)


@retry(timeout, delay=1, tries=5)
async def get_l4d2_version(app: Quart):
    """Gets the latest L4D2 version and store it in config.

    :param Quart app: A Quart application with the L4D2_ADDRESS config pointing to
                      a valid L4D2 server.
    """
    address = await parse_hostname(app.config["L4D2_ADDRESS"])
    server_info: a2s.SourceInfo = await a2s.ainfo(address)
    if server_info.app_id != 550 or isinstance(server_info, a2s.GoldSrcInfo):
        raise RuntimeError("L4D2_ADDRESS does not point a L4D2 server.")
    app.config["L4D2_VERSION"] = server_info.version.replace(".", "")
