#!/usr/bin/python3

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                                                                          ║
# ║             ███╗   ███╗ █████╗  ██╗██╗      ██████╗  ██████╗             ║
# ║             ████╗ ████║██╔══██╗███║██║     ██╔═══██╗██╔════╝             ║
# ║             ██╔████╔██║███████║╚██║██║     ██║   ██║██║                  ║
# ║             ██║╚██╔╝██║██╔══██║ ██║██║     ██║   ██║██║                  ║
# ║             ██║ ╚═╝ ██║██║  ██║ ██║███████╗╚██████╔╝╚██████╗             ║
# ║             ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═╝╚══════╝ ╚═════╝  ╚═════╝             ║
# ║                                                                          ║
# ║    Project: mac_addr_changer                                             ║
# ║    Created: 2025-02-23                                                   ║
# ║    Author: ma1loc (youness anflous)                                      ║
# ║                                                                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import	argparse
import	subprocess
import	re
import	os
import	sys

def color(text, color_code):
	return f"\033[{color_code}m{text}\033[0m"

def	setup_new_addr(user_mac_addr, interface):
	try:
		subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "down"], check=True)
		subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "address", user_mac_addr], check=True)
		subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "up"], check=True)
		print(color("[+] MAC address is changed succassfully", "92"))
	except subprocess.CalledProcessError as error:
		print(color(f"[!] Error changing MAC address: {error}", "31"))
		sys.exit(1)

def	check_if_root():
	if os.geteuid() != 0:
		print(color("The script must be run as root!!!", "31"))
		sys.exit(1)

def	parsing_input(user_mac_addr):
	pattern = r'^([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})$'
	match = re.search(pattern, user_mac_addr)
	if match:
		return (user_mac_addr)
	else:
		return (None)

def	user_args():
	parser = argparse.ArgumentParser(description="MAC Addr changer")
	parser.add_argument("-i", "--interface", required=True, help="interface of the mac address option to change its MAC address")
	parser.add_argument("-m", "--mac_addr", required=True, help="MAC addr to change the interface MAC address to new one")
	return parser.parse_args()

def	main():
	check_if_root()
	args = user_args()
	if parsing_input(args.mac_addr):
		setup_new_addr(args.mac_addr, args.interface)
	else:
		print(color("MAC address structure error.", "31"))
		sys.exit(1)

if __name__ == "__main__":
	main()
