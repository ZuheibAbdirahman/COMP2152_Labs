# lab11_q1_complete.py
import socket

class PortScanner:
    def __init__(self, target):
        """Initialize scanner with target host"""
        self.target = target
        self.open_ports = []
    
    def scan_port(self, port):
        """Check if a specific port is open on the target"""
        sock = None
        try:
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            # Try to connect
            result = sock.connect_ex((self.target, port))
            
            # If result is 0, port is open
            if result == 0:
                print(f"  Port {port}: OPEN")
                self.open_ports.append(port)
                return True
            else:
                return False
                
        except socket.error:
            return False
        finally:
            if sock:
                sock.close()
    
    def scan_range(self, start_port, end_port):
        """Scan a range of ports from start_port to end_port (inclusive)"""
        print(f"  Scanning {self.target} ports {start_port}-{end_port}...")
        for port in range(start_port, end_port + 1):
            self.scan_port(port)
    
    def display_results(self):
        """Display the scan results"""
        print(f"Results for {self.target}:")
        if not self.open_ports:
            print("  No open ports found.")
        else:
            for port in self.open_ports:
                print(f"  Port {port}")


def main():
    print("=" * 60)
    print("  Q1: PORT SCANNER CLASS")
    print("=" * 60)
    print()
    
    # Scanner 1 - scanning common web ports on localhost
    print("--- Scanner 1: localhost ---")
    scanner1 = PortScanner("127.0.0.1")
    scanner1.scan_range(78, 82)
    scanner1.display_results()
    print()
    
    # Scanner 2 - scanning a different range
    print("--- Scanner 2: different target ---")
    scanner2 = PortScanner("127.0.0.1")
    scanner2.scan_range(20, 25)
    scanner2.display_results()
    print()
    
    print("=" * 60)


if __name__ == "__main__":
    main()