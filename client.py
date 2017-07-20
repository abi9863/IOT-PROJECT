import sys
import Adafruit_DHT
import socket
import demjson
import time
host='192.168.51.58'
port=9000
s=socket.socket(socket.AF_INET.SOCK_STREAM)
print("Network Initiated")
s.connect((host,port))
print("Network Established")
while True:
	h,t=Adafruit_DHT.read_retry(11,4)
	time.sleep(3)
	k=[{'h':h,'t':t}]
	i+=1
	j=demjson.encode(k)
	s.sendall(j.encode())
	s.close()
