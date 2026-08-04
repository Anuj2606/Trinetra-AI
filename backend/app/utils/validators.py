from urllib.parse import urlparse


def validate_url(url: str) -> bool:
    parsed = urlparse(url)

    return bool(parsed.scheme and parsed.netloc)