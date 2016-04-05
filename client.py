import sys
import socket
import time

# This client connects to catserver (which is in same bridge network)
if (len(sys.argv)!=3):
    print >>sys.stderr, "Usage:"
    print >>sys.stderr, "python client.py port textfile"
    sys.exit(0)

host = 'catserver'
port = int(sys.argv[2])
size = 1024
fname = str(sys.argv[1])
content = [line.upper() for line in open(fname)]
if len(content) == 0:
    print >>sys.stderr, 'FILE EMPTY, EXITING'
    sys.exit(0)

for i in range(10):
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_socket.connect((host,port))
    send_socket.send('LINE')
    data = send_socket.recv(size)
    if data in content:
        print >>sys.stderr, 'OK'
    else:
        print >>sys.stderr, 'MISSING'
    send_socket.close()
    time.sleep(3)