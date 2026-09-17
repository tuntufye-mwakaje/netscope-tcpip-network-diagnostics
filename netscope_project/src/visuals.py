from __future__ import annotations

import ipaddress

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


def subnet_visual(network_cidr: str):
    """Visualize the position of a selected IPv4 address space."""
    network = ipaddress.ip_network(network_cidr, strict=False)
    addresses = list(network.hosts())

    fig, ax = plt.subplots(figsize=(10, 2.8))
    if addresses:
        xs = range(len(addresses))
        ax.scatter(xs, [1] * len(addresses), s=45)
        ax.set_xlim(-1, max(len(addresses), 1))
        ax.set_yticks([])
        ax.set_xlabel("Host position inside subnet")
        ax.set_title(f"IPv4 Host Space: {network}")
        ax.grid(axis="x", alpha=0.25)
        if len(addresses) <= 256:
            ax.set_xticks(list(range(0, len(addresses), max(1, len(addresses) // 8))))
            ax.set_xticklabels(
                [str(addresses[i]) for i in range(0, len(addresses), max(1, len(addresses) // 8))],
                rotation=45,
                ha="right",
                fontsize=8,
            )
    else:
        ax.text(0.5, 0.5, "No usable host addresses in this subnet", ha="center", va="center")
        ax.axis("off")
    fig.tight_layout()
    return fig


def interface_traffic_visual(rows: list[dict]):
    """Plot bytes sent/received for local interfaces."""
    df = pd.DataFrame(rows)
    if df.empty:
        return None

    plot_df = df.set_index("interface")[["bytes_sent", "bytes_received"]]
    ax = plot_df.plot(kind="bar", figsize=(10, 4))
    ax.set_title("Local Interface Traffic Counters")
    ax.set_ylabel("Bytes")
    ax.set_xlabel("Network interface")
    ax.tick_params(axis="x", rotation=35)
    ax.grid(axis="y", alpha=0.25)
    fig = ax.get_figure()
    fig.tight_layout()
    return fig


def topology_visual():
    """Draw a small conceptual LAN/WAN topology for learning purposes."""
    graph = nx.Graph()
    graph.add_edges_from(
        [
            ("Laptop", "Access Switch"),
            ("Access Switch", "Router"),
            ("Router", "WAN/Internet"),
            ("Access Switch", "Application Server"),
            ("Access Switch", "DNS/DHCP Server"),
        ]
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    positions = nx.spring_layout(graph, seed=7)
    nx.draw_networkx(
        graph,
        positions,
        ax=ax,
        node_size=2300,
        font_size=9,
        width=2,
    )
    ax.set_title("Conceptual LAN → Router → WAN Topology")
    ax.axis("off")
    fig.tight_layout()
    return fig
