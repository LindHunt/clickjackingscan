# LINDHUNT Clickjacking Scanner

Asynchronous Clickjacking vulnerability scanner written in Python.

 Features

- Async high-speed scanning
- Single target mode (-u)
- Multi target mode (-list)
- Output file support (-o)
- Smart header analysis (X-Frame-Options & CSP frame-ancestors)
- Clean colored CLI output

 Installation
git clone https://github.com/yourusername/lindhunt-clickjacking.git
cd lindhunt-clickjacking
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
