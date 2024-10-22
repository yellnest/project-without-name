from datetime import datetime, UTC


def naive_utcnow():
    """Return (date time utc) without microseconds
    """
    return datetime.now(UTC).replace(tzinfo=None).strftime("%Y-%m-%d %H:%M:%S")
