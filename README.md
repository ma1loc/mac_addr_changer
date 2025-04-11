## MAC Address
### What's the MAC Address?
A Media Access Control (MAC) address is a unique identifier assigned to the network interface card (NIC) of a device, allowing it to be recognized on a local network. Operating at the Data Link Layer (Layer 2) of the OSI model, the MAC address is crucial for communication within a local network segment, ensuring that data reaches the correct physical device. Each MAC address is 48 bits long and is typically represented in hexadecimal format, appearing as six pairs of hexadecimal digits separated by colons or hyphens—for example, 00:1A:2B:3C:4D:5E. The uniqueness of a MAC address comes from its structure: the first 24 bits represent the Organizationally Unique Identifier (OUI) assigned to the manufacturer, while the remaining 24 bits are specific to the individual device. This design ensures that every MAC address is globally unique, allowing devices worldwide to communicate without address conflicts.

but it can not be change, is it realy? 
yes ,but naaah why?
the MAC is a physical address that mean's can not be chagne be you can chage it as a softwear
you can see it is chage but in the hardwear part is not chage
help usage
python3 Mac_changer.py --help -> help you to the usage of the tool
-i or --interface -> interface of the NIC to chage its MAC Address
-m or --new_mac -> New MAC of your choise to assign it to the interface
example of the usage -> python3 script.py -i eth0 -m 00:11:22:33:44:55
