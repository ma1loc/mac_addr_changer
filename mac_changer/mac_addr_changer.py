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

# command not found, to install
# random mac address, to add

from	mac_changer.parsing	import color
from	mac_changer.parsing	import check_interface_exists
from	mac_changer.parsing	import check_valid_interface
from	mac_changer.parsing	import check_misconfigured_mac
from	mac_changer.parsing	import check_if_root
import	argparse
import	subprocess
import	shutil
import	re
import	os
import	sys

# def color(text, color_code):
# 	return f"\033[{color_code}m{text}\033[0m"

# def	check_interface_exists(interface):
# 	return os.path.exists(f"/sys/class/net/{interface}")

# def	check_valid_interface(interface):
# 	return bool(re.match(r'^[a-zA-Z][a-zA-Z0-9_-]{0,14}$', interface))

# def	check_misconfigured_mac(user_mac_addr):
#     first_byte = int(user_mac_addr.split(":")[0], 16)
#     return not (first_byte & 1)

def	setup_new_addr(user_mac_addr, interface):
	try:
		subprocess.run(["ip", "link", "set", "dev", interface, "down"], check=True)
		subprocess.run(["ip", "link", "set", "dev", interface, "address", user_mac_addr], check=True)
		subprocess.run(["ip", "link", "set", "dev", interface, "up"], check=True)
	except subprocess.CalledProcessError as error:
		print(color(f"[-] Error upgrading the MAC address: {error}", "31"))
		sys.exit(1)

# def	check_if_root():
# 	if os.geteuid() != 0:
# 		print(color("[!] The script must be run as root!!!", "31"))
# 		sys.exit(1)

def	parsing_input(user_mac_addr):
	pattern = r'^([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})$'
	match = re.search(pattern, user_mac_addr)
	if match:
		return (user_mac_addr)
	else:
		return (None)

def	user_args():
	parser = argparse.ArgumentParser(description="MAC Addr changer")
	parser.add_argument("-i", "--interface", required=True, help="interface of the mac address option to upgrad its MAC address")
	parser.add_argument("-m", "--mac_addr", required=True, help="MAC addr to change the interface MAC address to new one")
	return parser.parse_args()

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
			# print(mac_match.group(1))
		else:
			print(color("[!] Could not read the MAC address.", "31"))
			sys.exit(1)
	except subprocess.CalledProcessError as e:
		print(color(f"Error: {e}", "31"))
		sys.exit(1)

def check_mac_upgraded(old_mac, new_mac):
	if old_mac != new_mac:
		print(color("[+] MAC address has been successfully changed!", "92"))

	elif old_mac == new_mac:
		print(color("[!] No change detected: the new MAC address is the same as the current one.", "33"))
	else:
		print(color("[-] MAC address couldn't be changed!", "31"))
		sys.exit(1)

def	check_command_exists():
	if shutil.which("ip") is None:
		print(color(r"[-] The command '{ip}' is not installed. Please install it before running the script."))
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
