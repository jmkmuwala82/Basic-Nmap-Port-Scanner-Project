# We need to create regular expressions to ensure that the input is correctly formatted.
import re
#Use these commands in Kali to install required software:
#  sudo apt install python3-pip
#  pip install python-nmap

# Import nmap so we can use it for the scan
import nmap

class PortScanner:

    def __init__(self):

        self.ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

        self.port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

        self.port_min = 0

        self.port_max = 65535

        self.nm = nmap.PortScanner()

         # You can scan from 0-65535 ports.
         # def get_ip_address(self):

        while True:

            ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")

            if self.ip_add_pattern.search(ip_add_entered):

                print(f"{ip_add_entered} is a valid ip address")

                return ip_add_entered



    def get_port_range(self):

        while True:

            print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")

            port_range = input("Enter port range: ")

            port_range_valid = self.port_range_pattern.search(port_range.replace(" ",""))

            if port_range_valid:

                self.port_min = int(port_range_valid.group(1))

                self.port_max = int(port_range_valid.group(2))

                return self.port_min, self.port_max



    def scan_ports(self, ip_address, port_min, port_max):

        for port in range(port_min, port_max + 1):

            try:

                result = self.nm.scan(ip_address, str(port))

                port_status = (result['scan'][ip_address]['tcp'][port]['state'])

                print(f"Port {port} is {port_status} on {ip_address}")

            except:
                # We cannot scan some ports and this ensures the program doesn't crash when we try to scanthe code

                print(f"Cannot scan port {port} on {ip_address}.")



if __name__ == '__main__':

    scanner = PortScanner()

    ip_address = scanner.get_ip_address()

    port_min, port_max = scanner.get_port_range()

    scanner.scan_ports(ip_address, port_min, port_max)
