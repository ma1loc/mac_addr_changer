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

# execution.py

from	mac_changer.parsing import color
import	subprocess
import	sys
import	os

def	check_if_root():
	if os.geteuid() != 0:
		print(color("[!] The script must be run as root!!!", "31"))
		sys.exit(1)

def	setup_new_addr(user_mac_addr, interface):
	try:
		subprocess.run(["ip", "link", "set", "dev", interface, "down"], check=True)
		subprocess.run(["ip", "link", "set", "dev", interface, "address", user_mac_addr], check=True)
		subprocess.run(["ip", "link", "set", "dev", interface, "up"], check=True)
	except subprocess.CalledProcessError as error:
		print(color(f"[-] Error upgrading the MAC address: {error}", "31"))
		sys.exit(1)
