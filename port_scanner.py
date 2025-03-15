import nmap

def scan_ports(targets):
    print(f"\nScanning {targets} for open ports...\n")

    #Initializing nmap scanner
    scanner = nmap.PortScanner()
    try:

        #Running fast scans for commonly open ports
        scanner.scan(targets , arguments = "-T4 -F")

        if not scanner.all_hosts():
            print("No host was found. Check if the targets are correct.")
            return

        #print results
        for host in scanner.all_hosts():
            print(f"\n Host: {host} ({scanner[host].hostname()})")      
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()

                if ports:
                    print(f"Open Ports: {','.join(str(port) for port in ports)}")

                else:
                    print(f"No open ports found for {host}")
    except nmap.PortScannerError:
        print(" Nmap is not installed or not accessible. Please install Nmap and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

#Example use
if __name__ == "__main__":
    targets = input("Enter your target ip or domain name:")
    scan_ports(targets)            