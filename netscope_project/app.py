from __future__ import annotations

import streamlit as st

from src.interfaces import get_interface_summary
from src.networking import compare_subnet, dns_lookup, summarize_subnet, tcp_check
from src.visuals import interface_traffic_visual, subnet_visual, topology_visual

st.set_page_config(page_title="NetScope", page_icon="🌐", layout="wide")

st.title("NetScope")
st.caption("TCP/IP Network Diagnostics & Subnet Visualization Lab")

st.info(
    "Educational/portfolio project. TCP tests are limited to a host and port explicitly entered by the user; "
    "no broad network scanning is performed."
)

tab1, tab2, tab3, tab4 = st.tabs(
    ["IPv4 & Subnets", "DNS & TCP", "Local Interfaces", "Topology"]
)

with tab1:
    st.subheader("IPv4 subnet analyzer")
    cidr = st.text_input("IPv4 interface/CIDR", "192.168.10.25/24")
    try:
        summary = summarize_subnet(cidr)
        col1, col2 = st.columns(2)
        with col1:
            st.json(summary)
        with col2:
            network = summary["CIDR network"]
            st.pyplot(subnet_visual(network), clear_figure=True)
    except ValueError as exc:
        st.error(f"Invalid IPv4/CIDR input: {exc}")

    st.divider()
    st.subheader("Same-subnet comparison")
    c1, c2, c3 = st.columns(3)
    ip1 = c1.text_input("IPv4 address A", "192.168.10.25")
    ip2 = c2.text_input("IPv4 address B", "192.168.10.50")
    prefix = c3.number_input("CIDR prefix", min_value=0, max_value=32, value=24, step=1)

    try:
        same = compare_subnet(ip1, ip2, int(prefix))
        st.success(f"Same subnet: {same}") if same else st.warning(f"Same subnet: {same}")
    except ValueError as exc:
        st.error(str(exc))

with tab2:
    st.subheader("DNS resolution")
    hostname = st.text_input("Hostname", "example.com")
    if st.button("Resolve DNS"):
        try:
            addresses = dns_lookup(hostname)
            st.write("Resolved IP addresses:")
            st.code("\n".join(addresses) if addresses else "No addresses returned.")
        except (OSError, ValueError) as exc:
            st.error(f"DNS lookup failed: {exc}")

    st.divider()
    st.subheader("Explicit TCP connectivity test")
    host = st.text_input("Host", "example.com", key="tcp_host")
    port = st.number_input("TCP port", min_value=1, max_value=65535, value=443, step=1)
    if st.button("Run TCP check"):
        try:
            st.code(tcp_check(host, int(port)))
        except (OSError, ValueError) as exc:
            st.error(f"TCP check failed: {exc}")

with tab3:
    st.subheader("Local network interfaces")
    rows = get_interface_summary()
    st.dataframe(rows, use_container_width=True)
    fig = interface_traffic_visual(rows)
    if fig is not None:
        st.pyplot(fig, clear_figure=True)
    st.caption("Traffic counters are operating-system interface counters, not packet-level captures.")

with tab4:
    st.subheader("Conceptual network topology")
    st.pyplot(topology_visual(), clear_figure=True)
    st.markdown(
        "**Interpretation:** a LAN commonly contains endpoint devices, access switching and local services; "
        "a router provides Layer-3 forwarding toward another network such as a WAN/Internet connection."
    )
