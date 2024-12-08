# WiFi Deauth Detector

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A powerful and simple tool to detect Wi-Fi deauthentication (deauth) attacks in real-time using the Scapy library. Deauth attacks are a common form of Denial of Service (DoS) targeting Wi-Fi connections.

## Features
- Detects deauth packets in real-time.
- Displays packet count and source/destination MAC addresses.
- Simple and user-friendly interface.

## Requirements
- Python 3.x
- [Scapy](https://scapy.net) library
- Root privileges to sniff network packets.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/[YourUsername]/WiFi-Deauth-Detector.git
2. Navigate to the directory:
   ```bash
   cd WiFi-Deauth-Detector

3. Install dependencies:
      ```bash
    pip install scapy

Usage

Set your network interface to monitor mode:

   ```bash
sudo ifconfig wlan0 down
sudo iwconfig wlan0 mode monitor
sudo ifconfig wlan0 up
 ```
Replace wlan0 with your network interface name.

Run the script:
 ```
    sudo python3 deauth_detector.py
 ```
Enter your network interface when prompted.

Example Output
 ```
Enter your Network Interface (e.g., wlan0): wlan0
[*] Starting deauth detection on interface: wlan0
[+] Deauth Packet #1 Detected!
    Source: 00:14:22:01:23:45 -> Destination: FF:FF:FF:FF:FF:FF
[+] Deauth Packet #2 Detected!
    Source: 00:14:22:01:23:45 -> Destination: 01:23:45:67:89:AB
 ```
