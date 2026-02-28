# LINDHUNT CLICKJACKING SCANNER

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=CLICKJACKING%20SCANNER&fontSize=40&fontAlignY=35&desc=⚡%20Asynchronous%20Security%20Tool&descAlignY=55&descSize=18" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-000000?style=for-the-badge&logo=github&logoColor=white&labelColor=2D2D2D" />
  <img src="https://img.shields.io/badge/Python-3.8+-000000?style=for-the-badge&logo=python&logoColor=white&labelColor=2D2D2D" />
  <img src="https://img.shields.io/badge/License-MIT-000000?style=for-the-badge&logo=open-source-initiative&logoColor=white&labelColor=2D2D2D" />
  <img src="https://img.shields.io/badge/PRs-Welcome-000000?style=for-the-badge&logo=github&logoColor=white&labelColor=2D2D2D" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/OSINT-Analyst-000000?style=for-the-badge&logo=grafana&logoColor=white&labelColor=2D2D2D" />
  <img src="https://img.shields.io/badge/Security-Researcher-000000?style=for-the-badge&logo=tryhackme&logoColor=white&labelColor=2D2D2D" />
</p>

---

## 📋 **PROJECT OVERVIEW**

```
╔══════════════════════════════════════════════════════════════╗
║  ⚡ Lightweight asynchronous clickjacking scanner           ║
║  🔍 Built for modern security testing                       ║
║  🚀 Fast. Clean. Focused.                                   ║
╚══════════════════════════════════════════════════════════════╝
```

---

## ⚙️ **FEATURES**

| Feature | Description |
|---------|-------------|
| ⚡ Asynchronous | High-speed scanning with async/await |
| 🎯 Single Target | Quick scan one URL with `-u` |
| 📂 Multi Target | Bulk scan from file with `-list` |
| 💾 Output Support | Save results with `-o` |
| 🧠 Smart Analysis | X-Frame-Options & CSP frame-ancestors |
| 🎨 Clean Output | Colored CLI with status icons |
| 📊 Statistics | Summary of protected/vulnerable sites |

---

## 🛠️ **INSTALLATION**

```bash
# 📥 Clone repository
git clone https://github.com/LindHunt/clickjackingscan.git
cd clickjackingscan

# 🔧 Setup virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 📦 Install dependencies
pip install -r requirements.txt
```

---

## 🚀 **USAGE**

```bash
# 🎯 Single target
python clickscan.py -u https://example.com

# 📂 Multiple targets
python clickscan.py -list targets.txt

# 💾 Save output
python clickscan.py -u https://example.com -o result.txt

# ⚙️ Advanced options
python clickscan.py -list urls.txt -o results.txt --timeout 10 --threads 50
```

---

## 📊 **EXAMPLE OUTPUT**

```
┌─────────────────────────────────────────────────────────────┐
│  🚀 LINDHUNT CLICKJACKING SCANNER v1.0                      │
└─────────────────────────────────────────────────────────────┘

✅ [PROTECTED]   https://google.com     | XFO: SAMEORIGIN
❌ [VULNERABLE]  https://test.com        | No Headers Found
✅ [PROTECTED]   https://github.com      | CSP: frame-ancestors 'self'
❌ [VULNERABLE]  https://oldsite.net     | XFO: ALLOW-FROM
✅ [PROTECTED]   https://microsoft.com   | XFO: DENY

┌─────────────────────────────────────────────────────────────┐
│  📈 SUMMARY                                                 │
├─────────────────────────────────────────────────────────────┤
│  ✅ Protected  : 3                                          │
│  ❌ Vulnerable : 2                                          │
│  ⚪ Errors     : 0                                          │
│  ⏱️ Time       : 2.1 seconds                                │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛡️ **HEADERS CHECKED**

| Header | Secure | Status |
|--------|--------|--------|
| `X-Frame-Options: DENY` | ✅ | Protected |
| `X-Frame-Options: SAMEORIGIN` | ✅ | Protected |
| `CSP: frame-ancestors 'none'` | ✅ | Protected |
| `CSP: frame-ancestors 'self'` | ✅ | Protected |
| No Headers | ❌ | Vulnerable |

---

## 📦 **TECH STACK**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/aiohttp-2C5BB4?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/asyncio-0078D7?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/colorama-FF6C37?style=for-the-badge&logo=python&logoColor=white" />
</p>

---

## 🔥 **ACHIEVEMENTS**

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=LindHunt&theme=onedark&no-frame=true&row=2&column=4&margin-w=15&margin-h=15" width="80%" />
</p>

---

## 📈 **WAKATIME METRICS**

<p align="center">
  <img src="https://wakatime.com/badge/user/018d7c0e-8e2a-4b3f-9f1a-5d3c8b2f4e1a.svg?style=for-the-badge" />
</p>

---

## 🔥 **CONTRIBUTION CALENDAR**

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=LindHunt&theme=github-dark&hide_border=true&area=true" width="95%" />
</p>

---

## 🎯 **CURRENT FOCUS**

```
┌─────────────────────────────────────────────────────────┐
│  🔴 Web Security Testing          ████████░░ 80%       │
│  🟡 OSINT Development              ██████░░░░ 60%       │
│  🟢 Tool Optimization              ███████░░░ 70%       │
│  🔵 Documentation                  █████░░░░░ 50%       │
└─────────────────────────────────────────────────────────┘
```

---

## 📊 **PROJECT METRICS**

<p align="center">
  <img src="https://img.shields.io/github/stars/LindHunt/clickjackingscan?style=for-the-badge&logo=github&color=yellow" />
  <img src="https://img.shields.io/github/forks/LindHunt/clickjackingscan?style=for-the-badge&logo=github&color=blue" />
  <img src="https://img.shields.io/github/issues/LindHunt/clickjackingscan?style=for-the-badge&logo=github&color=red" />
  <img src="https://img.shields.io/github/last-commit/LindHunt/clickjackingscan?style=for-the-badge&logo=github&color=green" />
</p>

---

## ⚠️ **DISCLAIMER**

```
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  Educational purposes only                               ║
║  🔒 Authorized testing only                                  ║
║  ⚖️  Users assume all liability                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 📜 **LICENSE**

<p align="center">
  <img src="https://img.shields.io/badge/LICENSE-MIT-000000?style=for-the-badge&labelColor=2D2D2D" />
  <img src="https://img.shields.io/badge/COPYRIGHT-2024_LindHunt-000000?style=for-the-badge&labelColor=2D2D2D" />
</p>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" width="100%" />
</p>

<p align="center">
  <b>⭐ Star if useful • Made by LindHunt</b>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=LindHunt&style=for-the-badge&color=58A6FF" />
</p>
