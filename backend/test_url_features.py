from app.services.url_feature_analyzer import URLFeatureAnalyzer

analyzer = URLFeatureAnalyzer()

print(

    analyzer.analyze(

        "https://paypal-login-secure.xyz/account/verify"

    )

)