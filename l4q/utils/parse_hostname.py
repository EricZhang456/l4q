"""Hostname parsing utility."""

import socket

from urllib.parse import urlsplit


def parse_hostname(server_addr: str) -> tuple[str, int]:
    """Parse server address and format into a tuple.

    :param str server_addr: Server address (in host:port format).
    :return: A tuple of the parsed address, first item being the hostname
                and second item being the port.
    :rtype: tuple[str, int]
    :raises ValueError: Invalid address or hostname.
    """
    parsed = urlsplit("//" + server_addr)
    if parsed.hostname is None or parsed.port is None:
        raise ValueError("Invalid address")
    try:
        socket.gethostbyname(parsed.hostname)
    except socket.herror as e:
        raise ValueError("Invalid hostname") from e
    return parsed.hostname, parsed.port
