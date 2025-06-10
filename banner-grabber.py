import socket
import logging

def grab_banner(domain, ports):
    banners = {}
    try:
        ip = socket.gethostbyname(domain)
        logging.info(f"[+] Resolved {domain} to {ip}")
    except Exception as e:
        logging.error(f"[-] Failed to resolve {domain}: {e}")
        return {"error": f"Failed to resolve IP: {e}"}

    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)
                s.connect((ip, port))
                if port in [80, 443, 8080]:
                    s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = s.recv(1024).decode(errors='ignore').strip()
                banners[port] = banner if banner else "No banner"
                logging.debug(f"[DEBUG] Banner on port {port}: {banner[:50]}")
        except Exception as e:
            banners[port] = "No banner or connection failed"
            logging.warning(f"[!] Failed on port {port}: {e}")
    return banners
# main block
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    
    domain = "example.com"  
    ports = [80, 443, 21, 22, 8080]  # Ports to test
    
    result = grab_banner(domain, ports)
    for port, banner in result.items():
        print(f"[{port}] {banner}")
