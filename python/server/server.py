#!/usr/bin/env python
from gevent import monkey
monkey.patch_all()
from gevent.server import StreamServer
from collatz import Collatz


print "Initializing..."
coll = Collatz()
print "Ready to Serve."

def handler(socket, address):
    global coll
    print "Got Connection from %s:%s"%(address)
    fileobj = socket.makefile()
    while True:
        line = fileobj.readline()
        if not line:
            print "Client at %s:%s disconnected"%(address)
            break
        min_str, max_str = line.strip().split(" ")
        out = min_str + " " + max_str
        min_num = int(min_str)
        max_num = int(max_str)
        max_cycles = coll.max_cycles_r(min_num, max_num)
        out += " %s\n"%(max_cycles)
        fileobj.write(out)
        fileobj.flush()
        #print out
    socket.close()

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8000
    server = StreamServer((host, port),handler)
    print "Serving on %s:%s"%(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print "Quitting..."
        exit(0)