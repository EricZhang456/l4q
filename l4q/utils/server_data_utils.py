"""Server data utils."""

from socket import timeout

import validators
import l4d2query
from retry import retry

from l4q.utils.map_thumbnail import get_map_thumbnail
from l4q.utils.l4d2_names import (get_campaign_name, get_chapter_name,
                                  ACCESS_NAMES, DIFFICULTY_NAMES, MODE_NAMES, MAX_ROUNDS_NAMES,
                                  NO_DIFFICULTY_GAME_MODES)

_DEFAULT_CAMPAIGN_WEBSITE = "http://store.steampowered.com"


def format_server_data(server_data: l4d2query.TokenPacket) -> dict:
    """Format the server info and put them in a dictionary.

    :param TokenPacket server_data: Data of the server from l4d2query.
    :return: A dictionary containing the sever data.
    :rtype: dict
    """
    raw_data: dict = server_data.data
    # Server info case folding is inconsistent on listen/dedicated servers
    server_dict: dict = raw_data.get("Server")
    if server_dict is None:
        server_dict = raw_data.get("server")
    server_name = server_dict.get("Name")
    if server_name is None:
        server_name = server_dict.get("name")
    server_type = server_dict.get("Server")
    if server_type is None:
        server_type = server_dict.get("server")
    campaign_website: str | None = raw_data.get("game").get("MissionInfo").get("Website")
    if not campaign_website.startswith(("https://", "http://")):
        campaign_website = "https://" + campaign_website
    if not validators.url(campaign_website) or campaign_website == _DEFAULT_CAMPAIGN_WEBSITE:
        campaign_website = None
    response_data = {
        "access": raw_data.get("System").get("access"),
        "name": server_name,
        "type": server_type,
        "public_adr": server_dict.get("adronline"),
        "private_adr": server_dict.get("adrlocal"),
        "max_players": raw_data.get("Members").get("numSlots"),
        "player_count": raw_data.get("Members").get("numPlayers"),
        "state": raw_data.get("game").get("state"),
        "mode": raw_data.get("game").get("Mode"),
        "campaign": raw_data.get("game").get("campaign"),
        "chapter": raw_data.get("game").get("chapter"),
        "campaign_version": raw_data.get("game").get("MissionInfo").get("Version"),
        "campaign_builtin": bool(raw_data.get("game").get("MissionInfo").get("builtin")),
        "campaign_addon": bool(raw_data.get("game").get("MissionInfo").get("addon")),
        "campaign_display_title": raw_data.get("game").get("MissionInfo").get("DisplayTitle"),
        "campaign_author": raw_data.get("game").get("MissionInfo").get("Author"),
        "campaign_website": campaign_website,
        "campaign_workshop_id": raw_data.get("game").get("MissionInfo").get("workshopid"),
        "campaign_infected_only": raw_data.get("game").get("MissionInfo").get("InfectedOnly"),
        "mode_title": raw_data.get("game").get("ModeInfo").get("DisplayTitle"),
        "mode_workshop_id": raw_data.get("game").get("ModeInfo").get("workshopid"),
        "mode_addon": bool(raw_data.get("game").get("ModeInfo").get("addon")),
        "difficulty": raw_data.get("game").get("difficulty"),
        "maxrounds": raw_data.get("game").get("maxrounds"),
        "dlcrequired": raw_data.get("game").get("dlcrequired")
    }
    return response_data


@retry(timeout, delay=1, tries=5)
def get_server_data(server_addr: tuple[str, int], version: int) -> dict:
    """Get server data formatted in a dictionary from a host:port address.

    :param tuple[str, int] server_addr: Server address and port formatted in a tuple.
    :param int version: Engine version.
    :return: A dictionary of server info.
    :rtype: dict
    """
    return format_server_data(l4d2query.query_serverdetails(server_addr, version))


def get_disp_data(server_data: dict) -> dict:
    """Get display information from game server data.

    :param dict server_data: Server data.
    :return: A dictionary with all the display data.
    :rtype dict
    """
    response = {
        "access": ACCESS_NAMES.get(server_data.get("access")),
        "difficulty": DIFFICULTY_NAMES.get(server_data.get("difficulty").lower()),
        "campaign": get_campaign_name(server_data.get("campaign_display_title")),
        "thumbnail": get_map_thumbnail(server_data.get("campaign_display_title"),
                                       server_data.get("chapter"),
                                       server_data.get("mode")),
        "chapter": get_chapter_name(server_data.get("campaign_display_title"),
                                    server_data.get("chapter"),
                                    server_data.get("mode"),
                                    server_data.get("max_players")),
    }
    game_mode = MODE_NAMES.get(server_data.get("mode"))
    if game_mode is None:
        response["mode"] = server_data.get("mode")
    else:
        if server_data.get("mode") not in NO_DIFFICULTY_GAME_MODES:
            game_mode = f"{MODE_NAMES.get(server_data.get('mode'))} - {response.get('difficulty')}"
        response["mode"] = game_mode
    if server_data.get("mode") in {"scavenge", "mutation13"}:
        response["maxrounds"] = MAX_ROUNDS_NAMES.get(server_data.get("maxrounds"))
    return response
