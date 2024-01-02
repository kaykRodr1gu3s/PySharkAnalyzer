# PySharkAnalyzer


This project analyse and live capture your Network interface controller and save some datas in a CSV.


## Index

1 - [Requirements](#requirements)

2 - [Configuration](#configuration)

3 - [Live capture](#live-capture)

4 - [File capture](#file-capture)

5 - [Usage](#usage)

6 - [Contact](#contact)
## Requirements

The first thing to do is install the requirements : wireshark, tshark, pyshark and pandas

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

If you want to capture outher interface, open the wireshark application. You will see something like this:

![339862_340003_common_13130_01](https://github.com/kaykRodr1gu3s/PySharkAnalyzer/assets/110197812/253e771d-5c3f-4a9a-b6d2-efc83b4131a7)


in the example below, i will put the wi-fi interface:
```python
self.live = self.live_capture_pcap('Wi-fi')
```

i change the ```self.live = self.live_capture_pcap('Adapter for loopback traffic capture')``` to ```self.live = self.live_capture_pcap('Wi-fi')```

#### Windows

  In windows code you must execute your IDE as administrator, i left the Adapter for loopback traffic capture  interface . You can change the interface, for you see an example go to [USAGE](#usage)
 

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

You can change the pcap that will be generated, just change this code line:

```python
  self.pcap_name = "Pcap_Name.pcap"
```
In both code it's possible to change. On linux code the code line will be ```self.pcap_name = "Linux.pcap"``` and the windows will be ```self.pcap_name = "Windows.pcap"```

For the code work very well, on the [Live capture](https://github.com/kaykRodr1gu3s/PySharkAnalyzer/tree/main/Live%20capture) you just need to configure the interface , read the [Live capture configuration](#live-capture). 

It is possible you change the CSV name that will be generated just change the code
```python 
df.to_csv('My_pcap.csv', index=False)
```
The csv name is the ```My_pcap.csv```. If you want outher name, just eraise the 'My_pcap.pcap' put your name and run the code.

You can capture outher interface outher like the Wi-fi, you can see all the interface on wireshark interface.



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
 1. Fork the repository.
 2. Create a branch for your contribution: `git checkout -b feature-nova`.
 3. Make the desired changes and commit: `git commit -m "Add new functionality"`.
 4. Push to your branch: `git push origin new-feature`.
 5. Open a pull request.



## Contact

- Linkedin: [Kayk Rodrigues](https://www.linkedin.com/in/kayk-rodrigues-504a03273)
- Telegram: [Kayk Rodrigues](https://t.me/kaykRodrigues)
