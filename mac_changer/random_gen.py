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

# random_gen.py

import random

def gen_random_hex():
    return random.choice('0123456789abcdef')

def get_first_byte():
    return random.randint(0x00, 0xff) & 0xFE

def converte_to_hex():
    first_byte = format(get_first_byte(), '02x')
    return (first_byte)

def get_random_mac():
    first_byte = converte_to_hex()
    second_part = [''.join(gen_random_hex() for _ in range(2)) for _ in range(5)]
    mac_parts = [first_byte] + second_part
    full_mac_addr = ':'.join(mac_parts)
    return (full_mac_addr)
