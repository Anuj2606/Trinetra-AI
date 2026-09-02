<p align="center">
  <img src="https://img.shields.io/badge/Trinetra-AI-blue?style=for-the-badge&logo=shield&logoColor=white" alt="Trinetra AI" />
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React" />
  <img src="https://img.shields.io/badge/FastAPI-0.141-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Gemini_AI-Powered-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini" />
  <img src="https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
</p>

<h1 align="center">🛡️ Trinetra AI — AI Powered Threat Detection System</h1>

<p align="center">
  <b>A multi-layered, AI-powered threat intelligence system that analyzes URLs in real-time using 5 independent security providers, a proprietary risk scoring engine, and Google Gemini AI for explainable cybersecurity reports.</b>
</p>

<p align="center">
  <a href="#-key-features">Features</a> •
  <a href="#-system-architecture">Architecture</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-getting-started">Setup</a> •
  <a href="#-api-reference">API</a> •
  <a href="#-backend-implementation-deep-dive">Backend Deep Dive</a>
</p>

---

## 📌 Problem Statement

Phishing attacks, malicious URLs, and online fraud are growing at an alarming rate. Traditional blocklist-based approaches are reactive and fail against zero-day phishing domains. Security teams and everyday users need a **real-time, multi-signal, AI-explained** threat analysis tool that goes beyond simple URL lookups.

**Trinetra AI** solves this by orchestrating multiple threat intelligence providers in parallel, scoring risk with a custom weighted algorithm, classifying attack types with a fraud intelligence engine, and generating human-readable security reports powered by Google Gemini.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔍 **Multi-Provider Analysis** | Simultaneously queries VirusTotal, Google Safe Browsing, URLScan.io, and RDAP in parallel using `asyncio.gather` |
| 🧠 **AI-Powered Reports** | Google Gemini generates explainable cybersecurity summaries with threat context and actionable recommendations |
| 📊 **Proprietary Risk Scoring** | Custom weighted algorithm (0–100) combining 12+ risk signals across all providers and URL heuristics |
| 🎯 **Fraud Classification** | Dedicated engine classifies attack types (Phishing, Malware, Suspicious, Legitimate) with severity levels |
| 🔗 **URL Feature Analysis** | Heuristic pre-screening detects IP-based URLs, shorteners, suspicious TLDs, phishing keywords, and more — before any API calls |
| 📜 **PDF Report Export** | One-click downloadable PDF reports generated server-side with ReportLab |
| 📈 **Analytics Dashboard** | Interactive charts (Pie + Bar) visualize historical scan distributions across risk levels |
| 🕑 **Scan History** | Full searchable history of all past scans persisted in PostgreSQL |
| ⚡ **Fault-Tolerant Design** | Individual provider failures don't crash the scan — the system gracefully degrades with partial results |
| 🔄 **Async Everything** | End-to-end async architecture from API routes → orchestrator → providers for maximum throughput |

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              FRONTEND (React + Vite)                       │
│                                                                             │
│  ┌──────────┐  ┌───────────┐  ┌───────────┐  ┌────────────┐               │
│  │   Home   │  │ Dashboard │  │  History   │  │ Analytics  │               │
│  │ (ScanBox)│  │(Threat    │  │(Searchable │  │(Pie + Bar  │               │
│  │          │  │ Report)   │  │ Table)     │  │ Charts)    │               │
│  └────┬─────┘  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘               │
│       │              │              │              │                        │
│       └──────────────┴──────────────┴──────────────┘                        │
│                              │ Axios HTTP                                   │
└──────────────────────────────┼──────────────────────────────────────────────┘
                               │
                     ┌─────────▼─────────┐
                     │   FastAPI Server   │
                     │   (CORS Enabled)   │
                     └─────────┬─────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
     ┌────────▼──────┐ ┌──────▼──────┐ ┌───────▼──────┐
     │  POST /scan   │ │ GET /history│ │GET /analytics│
     │               │ │             │ │              │
     └────────┬──────┘ └──────┬──────┘ └───────┬──────┘
              │               │                │
              │          ┌────▼────────────────▼────┐
              │          │      PostgreSQL DB        │
              │          │  ┌───────┐ ┌──────────┐  │
              │          │  │ scans │ │ provider │  │
              │          │  │       │ │ _results │  │
              │          │  └───────┘ └──────────┘  │
              │          │  ┌───────┐               │
              │          │  │ users │               │
              │          │  └───────┘               │
              │          └──────────────────────────┘
              │
     ┌────────▼────────────────────────────────────────────┐
     │                 SCAN ORCHESTRATOR                    │
     │                                                      │
     │  1. URL Feature Analyzer (heuristic pre-screening)  │
     │                                                      │
     │  2. Parallel Provider Execution (asyncio.gather):   │
     │     ┌─────────────┐  ┌──────────────┐               │
     │     │ VirusTotal  │  │Safe Browsing │               │
     │     │   (v3 API)  │  │  (v4 API)    │               │
     │     └─────────────┘  └──────────────┘               │
     │     ┌─────────────┐  ┌──────────────┐               │
     │     │    RDAP     │  │  URLScan.io  │               │
     │     │(Domain Age) │  │ (Behaviour)  │               │
     │     └─────────────┘  └──────────────┘               │
     │                                                      │
     │  3. Risk Engine → Weighted Score (0-100)            │
     │                                                      │
     │  4. Fraud Engine → Attack Classification            │
     │                                                      │
     │  5. Gemini AI → Explainable Security Report         │
     │                                                      │
     │  6. Report Generator → Final JSON Response          │
     └────────────────────────────────────────────────────┘
```

---

## 🔄 How It Works

### Scan Workflow (End-to-End Pipeline)

```
User enters URL → Frontend POST /scan
                        │
                        ▼
              ┌─── URL Feature Analyzer ───┐
              │ • HTTPS check              │
              │ • IP address detection     │
              │ • Suspicious TLD check     │
              │ • Keyword scanning         │
              │ • Shortener detection      │
              │ • URL length analysis      │
              └───────────┬────────────────┘
                          │
                          ▼
         ┌──── asyncio.gather (Parallel) ────┐
         │                                    │
    ┌────▼────┐  ┌────▼────┐  ┌───▼───┐  ┌──▼──────┐
    │ VT      │  │ Google  │  │ RDAP  │  │ URLScan │
    │ Submit→ │  │ Safe    │  │ Domain│  │ Submit→ │
    │ Poll    │  │ Browse  │  │ Age   │  │ Poll    │
    │ Report  │  │ Lookup  │  │ Whois │  │ Report  │
    └────┬────┘  └────┬────┘  └───┬───┘  └──┬──────┘
         │            │           │          │
         └────────────┴─────┬─────┴──────────┘
                            │
                   ┌────────▼────────┐
                   │   Risk Engine   │
                   │ Weighted Score  │
                   │   (0 → 100)    │
                   │                 │
                   │ SAFE < 20      │
                   │ LOW  < 40      │
                   │ MEDIUM < 60    │
                   │ HIGH < 80      │
                   │ CRITICAL ≥ 80  │
                   └────────┬───────┘
                            │
                   ┌────────▼────────┐
                   │  Fraud Engine   │
                   │                 │
                   │ → Attack Type   │
                   │ → Severity      │
                   │ → Indicators    │
                   │ → Recommendation│
                   └────────┬───────┘
                            │
                   ┌────────▼────────┐
                   │   Gemini AI     │
                   │                 │
                   │ → Summary       │
                   │ → Threats       │
                   │ → Action Items  │
                   └────────┬───────┘
                            │
                   ┌────────▼────────┐
                   │ Report Generator│
                   │                 │
                   │ → Final JSON    │
                   │ → Save to DB    │
                   │ → Return to UI  │
                   └─────────────────┘
```

### Provider Fault Tolerance

```
Provider Call
     │
     ├── Success → result["success"] = True → Use data
     │
     └── Exception → ProviderRunner catches
                   → result["success"] = False
                   → Log error
                   → Continue scan with remaining providers
                   → Risk Engine uses defaults for failed providers
```

---

## 🛠 Tech Stack

### Backend
| Technology | Purpose |
|---|---|
| **Python 3.11+** | Core language |
| **FastAPI** | Async REST API framework |
| **SQLAlchemy** | ORM for PostgreSQL |
| **Pydantic** | Request/response validation and settings |
| **httpx** | Async HTTP client for external APIs |
| **Google GenAI SDK** | Gemini AI integration |
| **ReportLab** | PDF report generation |
| **Loguru** | Structured logging with rotation |
| **python-dateutil** | RDAP date parsing |
| **PostgreSQL** | Primary database |

### Frontend
| Technology | Purpose |
|---|---|
| **React 19** | UI framework |
| **Vite 8** | Build tool and dev server |
| **TypeScript** | Type safety (build config) |
| **Tailwind CSS 4** | Utility-first styling |
| **Framer Motion** | Animations and transitions |
| **Recharts** | Interactive charts (Pie, Bar) |
| **React Router v7** | Client-side routing |
| **Axios** | HTTP client |
| **Lucide React / React Icons** | Icon library |
| **React Hot Toast** | Notifications |
| **React CountUp** | Animated number counters |

---

## 📂 Project Structure

```
TrinetraAI/
│
├── backend/
│   ├── app/
│   │   ├── api/                        # API layer
│   │   │   ├── router.py               # Central router aggregation
│   │   │   ├── health.py               # Health check endpoint
│   │   │   ├── scan.py                 # Legacy scan endpoint
│   │   │   └── routes/
│   │   │       ├── scan.py             # POST /scan — main scan endpoint
│   │   │       ├── history.py          # GET /history — scan history
│   │   │       ├── analytics.py        # GET /analytics — aggregate stats
│   │   │       └── report.py           # POST /report — PDF generation
│   │   │
│   │   ├── core/                       # Core infrastructure
│   │   │   ├── config.py               # Pydantic settings (.env loader)
│   │   │   ├── http_client.py          # Shared async HTTP client (httpx)
│   │   │   ├── exceptions.py           # Custom exception hierarchy
│   │   │   └── logger.py              # Loguru configuration
│   │   │
│   │   ├── services/                   # Business logic layer
│   │   │   ├── orchestrator.py         # ScanOrchestrator — main pipeline
│   │   │   ├── risk_engine.py          # Weighted risk scoring (0-100)
│   │   │   ├── fraud_engine.py         # Attack classification engine
│   │   │   ├── url_feature_analyzer.py # Heuristic URL pre-screening
│   │   │   ├── report_generator.py     # Final JSON report assembly
│   │   │   ├── provider_runner.py      # Fault-tolerant provider executor
│   │   │   └── providers/
│   │   │       ├── base.py             # Abstract BaseProvider interface
│   │   │       ├── virustotal_provider.py
│   │   │       ├── safebrowsing_provider.py
│   │   │       ├── rdap_provider.py
│   │   │       ├── urlscan_provider.py
│   │   │       └── gemini_provider.py
│   │   │
│   │   ├── models/                     # SQLAlchemy ORM models
│   │   │   ├── user.py                 # User model
│   │   │   ├── scan.py                 # Scan model
│   │   │   └── provider_result.py      # Provider result model (JSON)
│   │   │
│   │   ├── schemas/                    # Pydantic request/response schemas
│   │   │   └── scan.py                 # ScanRequest, ScanResponse, RiskResponse
│   │   │
│   │   ├── crud/                       # Database operations
│   │   │   ├── scan_crud.py            # Save scan + provider results
│   │   │   └── history_crud.py         # Query scan history
│   │   │
│   │   ├── database/                   # Database configuration
│   │   │   ├── database.py             # Engine, SessionLocal, get_db
│   │   │   └── init_db.py             # Table creation script
│   │   │
│   │   └── utils/
│   │       └── validators.py           # URL validation helper
│   │
│   ├── logs/                           # Application logs (auto-rotated)
│   ├── requirements.txt                # Python dependencies
│   ├── .env                            # Environment variables (not committed)
│   ├── test_orchestrator.py            # Integration test for orchestrator
│   ├── test_gemini.py                  # Gemini provider test
│   ├── test_virustotal.py              # VirusTotal provider test
│   ├── test_safebrowsing.py            # Safe Browsing provider test
│   ├── test_rdap.py                    # RDAP provider test
│   ├── test_urlscan.py                 # URLScan provider test
│   └── test_url_features.py            # URL feature analyzer test
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                     # Route definitions
│   │   ├── main.jsx                    # React DOM entry point
│   │   ├── pages/
│   │   │   ├── Home.jsx                # Landing page with scan box
│   │   │   ├── Dashboard.jsx           # Threat intelligence report view
│   │   │   ├── History.jsx             # Searchable scan history table
│   │   │   ├── Analytics.jsx           # Charts and aggregate statistics
│   │   │   └── About.jsx               # About page
│   │   ├── components/
│   │   │   ├── layout/
│   │   │   │   ├── Navbar.jsx          # Navigation bar
│   │   │   │   └── Hero.jsx            # Hero section
│   │   │   ├── ui/
│   │   │   │   ├── ScanBox.jsx         # URL input + scan trigger
│   │   │   │   └── ScanLoader.jsx      # Multi-step loading animation
│   │   │   ├── dashboard/
│   │   │   │   ├── RiskOverview.jsx     # Risk score gauge display
│   │   │   │   ├── ProviderCards.jsx    # Per-provider result cards
│   │   │   │   ├── ThreatIndicators.jsx # Risk reasons + fraud indicators
│   │   │   │   ├── AICard.jsx           # Gemini AI summary card
│   │   │   │   ├── RecommendationCard.jsx # Action recommendations
│   │   │   │   └── ReasonList.jsx       # Risk reason list component
│   │   │   └── cards/
│   │   │       ├── AICard.jsx           # AI insight card
│   │   │       ├── FraudCard.jsx        # Fraud classification card
│   │   │       ├── LiveStats.jsx        # Real-time statistics
│   │   │       └── StatsCards.jsx       # Summary stat cards
│   │   └── services/
│   │       └── api.js                   # Axios instance (baseURL config)
│   │
│   ├── package.json
│   ├── vite.config.ts
│   └── index.html
│
├── docker/                             # Docker configuration (planned)
├── docs/                               # Documentation (planned)
├── screenshots/                        # UI screenshots (planned)
├── docker-compose.yml                  # Docker Compose (planned)
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.11+**
- **Node.js 18+** and **npm**
- **PostgreSQL 15+**
- API Keys for:
  - [VirusTotal](https://www.virustotal.com/gui/join-us) (free tier available)
  - [Google Safe Browsing](https://developers.google.com/safe-browsing) (free)
  - [URLScan.io](https://urlscan.io/user/signup) (free tier available)
  - [Google Gemini AI](https://aistudio.google.com/apikey) (free tier available)

### 1. Clone the Repository

```bash
git clone https://github.com/Anuj2606/Trinetra-AI.git
cd Trinetra-AI
```

### 2. Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file inside `backend/`:

```env
APP_NAME=Trinetra AI
APP_VERSION=1.0.0
DEBUG=True
HOST=127.0.0.1
PORT=8000

# API Keys
GEMINI_API_KEY=your_gemini_api_key
VIRUSTOTAL_API_KEY=your_virustotal_api_key
SAFE_BROWSING_API_KEY=your_safe_browsing_api_key
URLSCAN_API_KEY=your_urlscan_api_key

# PostgreSQL
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=trinetra_ai
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
```

### 4. Initialize Database

```bash
# Create the database in PostgreSQL first
psql -U postgres -c "CREATE DATABASE trinetra_ai;"

# Run table creation
python -m app.database.init_db
```

### 5. Start Backend Server

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at `http://127.0.0.1:8000` with interactive docs at `/docs`.

### 6. Frontend Setup

```bash
# Navigate to frontend (from project root)
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:5173`.

---

## 📡 API Reference

### Core Endpoints

| Method | Endpoint | Description | Request Body |
|---|---|---|---|
| `POST` | `/scan` | Analyze a URL across all providers | `{ "url": "https://example.com" }` |
| `GET` | `/history/` | Retrieve all past scans (newest first) | — |
| `GET` | `/analytics/` | Aggregate scan statistics | — |
| `POST` | `/report/` | Generate downloadable PDF report | Full scan result JSON |

### Sample Scan Response

```json
{
  "scan_id": "20260806012033",
  "generated_at": "2026-08-05T19:50:33.000000",
  "url": "https://example.com",
  "risk": {
    "risk_score": 15,
    "risk_level": "SAFE",
    "confidence": 95,
    "reasons": [
      "VirusTotal found no malicious detections.",
      "Google Safe Browsing reports the URL as safe.",
      "Domain has existed for a long time.",
      "URLScan found no malicious behaviour."
    ]
  },
  "fraud_analysis": {
    "attack_type": "Legitimate Website",
    "severity": "LOW",
    "recommendation": "The website appears trustworthy. Continue browsing with normal caution.",
    "indicators": [],
    "risk_score": 15
  },
  "ai_summary": "Summary: The analyzed URL shows no significant threats...",
  "providers": {
    "virustotal": { "malicious": 0, "suspicious": 0, "harmless": 72, ... },
    "safe_browsing": { "unsafe": false, "threat_count": 0, ... },
    "rdap": { "domain": "example.com", "age_days": 11234, ... },
    "urlscan": { "malicious": false, "redirects": 0, ... }
  }
}
```

---

## 🧠 Backend Implementation Deep Dive

### Provider Interface Design (PID)

All threat intelligence providers implement the **`BaseProvider`** abstract class, enforcing a consistent interface:

```python
class BaseProvider(ABC):
    @abstractmethod
    async def analyze(self, url: str) -> Dict[str, Any]:
        """Analyze the given URL and return a standardized dictionary."""
        pass
```

Each provider returns a dictionary with at minimum:
- `provider`: Provider name string
- `success`: Boolean indicating if the call succeeded
- Provider-specific fields (e.g., `malicious`, `unsafe`, `age_days`)

### Provider Details

| Provider | API | Key Signals | Async Behaviour |
|---|---|---|---|
| **VirusTotal** | v3 REST | `malicious` count, `suspicious` count, reputation, categories, threat names | Submit URL → wait 3s → fetch report |
| **Google Safe Browsing** | v4 threatMatches | `unsafe` flag, threat type matches (Malware, Social Engineering, Unwanted Software) | Single POST lookup |
| **RDAP** | rdap.org | Domain `age_days`, registration date, expiration, registrar, status | Single GET lookup |
| **URLScan.io** | v1 REST | `malicious` verdict, redirect count, page metadata, screenshot, ASN, brands | Submit URL → poll up to 30 attempts (2s intervals) |
| **Gemini AI** | Google GenAI SDK | AI-generated security summary, threats, recommendations | Model fallback chain (3.6→3.5→2.5→2.0-flash) |

### Risk Scoring Algorithm

The **Risk Engine** combines 12+ weighted signals into a score from 0 to 100:

```
Signal                          Weight    Condition
──────────────────────────────────────────────────────────
VirusTotal malicious > 0        +45       Any malicious engine detected
VirusTotal suspicious > 0       +20       Suspicious classification
Safe Browsing flagged           +30       Any threat match found
Domain age < 30 days            +20       Newly registered domain
Domain age < 180 days           +10       Relatively new domain
URLScan malicious verdict       +35       Overall malicious verdict
URLScan redirects > 3           +10       Excessive redirections
No HTTPS                        +10       Missing SSL/TLS
Contains IP address             +20       IP-based URL
Contains '@' symbol             +10       Deceptive URL character
Suspicious TLD                  +10       .xyz, .top, .click, .zip, etc.
Multiple hyphens (≥2)           +5        Domain obfuscation pattern
URL length > 75 chars           +5        Unusually long URL
URL shortener detected          +15       bit.ly, tinyurl, t.co, etc.
Phishing keywords               +5 each  login, verify, bank, wallet, etc.
──────────────────────────────────────────────────────────
Final Score = min(sum, 100)

Risk Level Mapping:
  SAFE     →  0–19
  LOW      → 20–39
  MEDIUM   → 40–59
  HIGH     → 60–79
  CRITICAL → 80–100

Confidence = max(60, 100 - score/3)
```

### Fraud Classification Engine

The **Fraud Engine** operates downstream of the Risk Engine and classifies:

| Output Field | Values |
|---|---|
| `attack_type` | `Legitimate Website`, `Known Malicious Website`, `Phishing / Malware`, `Suspicious Website` |
| `severity` | `LOW`, `MEDIUM`, `HIGH`, `CRITICAL` |
| `recommendation` | Dynamic text based on severity level |
| `indicators` | Array of human-readable signals that triggered classification |

Classification priority: VirusTotal malicious → Safe Browsing flagged → URLScan malicious → Domain age < 30 days

### Orchestrator Pipeline

The `ScanOrchestrator` is the central coordinator that executes the full analysis pipeline:

```
ScanOrchestrator.analyze(url)
│
├── 1. URLFeatureAnalyzer.analyze(url)     # Synchronous heuristic check
│
├── 2. asyncio.gather(                     # Parallel external API calls
│       ProviderRunner.run("VirusTotal", vt.analyze(url)),
│       ProviderRunner.run("Safe Browsing", safe.analyze(url)),
│       ProviderRunner.run("RDAP", rdap.analyze(url)),
│       ProviderRunner.run("URLScan", urlscan.analyze(url))
│   )
│
├── 3. RiskEngine.calculate(vt, safe, rdap, urlscan, url_features)
│
├── 4. FraudEngine.classify(providers, risk)
│
├── 5. GeminiProvider.analyze(risk)         # AI explanation
│
└── 6. ReportGenerator.generate(url, providers, risk, ai, fraud)
```

### Database Schema (ERD)

```
┌─────────────────┐       ┌─────────────────────┐
│     users        │       │      scans           │
├─────────────────┤       ├─────────────────────┤
│ id (PK)         │◄──┐   │ id (PK)             │
│ full_name       │   └───│ user_id (FK)        │
│ email (UNIQUE)  │       │ url                  │
│ password        │       │ risk_score           │
│ created_at      │       │ risk_level           │
└─────────────────┘       │ confidence           │
                          │ attack_type          │
                          │ ai_summary           │
                          │ created_at           │
                          └──────────┬───────────┘
                                     │
                          ┌──────────▼───────────┐
                          │  provider_results     │
                          ├──────────────────────┤
                          │ id (PK)              │
                          │ scan_id (FK → scans) │
                          │ provider             │
                          │ success              │
                          │ response (JSON)      │
                          └──────────────────────┘
```

### Custom Exception Hierarchy

```
TrinetraException (base)
├── ProviderError
│   ├── InvalidAPIKeyError
│   ├── RateLimitError
│   └── ExternalServiceUnavailableError
├── InvalidURLException
├── RiskScoringError
├── AIProviderError
└── ConfigurationError
```

### Shared HTTP Client

All external API calls go through a centralized `HTTPClient` (built on `httpx.AsyncClient`) that provides:
- Configurable timeouts (default: 30s)
- Automatic redirect following
- Graceful handling of URLScan's 404-while-processing edge case
- Consistent error mapping to custom exceptions

---

## 🖥 Frontend Pages

| Page | Route | Description |
|---|---|---|
| **Home** | `/` | Landing page with hero section, live statistics, and URL scan input box |
| **Dashboard** | `/dashboard` | Full threat intelligence report: risk overview, provider results, threat indicators, AI summary, recommendations, PDF export |
| **History** | `/history` | Searchable table of all past scans with risk score, level, attack type, and timestamp |
| **Analytics** | `/analytics` | Aggregate stats (total/safe/malicious counts) with interactive Pie and Bar charts |

---

## 🧪 Testing

The project includes per-provider integration tests:

```bash
cd backend

# Test individual providers
python test_virustotal.py
python test_safebrowsing.py
python test_rdap.py
python test_urlscan.py
python test_gemini.py
python test_url_features.py

# Test full orchestrator pipeline
python test_orchestrator.py
```

---

## 🔮 Roadmap

- [ ] Docker containerization (Compose setup for API + DB + Frontend)
- [ ] User authentication (JWT-based signup/login)
- [ ] Browser extension for one-click URL scanning
- [ ] Email alert system for high-risk scans
- [ ] Batch URL scanning via CSV upload
- [ ] Historical trend analysis and ML-based anomaly detection
- [ ] Webhook integrations (Slack, Discord, Teams)
- [ ] Rate limiting and API key management

---

## 👨‍💻 Author

**Anuj**

- GitHub: [@Anuj2606](https://github.com/Anuj2606)

---
