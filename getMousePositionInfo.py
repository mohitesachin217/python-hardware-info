from pynput.mouse import Controller

def get_mouse_info():
    mouse = Controller()
    position = mouse.position
    print("Mouse Information:")
    print(f"  Position: {position}")
    
if __name__ == "__main__":
    get_mouse_info()
