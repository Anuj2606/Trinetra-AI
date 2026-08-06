"""
Fraud Intelligence Risk Engine

Combines results from multiple providers
into one explainable risk score.
"""


class RiskEngine:

    def calculate(
        self,
        vt,
        safe,
        rdap,
        urlscan,
        url_features,
        redirect_info=None
    ):

        # --------------------------
        # Handle failed providers
        # --------------------------

        if not vt.get("success", False):
            vt = {
                "malicious": 0,
                "suspicious": 0
            }

        if not safe.get("success", False):
            safe = {
                "unsafe": False
            }

        if not rdap.get("success", False):
            rdap = {
                "age_days": None
            }

        if not urlscan.get("success", False):
            urlscan = {
                "malicious": False,
                "redirects": 0
            }

        score = 0
        reasons = []

        # --------------------------
        # VirusTotal
        # --------------------------

        if vt["malicious"] > 0:
            score += 45
            reasons.append(
                f"VirusTotal detected {vt['malicious']} malicious engines."
            )
        else:
            reasons.append(
                "VirusTotal found no malicious detections."
            )

        if vt["suspicious"] > 0:
            score += 20
            reasons.append(
                "VirusTotal marked the URL as suspicious."
            )

        # --------------------------
        # Safe Browsing
        # --------------------------

        if safe["unsafe"]:
            score += 30
            reasons.append(
                "Google Safe Browsing flagged this URL."
            )
        else:
            reasons.append(
                "Google Safe Browsing reports the URL as safe."
            )

        # --------------------------
        # RDAP
        # --------------------------

        if rdap["age_days"] is not None:

            if rdap["age_days"] < 30:
                score += 20
                reasons.append(
                    "Domain is less than 30 days old."
                )

            elif rdap["age_days"] < 180:
                score += 10
                reasons.append(
                    "Domain is relatively new."
                )

            else:
                reasons.append(
                    "Domain has existed for a long time."
                )

        # --------------------------
        # URLScan
        # --------------------------

        if urlscan["malicious"]:
            score += 35
            reasons.append(
                "URLScan detected suspicious behaviour."
            )
        else:
            reasons.append(
                "URLScan found no malicious behaviour."
            )

        if urlscan["redirects"] > 3:
            score += 10
            reasons.append(
                "Multiple redirects detected."
            )

        # --------------------------
        # URL Features
        # --------------------------

        if not url_features["https"]:
            score += 10
            reasons.append(
                "Website does not use HTTPS."
            )

        if url_features["contains_ip"]:
            score += 20
            reasons.append(
                "URL contains an IP address."
            )

        if url_features["contains_at"]:
            score += 10
            reasons.append(
                "URL contains '@'."
            )

        if url_features["suspicious_tld"]:
            score += 10
            reasons.append(
                "Suspicious top-level domain detected."
            )

        if url_features["hyphen_count"] >= 2:
            score += 5
            reasons.append(
                "Multiple hyphens detected."
            )

        if url_features["url_length"] > 75:
            score += 5
            reasons.append(
                "Very long URL."
            )

        if url_features["shortener"]:
            score += 15
            reasons.append(
                "URL shortener detected."
            )

        keyword_score = len(url_features["keywords"]) * 5

        score += keyword_score

        if keyword_score:
            reasons.append(
                f"Suspicious keywords detected: {', '.join(url_features['keywords'])}"
            )

        # --------------------------
        # Redirect Logic
        # --------------------------

        if redirect_info and redirect_info.get("redirect_count", 0) > 0:
            count = redirect_info["redirect_count"]
            score += 15 + (count * 5)
            reasons.append(
                f"URL uses redirects ({count} hops) to hide final destination."
            )
            
            # If the final destination is different from the original submitted, 
            # and it redirected through a known shortener or multiple times, that's high risk.
            if url_features.get("shortener"):
                score += 20
                reasons.append("Shortened URL hiding the final destination.")

        score = min(score, 100)

        if score >= 80:
            level = "CRITICAL"
        elif score >= 60:
            level = "HIGH"
        elif score >= 40:
            level = "MEDIUM"
        elif score >= 20:
            level = "LOW"
        else:
            level = "SAFE"

        confidence = max(60, 100 - (score // 3))

        return {
            "risk_score": score,
            "risk_level": level,
            "confidence": confidence,
            "reasons": reasons
        }