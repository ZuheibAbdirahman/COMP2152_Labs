# assignment2_101201301.py
"""
Author: Zuheib Abdirahman Student ID: 101549351
Assignment: #2
Description: Port Scanner — A tool that scans a target machine for open network ports
"""

import socket
import threading
import sqlite3
import os
import platform
import datetime

# Print Python version and operating system name
print(f"Python Version: {platform.python_version()}")
print(f"Operating System: {os.name}")

# Dictionary mapping common port numbers to their service names
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt"
}


class NetworkTool:
    """Parent class for network tools"""
    
    def __init__(self, target):
        """Constructor that stores target as private property"""
        self.__target = target
    
    # Q3: What is the benefit of using @property and @target.setter?
    # The @property decorator allows us to access the private attribute like a regular attribute
    # while maintaining control over how it's accessed. The setter adds validation logic to ensure
    # data integrity by checking if the target is empty before setting it.
    @property
    def target(self):
        """Getter for target property"""
        return self.__target
    
    @target.setter
    def target(self, value):
        """Setter for target property with validation"""
        if value == "":
            print("Error: Target cannot be empty")
        else:
            self.__target = value
    
    def __del__(self):
        """Destructor that prints when instance is destroyed"""
        print("NetworkTool instance destroyed")


class PortScanner(NetworkTool):
    """Child class that inherits from NetworkTool for port scanning"""
    
    # Q1: How does PortScanner reuse code from NetworkTool?
    # PortScanner inherits from NetworkTool, which allows it to reuse the target property
    # and its validation logic without rewriting the code. For example, when we create a
    # PortScanner object with a target IP, it automatically gets the target property and
    # validation from the parent class through inheritance.
    
    def __init__(self, target):
        """Constructor that initializes scan_results and lock"""
        super().__init__(target)
        self.scan_results = []
        self.lock = threading.Lock()
    
    def __del__(self):
        """Destructor that prints and calls parent destructor"""
        print("PortScanner instance destroyed")
        super().__del__()
    
    def scan_port(self, port):
        """Scan a single port to check if it's open"""
        # Q4: What would happen without try-except here?
        # Without try-except blocks, the program would crash with an unhandled socket.error
        # exception when scanning unreachable ports. This would terminate the entire scanning
        # process and prevent other ports from being scanned, making the tool unreliable.
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            
            if result == 0:
                status = "Open"
            else:
                status = "Closed"
            
            # Look up service name from common_ports dictionary
            service_name = common_ports.get(port, "Unknown")
            
            # Add result to scan_results with thread safety
            with self.lock:
                self.scan_results.append((port, status, service_name))
                
        except socket.error as e:
            print(f"Error scanning port {port}: {e}")
        finally:
            sock.close()
    
    def get_open_ports(self):
        """Return only open ports using list comprehension"""
        return [result for result in self.scan_results if result[1] == "Open"]
    
    # Q2: Why do we use threading instead of scanning one port at a time?
    # Threading allows multiple ports to be scanned simultaneously, dramatically reducing the
    # total scan time. Without threading, scanning 1024 ports sequentially would take at least
    # 1024 seconds (over 17 minutes) with a 1-second timeout per port, which is impractical
    # for a port scanner tool.
    def scan_range(self, start_port, end_port):
        """Scan a range of ports using multiple threads"""
        threads = []
        
        # Create threads for each port
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=self.scan_port, args=(port,))
            threads.append(thread)
        
        # Start all threads
        for thread in threads:
            thread.start()
        
        # Join all threads
        for thread in threads:
            thread.join()


def save_results(target, results):
    """Save scan results to SQLite database"""
    try:
        conn = sqlite3.connect("scan_history.db")
        cursor = conn.cursor()
        
        # Create scans table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT,
                port INTEGER,
                status TEXT,
                service TEXT,
                scan_date TEXT
            )
        """)
        
        # Insert each result
        for port, status, service in results:
            scan_date = str(datetime.datetime.now())
            cursor.execute("""
                INSERT INTO scans (target, port, status, service, scan_date)
                VALUES (?, ?, ?, ?, ?)
            """, (target, port, status, service, scan_date))
        
        conn.commit()
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def load_past_scans():
    """Load and display past scan history from database"""
    try:
        conn = sqlite3.connect("scan_history.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM scans")
        rows = cursor.fetchall()
        
        if rows:
            for row in rows:
                print(f"[{row[5]}] {row[1]} : Port {row[2]} ({row[4]}) - {row[3]}")
        else:
            print("No past scans found.")
            
    except sqlite3.Error:
        print("No past scans found.")
    finally:
        conn.close()


def main():
    """Main program execution"""
    # Get target IP with default
    target = input("Enter target IP address (default: 127.0.0.1): ") or "127.0.0.1"
    
    # Get start port with validation
    while True:
        try:
            start_port = input("Enter starting port number (1-1024): ")
            start_port = int(start_port)
            if 1 <= start_port <= 1024:
                break
            else:
                print("Port must be between 1 and 1024.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Get end port with validation
    while True:
        try:
            end_port = input("Enter ending port number (1-1024): ")
            end_port = int(end_port)
            if 1 <= end_port <= 1024:
                if end_port >= start_port:
                    break
                else:
                    print("End port must be greater than or equal to start port.")
            else:
                print("Port must be between 1 and 1024.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Create scanner and perform scan
    scanner = PortScanner(target)
    print(f"\nScanning {target} from port {start_port} to {end_port}...")
    scanner.scan_range(start_port, end_port)
    
    # Display results
    print(f"\n--- Scan Results for {target} ---")
    open_ports = scanner.get_open_ports()
    for port, status, service in open_ports:
        print(f"Port {port}: {status} ({service})")
    print("-" * 30)
    print(f"Total open ports found: {len(open_ports)}")
    
    # Save results to database
    save_results(target, scanner.scan_results)
    
    # Ask to view past scans
    view_history = input("\nWould you like to see past scan history? (yes/no): ")
    if view_history.lower() == "yes":
        load_past_scans()


if __name__ == "__main__":
    main()

# Q5: New Feature Proposal
# I would add a port risk classifier that categorizes open ports by security risk level.
# This feature would use nested if-statements to classify ports as "HIGH" risk (FTP, Telnet, SSH, RDP),
# "MEDIUM" risk (SMTP, POP3, IMAP, MySQL), or "LOW" risk (HTTP, HTTPS, DNS). The classifier would
# display a risk report after the scan, helping users identify potentially vulnerable services.
# Diagram: See diagram_101201301.png in the repository root