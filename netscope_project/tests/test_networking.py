from src.networking import compare_subnet, summarize_subnet


def test_subnet_summary():
    result = summarize_subnet("192.168.10.25/24")
    assert result["Network address"] == "192.168.10.0"
    assert result["Broadcast address"] == "192.168.10.255"
    assert result["Usable hosts"] == 254


def test_same_subnet_true():
    assert compare_subnet("192.168.10.25", "192.168.10.50", 24) is True


def test_same_subnet_false():
    assert compare_subnet("192.168.10.25", "192.168.11.50", 24) is False
