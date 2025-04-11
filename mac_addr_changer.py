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

import	subprocess
import	re

# define a function first to take input and parsing the input
# use the subprocess to execute the commands
# befor that i have to check if the user is in sudo
# sudo ip link set dev <interface> down
# sudo ip link set dev <interface> address <new_mac>
# sudo ip link set dev <interface> up
# add a help page to be user firendly
# def	is_sudo():


def	setup_new_addr(user_mac_addr, interface):
	subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "down"])
	subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "address", user_mac_addr])
	subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "up"])


def	parsing_input(user_mac_addr):
	pattern = r'^([0-9a-fA-F]{2}[:-]){5}(/[0-9a-fA-F]{2})$'
	match = re.search(pattern, user_mac_addr)
	if match:
		return (user_mac_addr)
	else:
		return (None)


def	user_input():
	user_mac_addr = input(">>> Mac Addr: ")
	user_interface = input(">>> Interface: ")
	valid = parsing_input(user_mac_addr)
	if valid:
		setup_new_addr(user_mac_addr, user_interface)
	else:
		return (None)
	return (True)

def	main():
	result = user_input()
	if (result):
		print("MAC Address updated Seccussfully.")


if __name__ == "__main__":
	main()
