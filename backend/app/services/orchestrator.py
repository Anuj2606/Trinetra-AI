import asyncio

from app.services.providers.virustotal_provider import VirusTotalProvider
from app.services.providers.safebrowsing_provider import SafeBrowsingProvider
from app.services.providers.rdap_provider import RDAPProvider
from app.services.providers.urlscan_provider import URLScanProvider
from app.services.providers.gemini_provider import GeminiProvider

from app.services.risk_engine import RiskEngine
from app.services.report_generator import ReportGenerator
from app.services.fraud_engine import FraudEngine
from app.services.url_feature_analyzer import URLFeatureAnalyzer
from app.services.provider_runner import ProviderRunner

class ScanOrchestrator:

    def __init__(self):

        self.vt = VirusTotalProvider()
        self.safe = SafeBrowsingProvider()
        self.rdap = RDAPProvider()
        self.urlscan = URLScanProvider()

        self.gemini = GeminiProvider()

        self.risk_engine = RiskEngine()

        self.report = ReportGenerator()

        self.fraud_engine = FraudEngine()

        self.url_features = URLFeatureAnalyzer()

    async def analyze(self, url: str):
        url_features = self.url_features.analyze(url)

        vt, safe, rdap, urlscan = await asyncio.gather(

    ProviderRunner.run(
        "VirusTotal",
        self.vt.analyze(url)
    ),

    ProviderRunner.run(
        "Google Safe Browsing",
        self.safe.analyze(url)
    ),

    ProviderRunner.run(
        "RDAP",
        self.rdap.analyze(url)
    ),

    ProviderRunner.run(
        "URLScan",
        self.urlscan.analyze(url)
    )

)

        risk = self.risk_engine.calculate(
    vt,
    safe,
    rdap,
    urlscan,
    url_features
)

        providers = {
    "virustotal": vt,
    "safe_browsing": safe,
    "rdap": rdap,
    "urlscan": urlscan,
    "url_features": url_features
}
        fraud = self.fraud_engine.classify(

            providers,

            risk

        )

        ai = await self.gemini.analyze(risk)

        providers = {

            "virustotal": vt,

            "safe_browsing": safe,

            "rdap": rdap,

            "urlscan": urlscan

        }

        return self.report.generate(

    url,

    providers,

    risk,

    ai,

    fraud

)