# 🔍 Python TCP Port Scanner

A simple command-line TCP port scanner written in Python for educational and lab use.

## 📦 Features

- Scans an IP address or domain over a custom port range
- Uses connection timeout to speed up scanning
- Maps open ports to common services (e.g. 22 → SSH)
- Outputs results to the terminal and optionally to a file
- Clean command-line interface with `argparse`

## 🛠️ Usage

```bash
python portscan.py -t 127.0.0.1 -p 20-80 -to 0.5 -o results.txt

