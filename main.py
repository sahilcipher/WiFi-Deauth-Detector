#!/usr/bin/env python3

# WiFi Deauthentication Attack Detector - Version 1.1
# Developed by Parmar Sahil
# GitHub: https://github.com/[YourUsername]/WiFi-Deauth-Detector

"""
WiFi Deauth Detector Tool
-------------------------
This tool helps detect Wi-Fi deauthentication (deauth) attacks by analyzing network traffic.
A deauth attack is a form of Denial of Service (DoS) targeting Wi-Fi connections.

Features:
- Detects deauth frames in real-time.
- Tracks the number of detected packets.
- Outputs details like source and destination MAC addresses.
"""

from scapy.all import *
from scapy.layers.dot11 import Dot11

# Function to extract and display information from deauthentication packets
def detect_deauth(packet):
    if packet.haslayer(Dot11):
        if packet.type == 0 and packet.subtype == 12:  # Management frame, subtype 12 is deauth
            global packet_counter
            packet_counter += 1
            source = packet.addr2 or "Unknown"
            dest = packet.addr1 or "Unknown"
            print(f"[+] Deauth Packet #{packet_counter} Detected!")
            print(f"    Source: {source} -> Destination: {dest}")

# Prompt user for network interface
if __name__ == "__main__":
    try:
        interface = input("Enter your Network Interface (e.g., wlan0): ").strip()
        packet_counter = 0  # Initialize packet counter
        print(f"[*] Starting deauth detection on interface: {interface}")
        sniff(iface=interface, prn=detect_deauth)
    except KeyboardInterrupt:
        print("\n[!] Detection stopped by user.")
    except Exception as e:
        print(f"[!] Error: {e}")
