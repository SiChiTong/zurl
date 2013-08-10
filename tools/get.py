import sys
import uuid
import tnetstring
import zmq

if len(sys.argv) < 2:
	print "usage: %s [url]" % sys.argv[0]
	sys.exit(1)

ctx = zmq.Context()
sock = ctx.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5553")

req = dict()
req["id"] = str(uuid.uuid4())
req["method"] = "GET"
req["uri"] = sys.argv[1]
#req["ignore-tls-errors"] = True
sock.send("T" + tnetstring.dumps(req))

resp = tnetstring.loads(sock.recv()[1:])
if "type" in resp and resp["type"] == "error":
	print "error: %s" % resp["condition"]
	sys.exit(1)

print "code=%d reason=[%s]" % (resp["code"], resp["reason"])
for h in resp["headers"]:
	print "%s: %s" % (h[0], h[1])

if "body" in resp:
	print "\n%s" % resp["body"]
else:
	print "\n"
