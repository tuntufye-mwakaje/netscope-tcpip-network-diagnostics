# NetScope: TCP/IP Network Diagnostics & Subnet Visualization Lab

A beginner-friendly but technically structured Python networking project for learning and demonstrating:

- IPv4 addresses and CIDR notation
- subnet masks, network/broadcast addresses, usable hosts
- same-subnet analysis
- DNS name resolution
- TCP connectivity checks
- local network-interface inventory and counters
- network topology visualization
- network-performance visualization
- modular Python design, testing, and Git/GitHub workflow

> **Scope:** This is a defensive/educational network diagnostics lab. TCP checks are performed only against hosts and ports explicitly supplied by the user. It does not perform broad or automated Internet scanning.

## Architecture

```text
                +---------------------------+
                |        Streamlit UI       |
                |   app.py / dashboard      |
                +-------------+-------------+
                              |
                    +---------v---------+
                    |  Network Service  |
                    +---------+---------+
                              |
        +---------------------+---------------------+
        |                     |                     |
+-------v-------+     +-------v-------+     +-------v-------+
| IPv4/Subnets  |     | DNS/TCP Probe |     | Interfaces    |
| ipaddress     |     | socket        |     | psutil        |
+-------+-------+     +-------+-------+     +-------+-------+
        |                     |                     |
        +---------------------+---------------------+
                              |
                    +---------v---------+
                    | Visualizations    |
                    | matplotlib /      |
                    | networkx          |
                    +-------------------+
```

## Requirements

- Windows 10/11, Linux, or macOS
- Python 3.11+
- VS Code
- Internet connection for package installation and DNS/TCP demonstrations

## Features

### 1. IPv4 / subnet analysis
Input an address such as `192.168.10.25/24` and inspect:

- network address
- broadcast address
- subnet mask
- prefix length
- total addresses
- usable hosts
- first/last usable host

The implementation uses Python's standard `ipaddress` module.

### 2. Same-subnet comparison
Compare two IPv4 addresses against a selected CIDR network and determine whether they belong to the same subnet.

### 3. DNS resolution
Resolve a hostname such as `example.com` and display its resolved IP addresses.

### 4. TCP connectivity
Test one explicitly supplied `host:port`, for example `example.com:443`.

### 5. Local interface inventory
Display local IPv4 interfaces and interface traffic counters collected through `psutil`.

### 6. Visualizations
The dashboard generates:

- subnet address-space visualization
- local interface traffic chart
- network topology graph

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal, normally `http://localhost:8501`.

## CLI

```powershell
python main.py
```

## Tests

```powershell
pytest -q
```

## Suggested GitHub repository name

`netscope-tcpip-network-diagnostics`

## Professional portfolio value

The project demonstrates application of TCP/IP networking concepts through working code rather than a list of theoretical terms. It complements software-development, data/AI, and OT-monitoring portfolio work by adding practical networking evidence.
