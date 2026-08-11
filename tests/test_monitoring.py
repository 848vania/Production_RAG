from app.monitoring.metrics import (
    average_latency_ms,
    low_confidence_rate,
    refusal_rate,
    total_estimated_cost_usd,
)


class FakeLog:
    def __init__(
        self,
        latency_ms=0.0,
        cost_usd=None,
        refused=False,
        confidence="low",
    ):
        self.latency_ms = latency_ms
        self.cost_usd = cost_usd
        self.refused = refused
        self.confidence = confidence


def test_average_latency_ms():
    logs = [
        FakeLog(latency_ms=100.0),
        FakeLog(latency_ms=300.0),
    ]

    assert average_latency_ms(logs) == 200.0


def test_total_estimated_cost_usd():
    logs = [
        FakeLog(cost_usd=0.001),
        FakeLog(cost_usd=0.002),
        FakeLog(cost_usd=None),
    ]

    assert total_estimated_cost_usd(logs) == 0.003


def test_refusal_rate():
    logs = [
        FakeLog(refused=True),
        FakeLog(refused=False),
        FakeLog(refused=False),
    ]

    assert refusal_rate(logs) == 1 / 3


def test_low_confidence_rate():
    logs = [
        FakeLog(confidence="low"),
        FakeLog(confidence="medium"),
        FakeLog(confidence="high"),
    ]

    assert low_confidence_rate(logs) == 1 / 3