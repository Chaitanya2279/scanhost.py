Usage: python scanhost.py

This tool lets you analyze which ports are open/closed for a particular domain.

Instructions for Domain:
- Enter a domain name which is alphanumeric and may include special characters like dot (.) and hyphen (-).
- The domain name should match the pattern [a-zA-Z0-9].
- The domain name will be validated to be a real domain.

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

Example:
python scanhost.py
Enter your domain: www.rit.edu
Enter a starting port between 0 and 1000: 79
Enter an ending port between 79 and 1000: 80

www.rit.edu Port 79: closed
www.rit.edu Port 80: open
