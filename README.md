# PySharkAnalyzer


This project analyse and live capture your Network interface controller and save some datas in a CSV.


## Index

1 - [Pre-requirement](#pre-requirement)

2 - [Configuration](#configuration)


## Pre-requirement

The firts thing to do is install the pre-requirement : wireshark, tshark, pyshark and pandas

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

### Linux

+ If you are on Linux , you need to change the Network interface controller(NIC). For see the NIC names tables on terminal , use the command :

```bash
tshark -D
```
















