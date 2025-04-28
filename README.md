🔍 Subnet Calculator
\n
A simple Python-based subnet calculator that computes subnet details for a given IP address and subnet mask (CIDR or dotted decimal). Perfect for network administrators, students, or anyone learning about IP networking!

📌 Features

Calculate subnet details including:
Network Address
Broadcast Address
Usable Host Range
Number of Usable Hosts
Wildcard Mask


Supports CIDR notation (e.g., /24) and dotted decimal masks (e.g., 255.255.255.0)
User-friendly command-line interface
Error handling for invalid inputs
Clean, documented code for easy learning


⚠️ Disclaimer

🚨 This tool is intended for educational and legitimate use.Ensure you understand IP addressing and subnetting before using.


💪 Requirements

Python 3.6 or higher

This script uses Python's built-in module:

ipaddress

No external libraries required.

🚀 Usage

Clone the repository:
git clone https://github.com/Mangala-Manmatharaja/Subnet-calculator.git
cd subnet-calculator


Run the script:
python subnet_calculator.py


Follow the prompts:

Enter an IP address (e.g., 192.168.1.10)
Enter a subnet mask (e.g., /24 or 255.255.255.0)


Results:

Console displays detailed subnet information
Option to calculate another subnet or exit




🧪 Example Output
Enter IP address (e.g., 192.168.1.10): 192.168.1.10
Enter subnet mask (e.g., /24 or 255.255.255.0): /24

Subnet Calculator Results:
--------------------------------------------------
IP Address: 192.168.1.10
Subnet Mask: 255.255.255.0
CIDR Notation: /24
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
Host Range: 192.168.1.1 - 192.168.1.254
Number of Usable Hosts: 254
Wildcard Mask: 0.0.0.255
--------------------------------------------------


📄 License
MIT License — feel free to use, modify, and share with credit.

✍️ Author

Mangala-Manmatharaja


🌟 Future Enhancements

Add support for subnet splitting
Create a GUI version with tkinter
Include unit tests for robustness
Develop a web-based interface

