# lab12_q1_starter.py
import socket
import urllib.request
import urllib.error

class Scanner:
    """Parent class for all scanners"""
    
    def __init__(self, target):
        """Initialize with a target (IP or URL)"""
        self.target = target
        self.results = []
    
    def display_results(self):
        """Display all scan results"""
        if not self.results:
            print(f"No results found for {self.target}")
        else:
            print(f"Results for {self.target}:")
            for result in self.results:
                print(f"  - {result}")


class PortScanner(Scanner):
    """Scans ports on a target IP address"""
    
    def __init__(self, target, ports):
        """Initialize with target and list of ports to scan"""
        super().__init__(target)  
        self.ports = ports
    
    def scan(self):
        """Scan all ports using socket.connect_ex()"""
        
        for port in self.ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                self.results.append(f"Port {port}: OPEN")
            sock.close()
class HTTPScanner(Scanner):
    """Checks HTTP paths on a website"""
    
    def __init__(self, target, paths):
        """Initialize with target URL and list of paths to check"""
        super().__init__(target)  
        self.paths = paths
    
    def scan(self):
        """Check each path using urllib"""
        for path in self.paths:
            url = f"http://{self.target}{path}"
            try:
                response = urllib.request.urlopen(url)
                if response.getcode() == 200:
                    self.results.append(f"Path '{path}': FOUND (Status 200)")
            except urllib.error.URLError:
                self.results.append(f"Path '{path}': NOT FOUND")

# Test the classes
if __name__ == "__main__":
    print("=" * 50)
    print("Q1: Scanner Inheritance Test")
    print("=" * 50)
    # Test PortScanner
    print("\n--- Port Scanner Test ---")
    port_scanner = PortScanner("127.0.0.1", [80, 443, 8080, 22])
    port_scanner.scan()
    port_scanner.display_results()
    # Test HTTPScanner
    print("\n--- HTTP Scanner Test ---")
    http_scanner = HTTPScanner("example.com", ["/", "/about", "/contact", "/nonexistent"])
    http_scanner.scan()
    http_scanner.display_results()