# PySharkAnalyzer


This project analyse and live capture your Network interface controller and save some datas in a CSV.


## Index

1 - [Pre-requirement](#pre-requirement)

2 - [Configuration](#configuration)

3 - [Live capture](#live-capture)

4 - [File capture](#file-capture)

5 - [Usage](#usage)
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

### Live capture

#### Windows
 
+ If you are on windows, you need to change the Network interface controller(NIC). For see the NIC names tables on cmd , use the command :

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
#### Linux

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


Put your NIC on the code. For example , i put the enp0s3, you just need to put your!
```python
self.live = self.live_capture_pcap('enp0s3')
``` 

---

### File capture 

If you want to read a pcap is easier than taking live capture.

You can analysis outher pcap, You just need to put the pcap file on same code directory, and change the name on the code.
The code line is the
```python
self.pyshark_obj = pyshark.FileCapture(f'./2023-12-15-TA577-Pikabot-infection-traffic.pcap')
```
For example , i left the pcap 2023-12-15-TA577-Pikabot-infection-traffic.pcap, if you want to download the pcap, [click here](https://www.malware-traffic-analysis.net/2023/12/18/index.html).


## Usage
### Live capture
For the code work, on the [Live capture](https://github.com/kaykRodr1gu3s/PySharkAnalyzer/tree/main/Live%20capture) you just need to configure the NIC , read the [Live capture configuration](#live-capture). Is possible you change the CSV name that will be generated just change the code
```python 
df.to_csv('My_pcap.csv', index=False)
```
The csv name is the ```My_pcap.csv```. If you want outher name, just eraise the 'My_pcap.pcap' put your name and run the code.

### File capture

The code [File capture](https://github.com/kaykRodr1gu3s/PySharkAnalyzer/tree/main/File%20capture), it's possible to change the pcap file and csv name. For change the pcap file just put the pcap on the same directory and change the pcap file name  on the code
```python
self.pyshark_obj = pyshark.FileCapture(f'./2023-12-15-TA577-Pikabot-infection-traffic.pcap')
```
The pcap name that i use as example is ```2023-12-15-TA577-Pikabot-infection-traffic.pcap``` , put your pcap name that are on the directory.

For change the csv name, change the string name
```python
df.to_csv('2023-12-15-TA577-Pikabot-infection-traffic.csv', index=False)
```
In this example, i use the the ```2023-12-15-TA577-Pikabot-infection-traffic.csv``` as example, just eraise and put your csv name




## how to contribute
 + Clone the repository
 + Try to upgrade the code
 + Make the pull request



## Contact


+ Linkedin : https://www.linkedin.com/in/kayk-rodrigues-504a03273
+ Telegram : 
