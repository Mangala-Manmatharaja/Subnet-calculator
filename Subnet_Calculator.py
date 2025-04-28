import ipaddress


def calculate_subnet(ip_address: str, subnet_mask: str) -> dict:

    try:
        # Handle CIDR notation or dotted decimal subnet mask
        if subnet_mask.startswith('/'):
            network = ipaddress.ip_network(f"{ip_address}{subnet_mask}", strict=False)
        else:
            network = ipaddress.ip_network(f"{ip_address}/{subnet_mask}", strict=False)

        # Calculate subnet details
        network_address = str(network.network_address)
        broadcast_address = str(network.broadcast_address)
        num_hosts = network.num_addresses - 2  # Exclude network and broadcast addresses
        host_min = str(list(network.hosts())[0]) if num_hosts > 0 else network_address
        host_max = str(list(network.hosts())[-1]) if num_hosts > 0 else broadcast_address

        return {
            "IP Address": ip_address,
            "Subnet Mask": str(network.netmask),
            "CIDR Notation": f"/{network.prefixlen}",
            "Network Address": network_address,
            "Broadcast Address": broadcast_address,
            "Host Range": f"{host_min} - {host_max}" if num_hosts > 0 else "N/A",
            "Number of Usable Hosts": num_hosts,
            "Wildcard Mask": str(network.hostmask)
        }

    except ValueError as e:
        return {"error": f"Invalid IP address or subnet mask: {e}"}


def display_subnet_details(subnet_info: dict):
    """
    Display subnet details in a formatted manner.

    Args:
        subnet_info (dict): Dictionary containing subnet details
    """
    if "error" in subnet_info:
        print(subnet_info["error"])
        return

    print("\nSubnet Calculator Results:")
    print("-" * 50)
    for key, value in subnet_info.items():
        print(f"{key}: {value}")
    print("-" * 50)


def main():
    """
    Main function to run the subnet calculator with user input.
    """
    print("#######---Welcome to the Subnet Calculator! ---#######")

    while True:
        ip_address = input("\n>>> Enter IP address (e.g., 192.168.1.10): ").strip()
        subnet_mask = input(">>> Enter subnet mask (e.g., /24 or 255.255.255.0): ").strip()

        subnet_info = calculate_subnet(ip_address, subnet_mask)
        display_subnet_details(subnet_info)

        choice = input("\n>>> Calculate another subnet? (y/n): ").strip().lower()
        if choice != 'y':
            print("*----* Thank you for using the Subnet Calculator! *----*")
            break


if __name__ == "__main__":
    main()