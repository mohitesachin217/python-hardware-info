import psutil
import socket

def list_network_cards():
    network_cards = psutil.net_if_addrs()
    
    for card, addresses in network_cards.items():
        print(f"Network Card: {card}")
        
        for address in addresses:
            if address.family == socket.AF_INET:
                print(f"  IPv4 Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif address.family == socket.AF_INET6:
                print(f"  IPv6 Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
            elif address.family == psutil.AF_LINK:
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
                
        print("=" * 40)

if __name__ == "__main__":
    list_network_cards()
