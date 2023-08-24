import wmi

def count_chipset_types():
    c = wmi.WMI()
    chipsets = set()
    
    for item in c.Win32_BaseBoard():
        chipset = f"{item.Manufacturer} {item.Product}"
        chipsets.add(chipset)
        
    return len(chipsets)

if __name__ == "__main__":
    chipset_count = count_chipset_types()
    print(f"Number of different chipset types: {chipset_count}")
