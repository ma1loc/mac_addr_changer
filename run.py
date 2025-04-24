#!/usr/bin/env python3

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                                                                          ║
# ║             ███╗   ███╗ █████╗  ██╗██╗      ██████╗  ██████╗             ║
# ║             ████╗ ████║██╔══██╗███║██║     ██╔═══██╗██╔════╝             ║
# ║             ██╔████╔██║███████║╚██║██║     ██║   ██║██║                  ║
# ║             ██║╚██╔╝██║██╔══██║ ██║██║     ██║   ██║██║                  ║
# ║             ██║ ╚═╝ ██║██║  ██║ ██║███████╗╚██████╔╝╚██████╗             ║
# ║             ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═╝╚══════╝ ╚═════╝  ╚═════╝             ║
# ║                                                                          ║
# ║    Project: mac_addr_changer v1.1.0                                      ║
# ║    Created: 2025-02-23                                                   ║
# ║    Author: ma1loc (youness anflous)                                      ║
# ║                                                                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝

# random mac address, to add

from	mac_changer.parsing import user_args
from	mac_changer.parsing import parsing_input
from	mac_changer.parsing	import check_interface_exists
from	mac_changer.parsing	import check_valid_interface
from	mac_changer.parsing	import check_misconfigured_mac
from	mac_changer.execution import check_if_root
from	mac_changer.parsing import check_mac_upgraded
from	mac_changer.execution import setup_new_addr
from	mac_changer.parsing	import color
import	argparse
import	subprocess
import	re
import	sys

def	is_valid_input(interface, mac_addr):
	if not check_valid_interface(interface):
		print(color(f"[-] Invalid interface name.", "31"))
		sys.exit(1)

	if not check_interface_exists(interface):
		print(color(f"[-] Interface {interface} not exists.", "31"))
		sys.exit(1)

	if not check_misconfigured_mac(mac_addr):
		print(color("[!] Invalid MAC address -> (must be unicast).", "31"))
		sys.exit(1)

def get_current_mac(interface):
	try:
		config_output = subprocess.check_output(["ip", "link", "show", interface]).decode()
		mac_match = re.search(r"link/ether\s+([0-9a-fA-F:]{17})", config_output)
		if mac_match:
			return (mac_match.group(1))
		else:
			print(color("[!] Could not read the MAC address.", "31"))
			sys.exit(1)
	except subprocess.CalledProcessError as e:
		print(color(f"Error: {e}", "31"))
		sys.exit(1)

def	main():
	check_if_root()
	args = user_args()
	is_valid_input(args.interface, args.mac_addr)

	old_mac = get_current_mac(args.interface)
	if parsing_input(args.mac_addr):
		setup_new_addr(args.mac_addr, args.interface)
	else:
		print(color(f"[-] MAC address {args.mac_addr} structure error.", "31"))
		sys.exit(1)
	new_mac = get_current_mac(args.interface)
	check_mac_upgraded(old_mac, new_mac)

if __name__ == "__main__":
	main()
