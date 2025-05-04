# ![Network Icon](https://img.icons8.com/color/48/000000/network-card.png) MAC Address Changer


**A simple tool allows you to change your device's network interface's MAC address (the physical address assigned to your network adapter).**


## 📌 What Does This Tool Do?

This tool lets you temporarily change the MAC address of your:
- Ethernet connections (like `eth0`)
- WiFi adapters (like `wlan0`)

⚠️ **Note:** Changes disappear after reboot!


## 🚀 How to Use

1. Open terminal
2. clone the repository
```bash
git clone https://github.com/ma1loc/mac_addr_changer.git
```
3. go to the mac_addr_changer folder
```bash
cd mac_addr_changer
```
4. Run this command and make sure your ROOT
```bash
sudo python3 setup.py -i [YOUR_INTERFACE] -m [NEW_MAC]
```

```bash
# Change WiFi MAC address
sudo python3 setup.py -i wlan0 -m 00:11:22:33:44:55

# Change Ethernet MAC address
sudo python3 setup.py -i eth0 -m 66:77:88:99:AA:BB
```

## 💡 Quick help about the tool options

```bash
sudo python3 setup.py --help
```

##  Additional Options
- --check option to check the current interface MAC address
```bash
sudo python3 setup.py -i [your_interface] --check
```
- --random option gives you a random MAC addresses
```bash
sudo python3 setup.py -i [your_interface] --random
```
- --anonym option change the MAC address every 600s -> 10min
```bash
sudo python3 setup.py -i [your_interface] --anonym
```


> ⚠️ **NOTICE:** For educational research only. Use responsibly and legally.
