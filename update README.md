# custom_recon_tool
# 🔍 Reconnaissance Tool

A powerful and modular Python-based reconnaissance framework for ethical hackers and cybersecurity researchers. This tool performs passive and active recon to gather information about a target, including subdomains, DNS records, WHOIS info, open ports, banners, and technologies used.

---

## 📁 Project Structure

```
Reconnaissance-Tool/
├── active/
│   ├── banner_grabber.py
│   ├── port_scanner.py
│   └── tech_detect.py
├── passive/
│   ├── dns_enum.py
│   ├── subdomain_enum.py
│   └── whois_lookup.py
├── cli/
│   └── cli_handler.py
├── logs/
│   └── tool.log
├── main.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Features

- ✅ Subdomain Enumeration using crt.sh  
- ✅ WHOIS Lookup  
- ✅ DNS Record Enumeration (A, NS, MX, TXT, SOA)  
- ✅ Full TCP Port Scan (1–65535)  
- ✅ Banner Grabbing on Open Ports  
- ✅ Technology Detection using Wappalyzer  
- ✅ Logging to `logs/tool.log`

---

## 🐍 Requirements

- Python 3.8 or higher

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Libraries Used:**

- `requests`  
- `dnspython`  
- `whois`  
- `Wappalyzer`

---

## 🚀 Usage

Run the tool using:

```bash
python3 main.py <domain> [options]
```

### Example:

```bash
python3 main.py testphp.vulnweb.com --subdomains --whois --dns --ports --banner --tech
```

### CLI Options:

| Option         | Description                                  |
|----------------|----------------------------------------------|
| `<domain>`     | Target domain (e.g. example.com)             |
| `--scheme`     | URL scheme (http or https), default is http  |
| `--subdomains` | Perform subdomain enumeration                |
| `--whois`      | Perform WHOIS lookup                         |
| `--dns`        | Enumerate DNS records                        |
| `--ports`      | Scan all ports (1–65535)                     |
| `--banner`     | Grab banners from open ports                 |
| `--tech`       | Detect web technologies (via Wappalyzer)     |

---

## 📄 Logging

All actions are logged in:

```bash
logs/tool.log
```

Use this file to review scan details, errors, and summaries.

---

## 🧪 Sample Output

```
====== SUBDOMAIN ENUMERATION RESULTS ======
- admin.testphp.vulnweb.com
- dev.testphp.vulnweb.com

====== WHOIS LOOKUP ======
Registrar: NameCheap, Inc.
Created: 2010-04-15
Expires: 2030-04-15

====== DNS ENUMERATION RESULTS ======
A Records:
- 93.184.216.34

MX Records:
- mail.vulnweb.com

====== FULL PORT SCAN (1–65535) ======
Open Ports:
- Port 80
- Port 443

====== BANNER GRABBING RESULTS ======
[Port 80] HTTP/1.1 200 OK
[Port 443] HTTP/1.1 301 Moved Permanently

====== TECHNOLOGY DETECTION (Wappalyzer) ======
- Apache
- Bootstrap
- Google Analytics
```

---

## ⚠️ Disclaimer

This tool is intended for educational and authorized use only.  
**Unauthorized scanning or enumeration of systems without permission may be illegal.**  
The author is not responsible for any misuse.

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---
