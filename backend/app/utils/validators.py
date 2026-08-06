import validators
from urllib.parse import urlparse

def validate_url(url: str) -> bool:
    if not validators.url(url):
        return False
        
    parsed = urlparse(url)
    # Require a TLD (a dot in the domain) or an IPv4/IPv6 address
    if "." not in parsed.netloc and not parsed.netloc.replace(":", "").isdigit():
        return False
        
    return True