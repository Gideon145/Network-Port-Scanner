import socket

def scan_ports(host, ports):
    print(f"Scanning {host} for open ports...\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"✅ Port {port} is OPEN")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    target_host = input("Enter target IP or hostname: ")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]
    scan_ports(target_host, common_ports)