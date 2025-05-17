"""Player list utilities"""

import time
from socket import timeout

import a2s
from retry import retry

from l4q.utils.parse_hostname import parse_hostname

@retry(timeout, tries=5, delay=1)
def get_player_list(server_addr: str) -> list[dict]:
    """Get the player list of a server with time formatted.
    
    :param str server_addr: Address of the server in a host:port format.
    :return: A list of dictionary with the player name and time connected.
    :rtype: list[dict]
    """
    player_list = a2s.players(parse_hostname(server_addr))
    response = []
    for item in player_list:
        time_hours = int(time.strftime("%H", time.gmtime(item.duration)))
        time_minutes = int(time.strftime("%M", time.gmtime(item.duration)))
        time_seconds = int(time.strftime("%S", time.gmtime(item.duration)))
        time_str = f"{time_seconds}s"
        if time_minutes:
            time_str = f"{time_minutes}m " + time_str
        if time_hours:
            time_str = f"{time_hours}h " + time_str
        response.append({
            "name": item.name,
            "time": time_str,
            "duration": int(item.duration)
        })
    return response
