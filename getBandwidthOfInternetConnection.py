import psutil
import time

def get_incoming_bandwidth(interval=1):
    last_bytes_received = psutil.net_io_counters().bytes_recv
    
    while True:
        current_bytes_received = psutil.net_io_counters().bytes_recv
        bytes_received_per_second = (current_bytes_received - last_bytes_received) / interval
        
        print(f"Incoming Bandwidth: {bytes_received_per_second:.2f} bytes/s")
        
        last_bytes_received = current_bytes_received
        time.sleep(interval)

if __name__ == "__main__":
    get_incoming_bandwidth()
