import socket
import sys

# Function to check if a string represents a valid integer
def is_valid_integer(value):
    try:
        int_value = int(value)
        return 0 <= int_value <= 1000
    except ValueError:
        return False

# Function to check if a string represents a valid domain name
def is_valid_domain(domain):
    try:
        socket.gethostbyname(domain)
        return True
    except socket.error:
        return False

# Function to print port status with colors
def print_port_status(domain, port, status):
    color = '\033[92m' if status == 'open' else '\033[91m'
    print(f"{domain} Port {port}: {color}{status}\033[0m")

def main():
    # Check if query parameters are passed
    if len(sys.argv) > 1 and sys.argv[1] in ['/?', '-h', '--help', '--version']:
        print("Usage: python scanhost.py")
        print("This script scans ports of a target domain interactively.")
        sys.exit()

    # Interactive mode
    print("This script scans ports of a target domain interactively.")
    domain = input("Enter your domain: ")
    while not is_valid_domain(domain):
        print("Invalid domain. Please enter a valid domain.")
        domain = input("Enter your domain: ")

    start_port = input("Enter a starting port between 0 and 1000: ")
    while not is_valid_integer(start_port) or not (0 <= int(start_port) <= 1000):
        print("Invalid port. Please enter a valid starting port between 0 and 1000.")
        start_port = input("Enter a starting port between 0 and 1000: ")

    end_port = input(f"Enter an ending port between {start_port} and 1000: ")
    while not is_valid_integer(end_port) or not (int(start_port) <= int(end_port) <= 1000):
        print(f"Invalid port. Please enter a valid ending port between {start_port} and 1000.")
        end_port = input(f"Enter an ending port between {start_port} and 1000: ")

    # Scan ports
    print(f"\nScanning ports for {domain}...")
    for port in range(int(start_port), int(end_port) + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)  # Set timeout to 0.5 seconds
                result = s.connect_ex((domain, port))
                if result == 0:
                    print_port_status(domain, port, 'open')
                else:
                    print_port_status(domain, port, 'closed')
        except socket.error:
            print_port_status(domain, port, 'filtered')

if _name_ == "_main_":
    main()
