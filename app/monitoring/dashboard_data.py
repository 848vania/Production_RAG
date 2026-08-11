from app.monitoring.metrics import get_monitoring_summary


def get_dashboard_metrics() -> dict:
    """
    Return monitoring data formatted for frontend display
    """
    summary = get_monitoring_summary()

    return {
        'cards': {
            'Total Queries': summary['total_queries'],
            'Average Latency': f'{summary['average_latency_ms'] / 1000:.2f}s',
            'Total Cost': f'{summary['total_estimated_cost_usd']:.4f}',
            'Refusal Rate': f'{summary['refusal_rate'] * 100:.1f}%',
            'Low Confidence Rate': f'{summary['low_confidence_rate'] * 100:.1f}%',
        },
        'recent_queries': summary['recent_queries'],
    }