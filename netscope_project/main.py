from src.networking import compare_subnet, tcp_check, dns_lookup, summarize_subnet
from src.interfaces import get_interface_summary


def main() -> None:
    print("=== NetScope TCP/IP Network Diagnostics Lab ===")
    print()

    cidr = input("Enter an IPv4 interface/network (example 192.168.10.25/24): ").strip()
    try:
        summary = summarize_subnet(cidr)
        print("\nIPv4 subnet summary")
        for key, value in summary.items():
            print(f"{key:>20}: {value}")
    except ValueError as exc:
        print(f"Invalid network input: {exc}")

    print("\nSame-subnet check")
    ip1 = input("First IPv4 address: ").strip()
    ip2 = input("Second IPv4 address: ").strip()
    mask = input("CIDR prefix (example 24): ").strip()
    try:
        result = compare_subnet(ip1, ip2, int(mask))
        print(f"Same subnet: {result}")
    except (ValueError, TypeError) as exc:
        print(f"Invalid subnet comparison: {exc}")

    print("\nDNS lookup")
    host = input("Hostname (example example.com): ").strip()
    try:
        addresses = dns_lookup(host)
        print("Resolved addresses:")
        for address in addresses:
            print(f"  - {address}")
    except OSError as exc:
        print(f"DNS lookup failed: {exc}")

    print("\nExplicit TCP connectivity test")
    host = input("Host: ").strip()
    port = input("Port (example 443): ").strip()
    try:
        status = tcp_check(host, int(port), timeout=3.0)
        print(status)
    except (ValueError, OSError) as exc:
        print(f"TCP check failed: {exc}")

    print("\nLocal network interfaces")
    for row in get_interface_summary():
        print(row)


if __name__ == "__main__":
    main()
