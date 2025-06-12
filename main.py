import os
import logging
from passive.dns_enum import get_dns_records
from active.banner_grabber import grab_banner
from active.port_scanner import socket_scan
from active.tech_detect import detect_with_wappalyzer
from passive.subdomain_enum import enumerate_subdomains  
from passive.whois_lookup import get_whois_info, print_whois_info
from cli.cli_handler import handle_cli

# === Logging Setup ===
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/tool.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main():
    args = handle_cli()
    domain = args.domain
    url = f"{args.scheme}://{domain}"

    # === SUBDOMAIN ENUMERATION ===
    if args.subdomains:
        print("\n====== SUBDOMAIN ENUMERATION RESULTS ======\n")
        try:
            logging.info(f"Starting subdomain enumeration for {domain}")
            subdomains = enumerate_subdomains(domain, verbose=True)
            if subdomains:
                print(f"\nTotal Subdomains Found: {len(subdomains)}\n")
                for sub in subdomains:
                    print(f"- {sub}")
                logging.info(f"Subdomains found for {domain}: {len(subdomains)}")
            else:
                print("No subdomains found.")
                logging.info(f"No subdomains found for {domain}")
        except Exception as e:
            print(f"Error in Subdomain Enumeration: {e}")
            logging.error(f"Subdomain Enumeration Error: {e}")

    # === WHOIS LOOKUP ===
    if args.whois:
        print("\n====== WHOIS LOOKUP ======\n")
        try:
            logging.info(f"Starting WHOIS lookup for {domain}")
            whois_data = get_whois_info(domain, verbose=True)
            if whois_data:
                print_whois_info(whois_data)
                logging.info(f"WHOIS data retrieved for {domain}")
            else:
                print("WHOIS data not found.")
                logging.warning(f"No WHOIS data found for {domain}")
        except Exception as e:
            print(f"Error in WHOIS Lookup: {e}")
            logging.error(f"WHOIS Lookup Error: {e}")

    # === DNS ENUMERATION ===
    if args.dns:
        print("\n====== DNS ENUMERATION RESULTS ======\n")
        try:
            logging.info(f"Starting DNS enumeration for {domain}")
            dns_results = get_dns_records(domain)
            for record_type, values in dns_results.items():
                print(f"{record_type} Records:")
                for value in values:
                    print(f"- {value}")
                print()
            logging.info(f"DNS records for {domain}: {dns_results}")
        except Exception as e:
            print(f"Error in DNS Enumeration: {e}")
            logging.error(f"DNS Enumeration Error: {e}")

    # === PORT SCANNING ===
    open_ports = []
    if args.ports:
        print("\n====== FULL PORT SCAN (1-65535) ======\n")
        try:
            logging.info(f"Starting full port scan on {domain}")
            open_ports = socket_scan(domain)
            if open_ports:
                print("\nOpen Ports:")
                for port in open_ports:
                    print(f"- Port {port}")
                logging.info(f"Open ports on {domain}: {open_ports}")
            else:
                print("No open ports found.")
                logging.info(f"No open ports found on {domain}")
        except Exception as e:
            print(f"Error in Port Scanning: {e}")
            logging.error(f"Port Scanning Error: {e}")

    # === BANNER GRABBING ===
    if args.banner and open_ports:
        print("\n====== BANNER GRABBING RESULTS ======\n")
        try:
            logging.info(f"Starting banner grabbing on {domain}")
            banner_results = grab_banner(domain, open_ports)
            for port, banner in banner_results.items():
                print(f"[Port {port}] {banner}")
            logging.info(f"Banners grabbed: {banner_results}")
        except Exception as e:
            print(f"Error in Banner Grabbing: {e}")
            logging.error(f"Banner Grabbing Error: {e}")
    elif args.banner:
        print("\nSkipping Banner Grabbing (no open ports found).")
        logging.warning(f"Banner grabbing skipped: no open ports found on {domain}")

    # === TECHNOLOGY DETECTION ===
    if args.tech:
        print("\n====== TECHNOLOGY DETECTION (Wappalyzer) ======\n")
        try:
            logging.info(f"Starting technology detection on {url}")
            tech_result = detect_with_wappalyzer(url)
            if isinstance(tech_result, set):
                print("Detected Technologies:")
                for tech in tech_result:
                    print(f"- {tech}")
                logging.info(f"Technologies detected on {url}: {list(tech_result)}")
            elif isinstance(tech_result, dict) and "error" in tech_result:
                print(tech_result["error"])
                logging.warning(f"Technology detection error on {url}: {tech_result['error']}")
            else:
                print("No technologies detected or unexpected result.")
                logging.info(f"No technologies detected on {url}")
        except Exception as e:
            print(f"Error in Technology Detection: {e}")
            logging.error(f"Technology Detection Error: {e}")

if __name__ == "__main__":
    main()
