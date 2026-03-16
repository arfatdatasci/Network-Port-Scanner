import socket
import threading

target = input("Enter target IP or domain: ")

print(f"\nScanning target: {target}\n")

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: Open")

    s.close()

for port in range(1, 1025):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
