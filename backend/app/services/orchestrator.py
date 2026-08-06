import asyncio
import httpx
from urllib.parse import urlparse

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

    async def resolve_url(self, url: str):
        redirect_count = 0
        final_url = url
        try:
            async with httpx.AsyncClient(follow_redirects=False, timeout=10.0) as client:
                for _ in range(5):
                    response = await client.get(final_url)
                    if response.is_redirect:
                        redirect_count += 1
                        location = response.headers.get("Location")
                        if location:
                            if not location.startswith("http"):
                                parsed = urlparse(final_url)
                                location = f"{parsed.scheme}://{parsed.netloc}{location}"
                            final_url = location
                        else:
                            break
                    else:
                        break
        except Exception as e:
            print(f"Error resolving URL {url}: {e}")
            pass
        return {"final_url": final_url, "redirect_count": redirect_count}

    async def analyze(self, url: str):
        redirect_info = await self.resolve_url(url)
        final_url = redirect_info["final_url"]

        original_features = self.url_features.analyze(url)
        url_features = self.url_features.analyze(final_url)
        
        # Keep the shortener flag if the original URL was a shortener
        if original_features.get("shortener"):
            url_features["shortener"] = True

        vt, safe, rdap, urlscan = await asyncio.gather(

    ProviderRunner.run(
        "VirusTotal",
        self.vt.analyze(final_url)
    ),

    ProviderRunner.run(
        "Google Safe Browsing",
        self.safe.analyze(final_url)
    ),

    ProviderRunner.run(
        "RDAP",
        self.rdap.analyze(final_url)
    ),

    ProviderRunner.run(
        "URLScan",
        self.urlscan.analyze(final_url)
    )

)

        risk = self.risk_engine.calculate(
    vt,
    safe,
    rdap,
    urlscan,
    url_features,
    redirect_info
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