"""
Fraud Intelligence Engine

Classifies attack type, severity and provides
security recommendations based on provider outputs.
"""


class FraudEngine:

    def classify(self, providers: dict, risk: dict):

        vt = providers["virustotal"]
        sb = providers["safe_browsing"]
        rdap = providers["rdap"]
        urlscan = providers["urlscan"]

        attack_type = "Legitimate Website"
        severity = "LOW"

        recommendation = (
            "The website appears trustworthy. "
            "Continue browsing with normal caution."
        )

        indicators = []

        # ----------------------------
        # Provider Availability
        # ----------------------------

        if not vt.get("success", False):
            indicators.append("VirusTotal unavailable.")

        if not sb.get("success", False):
            indicators.append("Google Safe Browsing unavailable.")

        if not rdap.get("success", False):
            indicators.append("RDAP unavailable.")

        if not urlscan.get("success", False):
            indicators.append("URLScan unavailable.")

        # ----------------------------
        # VirusTotal
        # ----------------------------

        if vt.get("malicious", 0) > 0:

            attack_type = "Known Malicious Website"

            severity = "CRITICAL"

            indicators.append(
                f"VirusTotal detected {vt['malicious']} malicious engines."
            )

        # ----------------------------
        # Safe Browsing
        # ----------------------------

        if sb.get("unsafe", False):

            attack_type = "Phishing / Malware"

            severity = "HIGH"

            indicators.append(
                "Google Safe Browsing flagged the URL."
            )

        # ----------------------------
        # Domain Age
        # ----------------------------

        if rdap.get("age_days") is not None:

            if rdap["age_days"] < 30:

                indicators.append(
                    "Domain registered less than 30 days ago."
                )

                if severity != "CRITICAL":
                    severity = "HIGH"

        # ----------------------------
        # URLScan
        # ----------------------------

        if urlscan.get("redirects", 0) > 3:

            indicators.append(
                "Multiple redirects detected."
            )

        if urlscan.get("malicious", False):

            attack_type = "Suspicious Website"

            severity = "HIGH"

            indicators.append(
                "URLScan detected suspicious behaviour."
            )

        # ----------------------------
        # Recommendation
        # ----------------------------

        if severity == "CRITICAL":

            recommendation = (
                "Do NOT visit this website. "
                "Avoid entering credentials or downloading files."
            )

        elif severity == "HIGH":

            recommendation = (
                "Proceed with extreme caution. "
                "Verify the website independently."
            )

        elif severity == "MEDIUM":

            recommendation = (
                "Inspect the website carefully before interacting."
            )

        return {

            "attack_type": attack_type,

            "severity": severity,

            "recommendation": recommendation,

            "indicators": indicators,

            "risk_score": risk["risk_score"]

        }