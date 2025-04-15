# 🖥️ MAC Address Changer


![Network Icon](https://img.icons8.com/color/48/000000/network-card.png)  
*A simple tool to change your device's MAC address*

---

## 📌 What Does This Do?

This tool lets you temporarily change the MAC address of your:
- Ethernet connections (like `eth0`)
- WiFi adapters (like `wlan0`)

⚠️ **Note:** Changes disappear after reboot!

---

## 🚀 How to Use

1. Open terminal
2. Run this command:
```bash
sudo python3 mac_addr_changer.py -i [YOUR_INTERFACE] -m [NEW_MAC]
```

```bash
# Change WiFi MAC address
sudo python3 mac_address_changer.py -i wlan0 -m 00:11:22:33:44:55

# Change Ethernet MAC address
sudo python3 mac_address_changer.py -i eth0 -m 66:77:88:99:AA:BB
```

## 💡 Quick Help

```bash
python3 mac_address_changer.py --help
```

> ⚠️ **NOTICE:** For educational research only. Use responsibly and legally.