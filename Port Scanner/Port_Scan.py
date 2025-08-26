import socket
import sys

target = sys.argv[1]
port = int(sys.argv[2])


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)

code = sock.connect_ex((target, port))

if code == 0:
	print(f'[+] - Port {port} is open')
