import wmi

def get_chipset_info():
    c = wmi.WMI()
    for item in c.Win32_BaseBoard():
        print("Chipset Information:")
        print(f"  Manufacturer: {item.Manufacturer}")
        print(f"  Product: {item.Product}")
        print(f"  Version: {item.Version}")
        print(f"  Serial Number: {item.SerialNumber}")

if __name__ == "__main__":
    get_chipset_info()
