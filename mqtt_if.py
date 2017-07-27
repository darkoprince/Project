from gpiozero import LED, Button
import paho.mqtt.client as mqtt
from RPLCD import CharLCD
from signal import pause
from time import sleep
import urllib2


lcd = CharLCD(cols=16, rows = 2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])



def fast(message):
	lcd.write_string(message.payload)

def on_message(client, userdata, message):
	print message.payload
	fast(message)

def on_connect(client, userdata, flags, code):
	print "connected:" + str(code)
	client.subscribe("test/richie")


	
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 8000)


client.loop_forever()
