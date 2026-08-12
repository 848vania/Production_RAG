from frontend.utils import format_cost, format_latency_ms, format_percent


def test_format_percent():
    assert format_percent(0.86) == "86.0%"
    assert format_percent(None) == "-"


def test_format_latency_ms():
    assert format_latency_ms(2100) == "2.10s"
    assert format_latency_ms(None) == "-"


def test_format_cost():
    assert format_cost(0.00321) == "$0.0032"
    assert format_cost(None) == "-"