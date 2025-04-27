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

# checker.py
# Contains functions to validate interfaces and MAC address format && stuff

import	argparse
import	shutil
import	sys
import	os
import	re


def	user_args():
	parser = argparse.ArgumentParser(description="MAC Addr changer")
	parser.add_argument("-i", "--interface", required=True, help="Interface of the mac address option to upgrad its MAC address")
	parser.add_argument("-m", "--mac_addr", help="MAC addr to change the interface MAC address to new one")
	# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	parser.add_argument("--random", action="store_true", help="nothing yet!")
	parser.add_argument("--check", action="store_true")
	parser.add_argument("--anonym", action="store_true")
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

def	parsing_input(user_mac_addr):
	pattern = r'^([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})$'
	match = re.search(pattern, user_mac_addr)
	if match:
		return (user_mac_addr)
	else:
		return (None)

def color(text, color_code):
	return f"\033[{color_code}m{text}\033[0m"

def check_interface_exists(interface):
    return os.path.exists(f"/sys/class/net/{interface}")

def check_mac_format(mac):
    pattern = r"^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$"
    return re.match(pattern, mac) is not None

def	check_interface_exists(interface):
	return os.path.exists(f"/sys/class/net/{interface}")

def	check_valid_interface(interface):
	return bool(re.match(r'^[a-zA-Z][a-zA-Z0-9_-]{0,14}$', interface))

def	check_misconfigured_mac(user_mac_addr):
    first_byte = int(user_mac_addr.split(":")[0], 16)
    return not (first_byte & 1)

def	check_command_exists():
	if shutil.which("ip") is None:
		print(color(r"[-] The command '{ip}' is not installed. Please install it before running the script."))
		sys.exit(1)

def check_mac_upgraded(old_mac, new_mac):
	if old_mac != new_mac:
		print(color("[+] MAC address has been successfully changed!", "92"))
	elif old_mac == new_mac:
		print(color("[!] No change detected: the new MAC address is the same as the current one.", "33"))
	else:
		print(color("[-] MAC address couldn't be changed!", "31"))
		sys.exit(1)
