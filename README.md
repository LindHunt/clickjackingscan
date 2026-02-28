# 🚀 **LINDHUNT CLICKJACKING SCANNER**

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=500&color=00FF00&center=true&vCenter=true&width=600&lines=⚡+CLICKJACKING+SCANNER;🔍+ASYNCHRONOUS+SECURITY+TOOL;🛡️+WEB+VULNERABILITY+DETECTOR;🚀+FAST+%26+LIGHTWEIGHT" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-00FF00?style=for-the-badge&logo=python&logoColor=white&labelColor=black" alt="Version">
  <img src="https://img.shields.io/badge/python-3.8+-00FF00?style=for-the-badge&logo=python&logoColor=white&labelColor=black" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-00FF00?style=for-the-badge&logo=open-source-initiative&logoColor=white&labelColor=black" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-00FF00?style=for-the-badge&logo=github&logoColor=white&labelColor=black" alt="PRs">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/OSINT-Analyst-FF00FF?style=for-the-badge&logo=grafana&logoColor=white&labelColor=black" alt="OSINT">
  <img src="https://img.shields.io/badge/Security-Researcher-FF00FF?style=for-the-badge&logo=security&logoColor=white&labelColor=black" alt="Security">
  <img src="https://img.shields.io/badge/Ethical-Hacker-FF00FF?style=for-the-badge&logo=hackthebox&logoColor=white&labelColor=black" alt="Hacker">
</p>

<br>

<p align="center">
  <img src="https://profile-counter.glitch.me/LindHunt/count.svg" alt="Visitor Count" />
</p>

---

## ⚡ **FEATURES MATRIX**

```
┌─────────────────────────────────────────────────────────────────┐
│  🔥 CORE FEATURES                     ⚡ PERFORMANCE            │
├─────────────────────────────────────────────────────────────────┤
│  🚀 Asynchronous Scanning            │  ⚡ 1000+ req/sec        │
│  🎯 Single Target Mode (-u)          │  🔋 Low Memory Usage     │
│  📂 Multi Target Mode (-list)         │  ⚙️ Configurable Threads │
│  💾 Output Support (-o)               │  📊 Real-time Stats      │
│  🧠 Smart Header Analysis             │  🎨 Colored Output       │
│  🔍 X-Frame-Options Check             │  📈 Summary Reports      │
│  🛡️ CSP frame-ancestors Check         │  ⏱️ Timeout Control      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ **INSTALLATION**

<p align="center">
  <img src="https://img.shields.io/badge/STEP_1-CLONE-00FF00?style=for-the-badge&labelColor=black" alt="Step1">
  <img src="https://img.shields.io/badge/STEP_2-SETUP-00FF00?style=for-the-badge&labelColor=black" alt="Step2">
  <img src="https://img.shields.io/badge/STEP_3-RUN-00FF00?style=for-the-badge&labelColor=black" alt="Step3">
</p>

```bash
# 📥 STEP 1: Clone Repository
git clone https://github.com/LindHunt/clickjackingscan.git
cd clickjackingscan

# 🔧 STEP 2: Setup Environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 📦 STEP 3: Install Dependencies
pip install -r requirements.txt
```

---

## 🚀 **USAGE COMMANDS**

<p align="center">
  <img src="https://img.shields.io/badge/🎯_SINGLE_TARGET-000000?style=for-the-badge&logo=target&logoColor=white&labelColor=red" alt="Single">
  <img src="https://img.shields.io/badge/📂_BULK_SCAN-000000?style=for-the-badge&logo=files&logoColor=white&labelColor=blue" alt="Bulk">
  <img src="https://img.shields.io/badge/💾_SAVE_OUTPUT-000000?style=for-the-badge&logo=save&logoColor=white&labelColor=green" alt="Save">
</p>

```bash
# 🎯 SCAN SINGLE TARGET
python clickscan.py -u https://example.com

# 📂 SCAN MULTIPLE TARGETS
python clickscan.py -list targets.txt

# 💾 SAVE RESULTS TO FILE
python clickscan.py -u https://example.com -o result.txt

# ⚙️ ADVANCED SCAN
python clickscan.py -list urls.txt -o results.txt --timeout 10 --threads 100
```

---

## 📊 **LIVE SCAN EXAMPLE**

```
┌──────────────────────────────────────────────────────────────┐
│  🚀 LINDHUNT CLICKJACKING SCANNER v1.0                       │
│  ⚡ SCANNING IN PROGRESS...                                    │
└──────────────────────────────────────────────────────────────┘

🟢 [PROTECTED]   https://google.com     │ XFO: SAMEORIGIN
🔴 [VULNERABLE]  https://test.com        │ No Headers Found
🟢 [PROTECTED]   https://github.com      │ CSP: frame-ancestors 'self'
🔴 [VULNERABLE]  https://oldsite.net     │ XFO: ALLOW-FROM (Deprecated)
🟢 [PROTECTED]   https://microsoft.com   │ XFO: DENY
🔴 [VULNERABLE]  https://example.org     │ No Security Headers

┌──────────────────────────────────────────────────────────────┐
│  📈 FINAL STATISTICS                                          │
├──────────────────────────────────────────────────────────────┤
│  🟢 PROTECTED  :  3                                           │
│  🔴 VULNERABLE :  3                                           │
│  ⚪ ERRORS     :  0                                           │
│  ⏱️ TIME       :  2.3 seconds                                 │
│  🚀 SPEED      :  150 req/sec                                 │
└──────────────────────────────────────────────────────────────┘
```

---

## 🛡️ **SECURITY HEADERS CHECKED**

<p align="center">
  <img src="https://img.shields.io/badge/X--Frame--Options-DENY-00FF00?style=for-the-badge&labelColor=black" alt="XFO">
  <img src="https://img.shields.io/badge/X--Frame--Options-SAMEORIGIN-00FF00?style=for-the-badge&labelColor=black" alt="XFO2">
  <img src="https://img.shields.io/badge/CSP-frame--ancestors-00FF00?style=for-the-badge&labelColor=black" alt="CSP">
</p>

| 🔒 HEADER | ✅ SECURE VALUES | ⚠️ VULNERABLE | 📝 STATUS |
|-----------|------------------|---------------|-----------|
| `X-Frame-Options` | `DENY`, `SAMEORIGIN` | Missing / `ALLOW-FROM` | 🛡️ Critical |
| `CSP: frame-ancestors` | `'none'`, `'self'` | Missing / `*` | 🛡️ Critical |
| `X-Frame-Options` + `CSP` | Both present | Only one present | 🟡 Medium |

---

## 📦 **TECH STACK**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/aiohttp-2C5BB4?style=for-the-badge&logo=python&logoColor=white" alt="aiohttp">
  <img src="https://img.shields.io/badge/asyncio-0078D7?style=for-the-badge&logo=python&logoColor=white" alt="asyncio">
  <img src="https://img.shields.io/badge/colorama-FF6C37?style=for-the-badge&logo=python&logoColor=white" alt="colorama">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,git,github,vscode&theme=dark" />
</p>

---

## 📊 **GITHUB STATS**

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=LindHunt&show_icons=true&theme=radical&count_private=true&hide_border=true&bg_color=000000&title_color=00FF00&icon_color=00FF00&text_color=FFFFFF" width="49%" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=LindHunt&theme=radical&hide_border=true&background=000000&stroke=00FF00&ring=00FF00&fire=FF0000&currStreakLabel=00FF00" width="49%" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=LindHunt&layout=pie&theme=radical&hide_border=true&bg_color=000000&title_color=00FF00&text_color=FFFFFF" width="40%" />
  <img src="https://github-profile-trophy.vercel.app/?username=LindHunt&theme=radical&no-frame=true&row=2&column=4&margin-w=15&margin-h=15" width="55%" />
</p>

---

## 🎯 **PROJECT METRICS**

<p align="center">
  <img src="https://img.shields.io/github/stars/LindHunt/clickjackingscan?style=for-the-badge&logo=github&color=yellow" alt="Stars">
  <img src="https://img.shields.io/github/forks/LindHunt/clickjackingscan?style=for-the-badge&logo=github&color=blue" alt="Forks">
  <img src="https://img.shields.io/github/issues/LindHunt/clickjackingscan?style=for-the-badge&logo=github&color=red" alt="Issues">
  <img src="https://img.shields.io/github/last-commit/LindHunt/clickjackingscan?style=for-the-badge&logo=github&color=green" alt="Last Commit">
</p>

---

## 🎨 **CONTRIBUTION GRAPH**

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=LindHunt&theme=react-dark&bg_color=000000&color=00FF00&line=00FF00&point=FFFFFF&area=true&hide_border=true" width="100%" />
</p>

---

## ⚠️ **DISCLAIMER**

```
█████████████████████████████████████████████████████████████████
█                                                               █
█  ⚠️  THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY              █
█  🔒 UNAUTHORIZED USE AGAINST SYSTEMS IS PROHIBITED           █
█  ⚖️  USERS ARE RESPONSIBLE FOR THEIR ACTIONS                 █
█  🛡️  ALWAYS GET PERMISSION BEFORE TESTING                    █
█                                                               █
█████████████████████████████████████████████████████████████████
```

---

## 📜 **LICENSE**

<p align="center">
  <img src="https://img.shields.io/badge/LICENSE-MIT-00FF00?style=for-the-badge&logo=bookstack&logoColor=white&labelColor=black&border=1px solid white" alt="MIT" />
</p>

---

## 🎪 **FINAL SHOWCASE**

<p align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />
</p>

<p align="center">
  <b>⚡ Star • 🍴 Fork • 🔧 Contribute</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/MADE_WITH_❤️_BY-LINDHUNT-00FF00?style=for-the-badge&labelColor=black" alt="Made by LindHunt" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />
</p>

<p align="center">
  <img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical" width="80%" />
</p>
