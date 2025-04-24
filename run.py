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

from	mac_changer.parsing import user_args
from	mac_changer.parsing import parsing_input
from	mac_changer.parsing import is_valid_input
from	mac_changer.parsing import check_mac_upgraded
from	mac_changer.parsing	import color
from	mac_changer.execution import check_if_root
from	mac_changer.execution import setup_new_addr
from	mac_changer.execution import get_current_mac
import	sys


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
