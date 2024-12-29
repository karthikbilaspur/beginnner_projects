import socket
import threading
import argparse
import json
import os
import datetime

class PortScanner:
    def __init__(self, target, min_port, max_port):
        self.target = target
        self.min_port = min_port
        self.max_port = max_port
        self.open_ports = []
        self.ports_info = {}
        self.scan_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def scan_port(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((self.target, port))
            self.open_ports.append(port)
            self.ports_info[port] = {"status": "Open", "service": self.get_service(port)}
            print(f"Port {port} is open ({self.ports_info[port]['service']})")
        except socket.error:
            self.ports_info[port] = {"status": "Closed", "service": ""}
        finally:
            sock.close()

    def get_service(self, port):
        try:
            return socket.getservbyport(port)
        except OSError:
            return "Unknown"

    def scan(self):
        threads = []

        for port in range(self.min_port, self.max_port + 1):
            thread = threading.Thread(target=self.scan_port, args=(port,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def save_results(self):
        results = {
            "target": self.target,
            "scan_time": self.scan_time,
            "ports": self.ports_info
        }
        with open(f"{self.target}_scan_results_{self.scan_time}.json", "w") as f:
            json.dump(results, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or hostname")
    parser.add_argument("-p", "--ports", required=True, help="Port range (e.g., 1-1024)")
    parser.add_argument("-s", "--save", action="store_true", help="Save results to file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase verbosity")
    args = parser.parse_args()

    min_port, max_port = map(int, args.ports.split("-"))
    scanner = PortScanner(args.target, min_port, max_port)
    
    if args.verbose:
        print(f"Scanning {args.target} from port {min_port} to {max_port}...")
    
    scanner.scan()

    print(f"\nOpen ports on {args.target}: {scanner.open_ports}")
    if args.save:
        scanner.save_results()
        print(f"Results saved to {args.target}_scan_results_{scanner.scan_time}.json")

if __name__ == "__main__":
    main()
    