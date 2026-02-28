🚀 LINDHUNT Clickjacking Scanner

Lightweight asynchronous clickjacking scanner built for modern security testing.

Fast. Clean. Focused.

✨ Features

⚡ Asynchronous high-speed scanning

🎯 Single target mode (-u)

📂 Multi target mode (-list)

💾 Output file support (-o)

🧠 Intelligent header analysis

X-Frame-Options

Content-Security-Policy (frame-ancestors)

🎨 Clean colored CLI output

📊 Summary statistics

🛠 Installation
git clone https://github.com/LindHunt/clickjackingscan.git
cd clickjackingscan

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
🚦 Usage
🔎 Scan Single Target
python clickscan.py -u https://example.com
📂 Scan Multiple Targets
python clickscan.py -list targets.txt
💾 Save Output to File
python clickscan.py -u https://example.com -o result.txt
🖥 Example Output
[PROTECTED] https://example.com | XFO: SAMEORIGIN
[VULNERABLE] https://test.com | No anti-clickjacking headers

------------------------------------------------------------
Protected: 1
Vulnerable: 1
Errors: 0
⚠ Disclaimer

This tool is intended for educational purposes and authorized security testing only.
Unauthorized use against systems without permission is strictly prohibited.




# 👋 Hello, I'm LindHunt

🛰 OSINT Analyst & Security Researcher  
⚡ Building lightweight security utilities  

---

## 📊 GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=LindHunt&show_icons=true&theme=tokyonight)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=LindHunt&layout=compact&theme=tokyonight)
