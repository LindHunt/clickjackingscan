LINDHUNT Clickjacking Scanner

Lightweight asynchronous clickjacking scanner built for modern security testing.

Features

Asynchronous high-speed scanning

Single target mode (-u)

Multi target mode (-list)

Output file support (-o)

Intelligent header analysis

X-Frame-Options

Content-Security-Policy (frame-ancestors)

Clean colored CLI output

Summary statistics

Installation
git clone https://github.com/LindHunt/clickjackingscan.git
cd clickjackingscan
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Usage
Single target
python clickscan.py -u https://example.com
Multiple targets
python clickscan.py -list targets.txt
Save output
python clickscan.py -u https://example.com -o result.txt
Example
[PROTECTED] https://example.com | XFO: SAMEORIGIN
[VULNERABLE] https://test.com | No anti-clickjacking headers
Disclaimer

This tool is intended for educational purposes and authorized security testing only.
