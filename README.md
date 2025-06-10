# custom_recon_tool
Functionality of a Banner Grabber

A Banner Grabber is a reconnaissance tool used in **network security and penetration testing** to gather **information from open ports** on a target system or server. The goal is to **collect banners—text responses from services running on those ports—which often include:

* Service name (e.g., Apache, OpenSSH)
* Version number
* Operating system details
* Miscellaneous metadata

Why is Banner Grabbing Important?

* Identify running services and versions.
* Detect vulnerabilities associated with specific service versions.
* Footprinting and attack surface analysis.

---

### 🧪 Example Output of Banner Grabbing

```bash
Connected to 192.168.1.1:80
Received banner: HTTP/1.1 200 OK
Server: Apache/2.4.41 (Ubuntu)
```

# ✅ Requirements to Run a Banner Grabber Script

1. **Python Environment**

You’ll need Python (usually Python 3):

```bash
python3 --version
```

 2. **Dependencies**

No third-party modules are usually required. The basic version uses the built-in `socket` module.


## 🔐 How a Pentester Benefits from Banner Grabbing

1. **Identify Services** – Reveals what services are running (e.g., SSH, Apache).
2. **Detect Versions** – Exposes software versions to find known vulnerabilities (CVEs).
3. **Plan Exploits** – Helps choose the right tools or exploits for detected services.
4. **Find Misconfigurations** – Overly detailed banners can be reported as information disclosure.
5. **Support Phishing** – Banner info can aid in crafting tech-specific phishing attacks.

> 📌 **Example**: `Server: Apache/2.4.49 (Ubuntu)` → Known vulnerability: [CVE-2021-41773](https://nvd.nist.gov/vuln/detail/CVE-2021-41773)

 
# Example usage
banner_grab("example.com", 80)

# Run the script
python3 banner_grabber.py

# Customize
You can loop over multiple ports or hosts for broader scanning:

```python
for port in [21, 22, 80, 443]:
    banner_grab("192.168.1.10", port)



