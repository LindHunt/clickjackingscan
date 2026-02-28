# LINDHUNT CLICKJACKING SCANNER

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=CLICKJACKING%20SCANNER&fontSize=40&fontAlignY=35&desc=Asynchronous%20Security%20Tool&descAlignY=55&descSize=18" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-000000?style=flat-square&logo=github&logoColor=white&labelColor=2D2D2D" />
  <img src="https://img.shields.io/badge/Python-3.8+-000000?style=flat-square&logo=python&logoColor=white&labelColor=2D2D2D" />
  <img src="https://img.shields.io/badge/License-MIT-000000?style=flat-square&logo=open-source-initiative&logoColor=white&labelColor=2D2D2D" />
</p>

---

## PROJECT OVERVIEW

```
╔══════════════════════════════════════════════════════════════╗
║  Lightweight asynchronous clickjacking scanner              ║
║  Built for modern security testing                           ║
║  Fast. Clean. Focused.                                       ║
╚══════════════════════════════════════════════════════════════╝
```

---

## FEATURES

```
┌─────────────────────────────────────────────────────────────┐
│  CORE FEATURES                    PERFORMANCE              │
├─────────────────────────────────────────────────────────────┤
│  Asynchronous Scanning            High-speed req/sec       │
│  Single Target Mode (-u)          Low Memory Usage         │
│  Multi Target Mode (-list)         Configurable Threads    │
│  Output Support (-o)               Real-time Stats         │
│  Smart Header Analysis             Colored Output          │
│  X-Frame-Options Check             Summary Reports         │
│  CSP frame-ancestors Check         Timeout Control         │
└─────────────────────────────────────────────────────────────┘
```

---

## INSTALLATION

```bash
# Step 1: Clone Repository
git clone https://github.com/LindHunt/clickjackingscan.git
cd clickjackingscan

# Step 2: Setup Environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Step 3: Install Dependencies
pip install -r requirements.txt
```

---

## USAGE COMMANDS

```bash
# Scan Single Target
python clickscan.py -u https://example.com

# Scan Multiple Targets
python clickscan.py -list targets.txt

# Save Results to File
python clickscan.py -u https://example.com -o result.txt

# Advanced Scan
python clickscan.py -list urls.txt -o results.txt --timeout 10 --threads 100
```

---

## SCAN OUTPUT EXAMPLE

```
┌──────────────────────────────────────────────────────────────┐
│  LINDHUNT CLICKJACKING SCANNER v1.0                         │
│  Scanning in progress...                                     │
└──────────────────────────────────────────────────────────────┘

[PROTECTED]   https://google.com     | XFO: SAMEORIGIN
[VULNERABLE]  https://test.com        | No Headers Found
[PROTECTED]   https://github.com      | CSP: frame-ancestors 'self'
[VULNERABLE]  https://oldsite.net     | XFO: ALLOW-FROM
[PROTECTED]   https://microsoft.com   | XFO: DENY
[VULNERABLE]  https://example.org     | No Security Headers

┌──────────────────────────────────────────────────────────────┐
│  FINAL STATISTICS                                            │
├──────────────────────────────────────────────────────────────┤
│  PROTECTED  :  3                                             │
│  VULNERABLE :  3                                             │
│  ERRORS     :  0                                             │
│  TIME       :  2.3 seconds                                   │
└──────────────────────────────────────────────────────────────┘
```

---

## SECURITY HEADERS CHECKED

| Header | Secure Values | Vulnerable |
|--------|--------------|------------|
| X-Frame-Options | DENY, SAMEORIGIN | Missing / ALLOW-FROM |
| CSP: frame-ancestors | 'none', 'self' | Missing / * |
| X-Frame-Options + CSP | Both present | Only one present |

---

## TECHNOLOGY STACK

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/aiohttp-2C5BB4?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/asyncio-0078D7?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/colorama-FF6C37?style=flat-square&logo=python&logoColor=white" />
</p>

---

## GITHUB STATISTICS

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=LindHunt&show_icons=true&theme=dark&count_private=true&hide_border=true&bg_color=0D1117&title_color=58A6FF&icon_color=58A6FF&text_color=C9D1D9" width="49%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=LindHunt&layout=compact&theme=dark&hide_border=true&bg_color=0D1117&title_color=58A6FF&text_color=C9D1D9" width="49%" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=LindHunt&theme=dark&hide_border=true&background=0D1117&stroke=58A6FF&ring=58A6FF&fire=FF6B6B&currStreakLabel=58A6FF" width="49%" />
  <img src="https://github-profile-trophy.vercel.app/?username=LindHunt&theme=onedark&no-frame=true&row=2&column=3&margin-w=15&margin-h=15" width="49%" />
</p>

---

## PROJECT METRICS

<p align="center">
  <img src="https://img.shields.io/github/stars/LindHunt/clickjackingscan?style=flat-square&logo=github&color=yellow" />
  <img src="https://img.shields.io/github/forks/LindHunt/clickjackingscan?style=flat-square&logo=github&color=blue" />
  <img src="https://img.shields.io/github/issues/LindHunt/clickjackingscan?style=flat-square&logo=github&color=red" />
  <img src="https://img.shields.io/github/last-commit/LindHunt/clickjackingscan?style=flat-square&logo=github&color=green" />
</p>

---

## DISCLAIMER

```
╔══════════════════════════════════════════════════════════════╗
║  This tool is for educational purposes and                  ║
║  authorized security testing only.                          ║
║  Unauthorized use against systems without                   ║
║  explicit permission is prohibited.                         ║
║  Users assume all liability for their actions.              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## LICENSE

<p align="center">
  <img src="https://img.shields.io/badge/LICENSE-MIT-000000?style=flat-square&labelColor=2D2D2D" />
  <img src="https://img.shields.io/badge/COPYRIGHT-2024_LindHunt-000000?style=flat-square&labelColor=2D2D2D" />
</p>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" width="100%" />
</p>

<p align="center">
  <b>Star if useful • Made by LindHunt</b>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=LindHunt&style=flat-square&color=58A6FF" />
</p>
