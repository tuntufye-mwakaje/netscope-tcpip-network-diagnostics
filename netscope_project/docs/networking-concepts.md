# Networking concepts used by NetScope

## IPv4 and CIDR

IPv4 uses 32-bit addresses. CIDR notation expresses the prefix length, for example `/24`. The prefix identifies the network portion while the remaining bits identify addresses within the subnet.

## TCP/IP

TCP provides connection-oriented transport behavior over IP. NetScope's TCP checker uses Python sockets to attempt one connection to an explicitly specified destination and port.

## LAN / WAN

The application distinguishes a local network segment from routed connectivity to another network. The topology tab is conceptual and does not claim to reproduce the user's physical network.

## DNS

DNS translates hostnames into IP addresses used by applications to communicate with network endpoints.

## DHCP

DHCP is not emulated in this version. It is included as a documented future extension because automatic host IP configuration is a core enterprise networking function.
