# PySharkAnalyzer


This project analyse and live capture your Network interface controller and save some datas in a CSV.


## Index

1 - [Pre-requirement](#pre-requirement)

2 - [Configuration](#configuration)


## Pre-requirement

The first thing to do is install the pre-requirement : wireshark, tshark, pyshark and pandas

### Windows 
  On windows, you need to install some application and some python libraries
  + [wireshark](https://www.wireshark.org/download.html)
  ```python
  pip install pyshark
  ```
  ```python
  pip install pandas
  ```
### Linux
On Linux, you need to install the wireshark ,and the tshark and some python libraries.
+ [wireshark](https://www.wireshark.org/download.html)
```bash
sudo apt install tshark
```
  ```python
  pip install pyshark
  ```
  ```python
  pip install pandas
  ```



## Configuration
 
### Windows

+ If you are on window s, you need to change the Network interface controller(NIC). For see the NIC names tables on cmd , use the command :

```bash
 wmic nic get name
```
The return will be something like this
```bash
Name
Microsoft Kernel Debug Network Adapter
Qualcomm QCA61x4A 802.11ac Wireless Adapter
Killer E2400 Gigabit Ethernet Controller
Bluetooth Device (Personal Area Network)
Microsoft Wi-Fi Direct Virtual Adapter
Microsoft Wi-Fi Direct Virtual Adapter #2
WAN Miniport (SSTP)
WAN Miniport (IKEv2)
WAN Miniport (L2TP)
WAN Miniport (PPTP)
WAN Miniport (PPPOE)
WAN Miniport (IP)
WAN Miniport (IPv6)
WAN Miniport (Network Monitor)
VirtualBox Host-Only Ethernet Adapter
RAS Async Adapter
```
### Linux

+ If you are on Linux , you need to change the Network interface controller(NIC). For see the NIC names tables on terminal , use the command :

```bash
tshark -D
```
```bash
1. enp0s3
2. any
3. lo (Loopback)
4. bluetooth-monitor
5. nflog
6. nfqueue
7. dbus-system
8. dbus-session
9. ciscodump (Cisco remote capture)
10. dpauxmon (DisplayPort AUX channel monitor capture)
11. randpkt (Random packet generator)
12. sdjournal (systemd Journal Export)
13. sshdump (SSH remote capture)
14. udpdump (UDP Listener remote capture)
```


---














