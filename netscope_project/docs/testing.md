# NetScope Testing

## Testing Framework

NetScope uses `pytest` for automated testing.

The test suite covers:

- IPv4 subnet calculations
- CIDR validation
- same-subnet comparisons
- IPv4/IPv6 validation
- DNS hostname validation
- TCP port validation
- TCP connectivity behavior
- local network-interface processing
- missing IPv4 interface handling
- subnet visualization
- interface traffic visualization
- topology visualization

## Running the Tests

From the repository root:

```powershell
python -m pytest -q
