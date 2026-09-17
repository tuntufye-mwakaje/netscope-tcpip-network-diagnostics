# NetScope Architecture

## 1. Overview

NetScope is organized as a small layered Python application.

The design separates:

1. User interface
2. Networking logic
3. Local interface inspection
4. Visualization
5. Automated testing

This separation makes the core networking functions easier to test and reuse independently from the Streamlit dashboard.

---

## 2. High-Level Architecture

```text
                         User
                           |
              +------------+------------+
              |                         |
        Command Line                Streamlit UI
           main.py                    app.py
              |                         |
              +------------+------------+
                           |
                    Application Logic
                           |
          +----------------+----------------+
          |                |                |
    networking.py    interfaces.py     visuals.py
          |                |                |
       ipaddress         psutil        Matplotlib
       socket                            NetworkX
          |
    IPv4 / CIDR
    DNS
    TCP