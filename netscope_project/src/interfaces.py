from __future__ import annotations

import socket
from typing import Any

import psutil


def get_interface_summary() -> list[dict[str, Any]]:
    """Collect a compact inventory of local interfaces and traffic counters."""
    addresses = psutil.net_if_addrs()
    counters = psutil.net_io_counters(pernic=True)
    rows: list[dict[str, Any]] = []

    for interface_name, addr_list in addresses.items():
        ipv4_addresses = [
            address.address
            for address in addr_list
            if address.family == socket.AF_INET
        ]
        traffic = counters.get(interface_name)
        rows.append(
            {
                "interface": interface_name,
                "ipv4": ", ".join(ipv4_addresses) if ipv4_addresses else "N/A",
                "bytes_sent": traffic.bytes_sent if traffic else 0,
                "bytes_received": traffic.bytes_recv if traffic else 0,
            }
        )

    return sorted(rows, key=lambda row: row["interface"].lower())
