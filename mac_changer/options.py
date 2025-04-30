# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                                                                          ║
# ║             ███╗   ███╗ █████╗  ██╗██╗      ██████╗  ██████╗             ║
# ║             ████╗ ████║██╔══██╗███║██║     ██╔═══██╗██╔════╝             ║
# ║             ██╔████╔██║███████║╚██║██║     ██║   ██║██║                  ║
# ║             ██║╚██╔╝██║██╔══██║ ██║██║     ██║   ██║██║                  ║
# ║             ██║ ╚═╝ ██║██║  ██║ ██║███████╗╚██████╔╝╚██████╗             ║
# ║             ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═╝╚══════╝ ╚═════╝  ╚═════╝             ║
# ║                                                                          ║
# ║    Project: mac_addr_changer v1.1.1                                      ║
# ║    Created: 2025-02-23                                                   ║
# ║    Author: ma1loc(youness anflous)                                       ║
# ║                                                                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝

# options.py
# Contains options function like: --mac_addr, --check, --random, --anonym

from	mac_changer.parsing	import color
from	mac_changer.parsing import parsing_input
from	mac_changer.parsing import check_mac_upgraded
from	mac_changer.execution import check_if_root
from	mac_changer.execution import setup_new_addr
from	mac_changer.execution import get_current_mac
from	mac_changer.random_gen import get_random_mac
import	time
import	sys

# --mac_addr option
def	mac_addr_option(args):
	check_if_root()
	old_mac = get_current_mac(args.interface)
	if parsing_input(args.mac_addr):
		setup_new_addr(args.mac_addr, args.interface)
	else:
		print(color(f"[-] MAC address {args.mac_addr} structure error.", "31"))
		sys.exit(1)
	new_mac = get_current_mac(args.interface)
	check_mac_upgraded(old_mac, new_mac, args.interface)

# --check option
def	check_option(interface):
	own_mac = get_current_mac(interface)
	print(color(f"[+] Your current MAC address -> \"{own_mac}\" on the \"{interface}\" interface", "92"))

# --random option
def	random_option(interface):
	check_if_root()
	old_mac = get_current_mac(interface)
	get_new_mac =  get_random_mac()
	if (get_new_mac):
		setup_new_addr(get_new_mac, interface)
	new_mac = get_current_mac(interface)
	check_mac_upgraded(old_mac, new_mac, interface)

# --anonym
def	anonym_option(interface):
	try:
		while True:
			random_option(interface)
			time.sleep(1)
	except KeyboardInterrupt:
		sys.exit(130)
