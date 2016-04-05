import sys
import socket

def server_forever(args):

	host = ''
	port = int(args[2])
	backlog = 5
	size = 1024
	fname = str(args[1])
	with open(fname) as f:
	    content = f.readlines()

	if len(content) == 0:
	    print >>sys.stderr, 'FILE EMPTY, EXITING'
	    sys.exit(0)

	listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listen.bind((host,port))
	listen.listen(backlog)
	print >>sys.stderr, "Server up and running at (host,port):", listen.getsockname(), "..."  
	idx = 0

	while True:
	    client, address = listen.accept()
	    data = client.recv(size)
	    if (data=='LINE'):
	        client.send(content[idx%len(content)].upper())
	        idx+=1
	    client.close()

if __name__ == '__main__':
	if (len(sys.argv)!=3):
	    print >>sys.stderr, "Usage:"
	    print >>sys.stderr, "python server.py port textfile"
	    sys.exit(0)
	server_forever(sys.argv)
