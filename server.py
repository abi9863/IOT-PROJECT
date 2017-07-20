import sys
import Adafruit_DHT
import socket
import demjson
import time
import MySQLdb

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',9000))
print("Network Initiated")
s.listen(5)
conn,addr=s.accept()
print("network established")
db=MySQLdb.connect("localhost","root","piraspberry","him2")

while True:
	h,t=Adafruit_DHT.read_retry(11,4)
	time.sleep(3)
	k=demjson.decode(v)
	print(k['H'])
	print(k['T'])
	print(' ')
	y=db.cursor()
	y.execute("INSERT INTO tem_sense(Temperature_one,Humidity_one,Temperature_two,Humidity_two)
	db.commit()
	conn.close()
	s.close()
