"""
URL Feature Analyzer

Extracts heuristic features from URLs before
calling external threat intelligence providers.
"""

import re
from urllib.parse import urlparse
import ipaddress


class URLFeatureAnalyzer:

    SUSPICIOUS_TLDS = {
        "xyz",
        "top",
        "click",
        "zip",
        "gq",
        "tk",
        "cf",
        "ml",
        "work",
        "buzz"
    }

    SUSPICIOUS_KEYWORDS = {
        "login",
        "verify",
        "secure",
        "update",
        "bank",
        "wallet",
        "account",
        "signin",
        "password",
        "confirm",
        "paypal",
        "amazon",
        "microsoft",
        "apple"
    }

    SHORTENERS = {
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "twitter.com",
        "goo.gl",
        "ow.ly",
        "is.gd"
    }

    def analyze(self, url: str):

        parsed = urlparse(url)

        domain = parsed.netloc.lower()

        path = parsed.path.lower()

        features = {

            "url_length": len(url),

            "https": parsed.scheme == "https",

            "contains_ip": False,

            "contains_at": "@" in url,

            "hyphen_count": domain.count("-"),

            "subdomain_count": max(domain.count(".") - 1, 0),

            "suspicious_tld": False,

            "shortener": False,

            "keywords": []
        }

        # IP Address

        try:
            ipaddress.ip_address(domain.split(":")[0])
            features["contains_ip"] = True
        except:
            pass

        # TLD

        if "." in domain:

            tld = domain.split(".")[-1]

            if tld in self.SUSPICIOUS_TLDS:

                features["suspicious_tld"] = True

        # URL Shortener

        if domain in self.SHORTENERS:

            features["shortener"] = True

        # Keywords

        text = domain + path

        for keyword in self.SUSPICIOUS_KEYWORDS:

            if keyword in text:

                features["keywords"].append(keyword)

        return features