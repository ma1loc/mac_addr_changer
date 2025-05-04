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
# ║    Project: mac_addr_changer v1.1.1                                      ║
# ║    Created: 2025-02-23                                                   ║
# ║    Author: ma1loc(youness anflous)                                       ║
# ║                                                                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝

# main.py
from	mac_changer.parsing import user_args
from	mac_changer.options import mac_addr_option
from	mac_changer.options import check_option
from	mac_changer.parsing import is_valid_input
from	mac_changer.options import random_option
from	mac_changer.options import anonym_option
from	mac_changer.parsing import check_interface_exists

def	main():
	args = user_args()

	is_valid_input(args.interface, args.mac_addr)
	check_interface_exists(args.interface)
	if args.mac_addr:
		mac_addr_option(args)
	elif args.check:
		check_option(args.interface)
	elif args.random:
		random_option(args.interface)
	elif args.anonym:
		anonym_option(args.interface)

if __name__ == "__main__":
	main()
