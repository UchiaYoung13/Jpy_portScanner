import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Timeout in seconds
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception as e:
        return False
    
def scan_ports(ip, start_port, end_port):
    print(f"Scanning {ip} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            print(f"Port {port}: OPEN")
            
            
if __name__ == "__main__":
    target = input("Enter target IP (e.g., 127.0.0.1):")
    start = int(input("Start port (e.g., 1):"))
    end = int(input("End port (e.g., 100):"))
    scan_ports(target, start, end)