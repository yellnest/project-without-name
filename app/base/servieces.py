import re
from datetime import datetime, UTC


def naive_utcnow():
    """Return (date time utc) without microseconds
    """
    return datetime.now(UTC).replace(tzinfo=None).strftime("%Y-%m-%d %H:%M:%S")

def generate_slug(title):
    """Return slug based on title, work only with latin letters
    """
    slug = re.sub(r'\W+', '-', title.lower())
    return slug
