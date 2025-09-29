"""Hostname parsing utility."""

from socket import AddressFamily # pylint stfu
from urllib.parse import urlsplit

import aiodns

async def parse_hostname(server_addr: str) -> tuple[str, int]:
    """Parse server address and format into a tuple in an async manner.

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
        async with aiodns.DNSResolver() as resolver:
            host = await resolver.gethostbyname(parsed.hostname, AddressFamily.AF_INET)
    except aiodns.error.DNSError as e:
        raise ValueError("Invalid hostname") from e
    hostname = host.name
    return hostname, parsed.port
