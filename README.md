# 🚀 **LindHunt Clickjacking Scanner**

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/python-3.8+-brightgreen.svg" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

<p align="center">
  <b>⚡ Lightweight asynchronous clickjacking scanner for modern security testing</b><br>
  <i>Fast • Clean • Focused</i>
</p>

---

## ✨ **Features**

| Feature | Description |
|---------|-------------|
| ⚡ Asynchronous | High-speed scanning with async/await |
| 🎯 Single Target | Quick scan one URL with `-u` |
| 📂 Multi Target | Bulk scan from file with `-list` |
| 💾 Output Support | Save results with `-o` |
| 🧠 Smart Analysis | Checks X-Frame-Options & CSP frame-ancestors |
| 🎨 Clean Output | Colored CLI with status icons |
| 📊 Statistics | Summary of protected/vulnerable sites |

---

## 🛠 **Installation**

```bash
# Clone repository
git clone https://github.com/LindHunt/clickjackingscan.git
cd clickjackingscan

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🚦 **Usage**

### 🎯 Single Target
```bash
python clickscan.py -u https://example.com
```

### 📂 Multiple Targets
```bash
python clickscan.py -list targets.txt
```

### 💾 Save Output
```bash
python clickscan.py -u https://example.com -o result.txt
```

---

## 📋 **Example Output**

```
[PROTECTED]   https://example.com     | XFO: SAMEORIGIN
[VULNERABLE]  https://test.com        | No anti-clickjacking headers
[PROTECTED]   https://secure-site.com | CSP: frame-ancestors 'self'

----------------------------------------
Protected: 2
Vulnerable: 1
Errors: 0
```

---

## 📊 **GitHub Stats**

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=LindHunt&show_icons=true&theme=tokyonight&hide_border=true" width="48%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=LindHunt&layout=compact&theme=tokyonight&hide_border=true" width="48%" />
</p>

---

## 🛡️ **Headers Checked**

| Header | Value | Status |
|--------|-------|--------|
| `X-Frame-Options` | `DENY` | ✅ Secure |
| `X-Frame-Options` | `SAMEORIGIN` | ✅ Secure |
| `CSP frame-ancestors` | `'none'` | ✅ Secure |
| `CSP frame-ancestors` | `'self'` | ✅ Secure |
| No headers | - | ⚠️ Vulnerable |

---

## 📦 **Dependencies**

<p align="center">
  <img src="https://img.shields.io/badge/aiohttp-3.9.0-blue.svg" alt="aiohttp">
  <img src="https://img.shields.io/badge/colorama-0.4.6-green.svg" alt="colorama">
  <img src="https://img.shields.io/badge/asyncio-3.4.3-yellow.svg" alt="asyncio">
</p>

---

## 👨‍💻 **About**

🛰 OSINT Analyst & Security Researcher  
⚡ Building lightweight security utilities  

---

## ⚠️ **Disclaimer**

> This tool is for educational purposes and authorized testing only.  
> Unauthorized use against systems without permission is prohibited.

---

## 📄 **License**

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge" alt="MIT License">
</p>

---

<p align="center">
  <b>⭐ Star if useful • Made by LindHunt</b>
</p>
