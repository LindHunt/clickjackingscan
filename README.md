# LINDHUNT CLICKJACKING SCANNER

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FF00,100:000000&height=200&section=header&text=CLICKJACKING%20SCANNER&fontSize=40&fontAlignY=35&desc=⚡%20Asynchronous%20Security%20Tool&descAlignY=55&descSize=18" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PYTHON-HACKER-00FF00?style=for-the-badge&logo=python&logoColor=white&labelColor=black" />
  <img src="https://img.shields.io/badge/SECURITY-RESEARCHER-00FF00?style=for-the-badge&logo=hackthebox&logoColor=white&labelColor=black" />
  <img src="https://img.shields.io/badge/OSINT-ANALYST-00FF00?style=for-the-badge&logo=grafana&logoColor=white&labelColor=black" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/VERSION-1.0.0-00FF00?style=for-the-badge&logo=github&logoColor=white&labelColor=black" />
  <img src="https://img.shields.io/badge/PYTHON-3.8+-00FF00?style=for-the-badge&logo=python&logoColor=white&labelColor=black" />
  <img src="https://img.shields.io/badge/LICENSE-MIT-00FF00?style=for-the-badge&logo=open-source-initiative&logoColor=white&labelColor=black" />
</p>

---

## ⚡ ABOUT

```
█████████████████████████████████████████████████████████████████
█                                                               █
█  ░█▀▀░█▀█░█▀▄░█░█░█▀▀░█▀▀░█▀▄░█▀▀░█▀█░▀█▀░█▀▀░█░█░░░░░░░░░  █
█  ░█▀▀░█░█░█░█░█▀▄░█▀▀░█▀▀░█▀▄░█▀▀░█░█░░█░░█▀▀░█▀█░░░░░░░░░  █
█  ░▀▀▀░▀▀▀░▀▀░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░░░░░░░░░  █
█                                                               █
█  ⚡ LIGHTWEIGHT ASYNCHRONOUS CLICKJACKING SCANNER            █
█  🔍 BUILT FOR MODERN SECURITY TESTING                        █
█  🚀 FAST - CLEAN - FOCUSED                                   █
█                                                               █
█████████████████████████████████████████████████████████████████
```

---

## 🐍 PYTHON HACKER TOOLKIT

```
┌─────────────────────────────────────────────────────────────────┐
│  🐍 PYTHON HACKER ESSENTIALS                                    │
├─────────────────────────────────────────────────────────────────┤
│  ► Async/Await Architecture                                     │
│  ► Socket Programming                                           │
│  ► Header Manipulation                                          │
│  ► Multi-threading Engine                                       │
│  ► Response Parsing                                             │
│  ► Colored Terminal Output                                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔥 FEATURES

```
┌─────────────────────────────────────────────────────────────────┐
│  ⚡ CORE ENGINE                      🛡️ SECURITY LAYER          │
├─────────────────────────────────────────────────────────────────┤
│  ▶ Asynchronous Scanner              ▶ X-Frame-Options Check   │
│  ▶ 1000+ req/second                  ▶ CSP Analysis            │
│  ▶ Low Memory Footprint               ▶ Header Inspection       │
│  ▶ Configurable Threads               ▶ Real-time Detection     │
│  ▶ Timeout Control                    ▶ Risk Assessment        │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ INSTALLATION

```bash
# ▶ CLONE THE REPOSITORY
git clone https://github.com/LindHunt/clickjackingscan.git
cd clickjackingscan

# ▶ SETUP VIRTUAL ENVIRONMENT
python3 -m venv venv
source venv/bin/activate

# ▶ INSTALL DEPENDENCIES
pip install -r requirements.txt
```

---

## 🚀 USAGE

```bash
# ▶ SINGLE TARGET SCAN
python clickscan.py -u https://example.com

# ▶ BULK SCAN FROM FILE
python clickscan.py -list targets.txt

# ▶ SAVE OUTPUT TO FILE
python clickscan.py -u https://example.com -o result.txt

# ▶ ADVANCED CONFIGURATION
python clickscan.py -list urls.txt -o results.txt --timeout 15 --threads 100
```

---

## 📟 TERMINAL OUTPUT

```
┌─────────────────────────────────────────────────────────────────┐
│  🐍 LINDHUNT CLICKJACKING SCANNER v1.0                         │
│  ⚡ INITIALIZING...                                             │
│  🔍 TARGETS LOADED: 10                                          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  ✅ https://google.com        │ X-FRAME-OPTIONS: SAMEORIGIN    │
│  ❌ https://test.com           │ NO HEADERS FOUND               │
│  ✅ https://github.com        │ CSP: FRAME-ANCESTORS 'SELF'    │
│  ❌ https://oldsite.net        │ XFO: ALLOW-FROM (DEPRECATED)  │
│  ✅ https://microsoft.com      │ X-FRAME-OPTIONS: DENY         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  📊 SCAN SUMMARY                                                │
├─────────────────────────────────────────────────────────────────┤
│  ✅ PROTECTED  : 7                                              │
│  ❌ VULNERABLE : 3                                              │
│  ⏱️ TIME       : 2.3 SECONDS                                    │
│  ⚡ SPEED      : 435 REQ/SEC                                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛡️ SECURITY HEADERS

```
╔═════════════════════════════════════════════════════════════════╗
║  HEADER                    SECURE VALUES          STATUS      ║
╠═════════════════════════════════════════════════════════════════╣
║  X-Frame-Options           DENY                   ✅ SECURE   ║
║  X-Frame-Options           SAMEORIGIN             ✅ SECURE   ║
║  CSP: frame-ancestors      'none'                 ✅ SECURE   ║
║  CSP: frame-ancestors      'self'                 ✅ SECURE   ║
║  NO HEADERS                N/A                     ❌ RISK    ║
╚═════════════════════════════════════════════════════════════════╝
```

---

## 📦 DEPENDENCIES

<p align="center">
  <img src="https://img.shields.io/badge/aiohttp-3.9.0-00FF00?style=for-the-badge&logo=python&logoColor=white&labelColor=black" />
  <img src="https://img.shields.io/badge/colorama-0.4.6-00FF00?style=for-the-badge&logo=python&logoColor=white&labelColor=black" />
  <img src="https://img.shields.io/badge/asyncio-3.4.3-00FF00?style=for-the-badge&logo=python&logoColor=white&labelColor=black" />
</p>

---

## 🔧 CODE SNIPPET

```python
import aiohttp
import asyncio
from colorama import Fore, Style

async def scan_target(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=10) as response:
                headers = response.headers
                xfo = headers.get('X-Frame-Options', '')
                csp = headers.get('Content-Security-Policy', '')
                
                if 'DENY' in xfo or 'SAMEORIGIN' in xfo:
                    return f"{Fore.GREEN}[SECURE]{Style.RESET_ALL} {url}"
                else:
                    return f"{Fore.RED}[VULNERABLE]{Style.RESET_ALL} {url}"
        except:
            return f"{Fore.YELLOW}[ERROR]{Style.RESET_ALL} {url}"
```

---

## 📊 METRICS

<p align="center">
  <img src="https://img.shields.io/github/stars/LindHunt/clickjackingscan?style=for-the-badge&logo=github&color=00FF00&labelColor=black" />
  <img src="https://img.shields.io/github/forks/LindHunt/clickjackingscan?style=for-the-badge&logo=github&color=00FF00&labelColor=black" />
  <img src="https://img.shields.io/github/issues/LindHunt/clickjackingscan?style=for-the-badge&logo=github&color=00FF00&labelColor=black" />
  <img src="https://img.shields.io/github/last-commit/LindHunt/clickjackingscan?style=for-the-badge&logo=github&color=00FF00&labelColor=black" />
</p>

---

## ⚠️ DISCLAIMER

```
╔═════════════════════════════════════════════════════════════════╗
║  ⚠️  EDUCATIONAL PURPOSES ONLY                                  ║
║  🔒 AUTHORIZED TESTING ONLY                                     ║
║  ⚖️  USERS ASSUME ALL LIABILITY                                ║
║  🚫 UNAUTHORIZED USE PROHIBITED                                ║
╚═════════════════════════════════════════════════════════════════╝
```

---

## 📜 LICENSE

<p align="center">
  <img src="https://img.shields.io/badge/LICENSE-MIT-00FF00?style=for-the-badge&labelColor=black" />
  <img src="https://img.shields.io/badge/COPYRIGHT-2024-LINDHUNT-00FF00?style=for-the-badge&labelColor=black" />
</p>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FF00,100:000000&height=100&section=footer" width="100%" />
</p>

<p align="center">
  <b>🐍 PYTHON HACKER • SECURITY RESEARCHER • OSINT ANALYST 🐍</b>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=LindHunt&style=for-the-badge&color=00FF00&labelColor=black" />
</p>
