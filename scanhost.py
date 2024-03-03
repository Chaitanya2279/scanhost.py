import socket # we import the socket module to create connections to send and receive data over the network
import sys # we import sys module for system-specific functions

# Function to check if a string represents a valid integer
import re


def valid_starting_port(value):

        if value.isnumeric(): # checks if the string only contains numeric value
            value = int(value) # converts string to integer

            if 0 <= value <= 1000: # checks if the input value lies between 0-1000
                return value

            else: # else gives an appropriate error message for range
                print("Invalid port doesn't lie between 0-1000. Please enter a valid port between 0 and 1000.")
                return False

        else: # else gives an appropriate error message for incorrect input type
            print("Input type is incorrect. Please enter a valid integer port between 0 and 1000.")
            return False

def valid_ending_port(starting_port, ending_port):

        if ending_port.isnumeric(): # checks if the string only contains numeric value
            ending_port = int(ending_port) # converts string to integer for ending port
            starting_port = int(starting_port) # converts string to integer for starting port

            if starting_port <= ending_port <= 1000: # checks if the input value lies between 0-1000
                return ending_port

            else: # else gives an appropriate error message for range
                print("Invalid port doesn't lie between 0-1000. Please enter a valid port between 0 and 1000.")
                return False

        else:  # else gives an appropriate error message for incorrect input type
            print(f"Input type is incorrect. Please enter a valid integer port between {starting_port} and 1000.")
            return False


# Function to check if a string represents a valid domain name
def valid_domain(domain):
    try:
        pattern = r'^[a-zA-Z0-9.-]+$'
        if bool(re.match(pattern, domain)):

            socket.gethostbyname(domain) # resolves hostname to ip address
            return True
        else:
            print("Invalid input! Your input should include alphanumeric or '.' or '-' ")
            return False

    except socket.error:
        print("Invalid domain name. Please enter a valid domain.")
        return False

# Function to print port status with colors
def print_port_status(domain, port, status):
    color = '\033[92m' if status == 'open' else '\033[91m'
    print(f"{domain} Port {port}: {color}{status}\033[0m")

def main():
    # Check if query parameters are passed
    # sys.argv contains a list of our command line input arguments
    # sys.argv[0] - contains the name of the file we are running
    # sys.argv[1] - contains the query argument passed by the user

    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', '--version']:
        if sys.argv[1] in [ '-h', '--help']:


            print(""" Usage:
  python scanhost.py [-h] [--help] [--version]

Description:
  This tool analyzes which ports are open/closed for a particular domain.

Options:
  -h, --help      Show this help message and exit.
  --version  Show version information.

Instructions for Domain:
- Enter a domain name which is alphanumeric and may include special characters like dot (.) and hyphen (-).
- The domain name should match the pattern [a-zA-Z0-9].
- The domain name will be validated for its correctness.

Instructions for Starting Port Number:
- Enter a starting port number between 0 and 1000.
- The starting port number should be an integer.
- It will be validated to ensure it lies within the valid range.

Instructions for Ending Port Number:
- Enter an ending port number between the starting port and 1000.
- The ending port number should be an integer.
- It will be validated to ensure it lies within the valid range.

Port Status:
- Open ports will be displayed as "Port [port_number]: open".
- Closed ports will be displayed as "Port [port_number]: closed".

Port Number Instructions:
- Port numbers should be integers.
- Port numbers should be in the range of 0-1000.

Example:
python scanhost.py
Enter your domain: www.rit.edu
Enter a starting port between 0 and 1000: 79
Enter an ending port between 79 and 1000: 80

www.rit.edu Port 79: closed
www.rit.edu Port 80: open""")


        elif sys.argv[1] in ['--version']:
            print("""scanhost.py 1.0

This script scans ports of a given domain to check their status.

Author: Advika Sunil, Sai Chaitanya Kumar, Vijay Baskar
Date: 03-03-24

Dependencies:
- Python 3.x

For more information or to report issues, visit [https://github.com/Chaitanya2279/scanhost.py.git]. """)

    sys.exit()



    # Interactive script
    print("This script scans ports of a target domain provided by the user and tells you if those ports are open or close.")


# input for domain
    domain = input("Enter your domain: ")
    while not valid_domain(domain):
        domain = input("Enter your domain: ")

# input for starting port
    starting_port = input("\nEnter a starting port between 0 and 1000: ")
    while not valid_starting_port(starting_port):

        starting_port = input("\nEnter a starting port between 0 and 1000: ")

#input for ending port
    ending_port = input("\nEnter an ending port between "+starting_port +" and 1000: ")
    while not valid_ending_port(starting_port, ending_port):
        ending_port = input(f"\nEnter an ending port between {starting_port} and 1000: ")

    # Scaning ports
    print(f"\nScanning ports {starting_port} - {ending_port} of {domain}...") # printing port scan

    for port in range (int(starting_port), int(ending_port) + 1): # iterating from start port to end port
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

                sock.settimeout(0.5)  # Set timeout to 0.5 seconds

                connection_output = sock.connect_ex((domain, port)) # connects domain and port together.. returns 0 if the connection is sucessfuly established

                if connection_output == 0:
                    print_port_status(domain, port, 'open')

                else:
                    print_port_status(domain, port, 'closed')

        except socket.error:
            print_port_status(domain, port, 'filtered')

if __name__ == "__main__":
    main()
