from __future__ import annotations

import ipaddress
import socket
from typing import Any


def summarize_subnet(value: str) -> dict[str, Any]:
    """Return useful IPv4 subnet information from an address/CIDR input."""
    interface = ipaddress.ip_interface(value)
    network = interface.network
    hosts = list(network.hosts())

    return {
        "IP address": str(interface.ip),
        "CIDR network": str(network),
        "Subnet mask": str(network.netmask),
        "Prefix length": f"/{network.prefixlen}",
        "Network address": str(network.network_address),
        "Broadcast address": str(network.broadcast_address),
        "Total addresses": network.num_addresses,
        "Usable hosts": max(network.num_addresses - 2, 0),
        "First usable host": str(hosts[0]) if hosts else "N/A",
        "Last usable host": str(hosts[-1]) if hosts else "N/A",
    }


def compare_subnet(ip1: str, ip2: str, prefix: int) -> bool:
    """Check whether two IPv4 addresses fall inside the same subnet."""
    if not 0 <= prefix <= 32:
        raise ValueError("Prefix must be between 0 and 32.")

    a = ipaddress.ip_address(ip1)
    b = ipaddress.ip_address(ip2)
    if a.version != 4 or b.version != 4:
        raise ValueError("This function currently expects IPv4 addresses.")

    network_a = ipaddress.ip_network(f"{a}/{prefix}", strict=False)
    return b in network_a


def dns_lookup(hostname: str) -> list[str]:
    """Resolve a hostname and return unique IP addresses."""
    if not hostname:
        raise ValueError("Hostname cannot be empty.")

    results = socket.getaddrinfo(hostname, None, type=socket.SOCK_STREAM)
    addresses = sorted({item[4][0] for item in results})
    return addresses


def tcp_check(host: str, port: int, timeout: float = 3.0) -> str:
    """Attempt one TCP connection to an explicitly supplied host/port."""
    if not host:
        raise ValueError("Host cannot be empty.")
    if not 1 <= port <= 65535:
        raise ValueError("Port must be between 1 and 65535.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))

    if result == 0:
        return f"TCP OPEN/REACHABLE: {host}:{port}"
    return f"TCP NOT REACHABLE: {host}:{port} (socket result={result})"
