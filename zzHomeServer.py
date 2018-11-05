

################### ~/bin/homechain$/config.py contents ################### config.py contents
pwm_output_local = 15
pwm_has_changed_front_lights = 1
pwm_gnd_front_lights = 15
billionth_loop = 0
broker_address_pi_1 = "192.168.1.101"
broker_address_homeserver = "192.168.1.99"
gain = 2
################### ~/bin/homechain$/config.py contents ################### config.py contents

################### ~/bin/homechain/python1.py contents ################### python1.py contents
## Global setup
import config
counter = config.pwm_gnd_front_lights
billionth_loop = config.billionth_loop
pwm_has_changed = config.pwm_has_changed_front_lights
from RPi import GPIO
from time import sleep
clk = 17
dt = 18
butn = 27
count = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(butn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
clkLastState = GPIO.input(clk)
btnLastState = GPIO.input(butn)
try:
	## For testing connection
	while True:
		clkState = GPIO.input(clk)
		dtState = GPIO.input(dt)
		btnState = GPIO.input(butn)
		if clkState != clkLastState:
			if dtState != clkState:
				counter += 1
			else:
				counter -= 1
			if counter < 0:
				counter = 0
			if counter > 100:
				counter = 100
			# On change set flag
			pwm_has_changed = 1
			#Make counter info available to block miner, don't wait for confirmation
			print counter
			clkLastState = clkState
		if btnState != btnLastState:
			print btnState
			btnLastState = btnState
		# count += 1
		# # Send e-mail after the 1 billionth loop
		# if count > 0:
			# count += 1
			# if count == 1000000000000:
				# billionth_loop = 1
				# # Only do once
				# count = 0
		sleep(0.0001)
finally:
	GPIO.cleanup()
################### ~/bin/homechain$/python1.py contents ################### python_1.py contents

################### ~/bin/homechain/python2.py contents ################### python2.py contents
## Global setup
import config
import paho.mqtt.client as mqtt
import smtplib
from email.mime.text import MIMEText
from time import sleep
counter = config.pwm_gnd_front_lights
pwm_gnd_front_lights_local = 0
pwm_has_changed = 
billionth_loop = config.billionth_loop
# On change detected modify pwm global value and set flag
def on_message(client, userdata, message):
	counter = message.payload.decode("utf-8")
	pwm_has_changed = 1
def billionth_email():
	smtp_ssl_host = 'mail.tomdwyer.co.uk'  # smtp.mail.yahoo.com
	smtp_ssl_port = 465
	username = 'homechain@tomdwyer.co.uk'
	password = 'qhaHZUEZDHlz4PP6kavI'
	sender = 'homechain@tomdwyer.co.uk'
	targets = ['tom.uwe@gmail.com', 'tim@thedwyers.co.uk']
	msg = MIMEText('One billion loops of code successfully run, Pi_Server.')
	msg['Subject'] = 'Congratulations!'
	msg['From'] = sender
	msg['To'] = ', '.join(targets)
	server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
	server.login(username, password)
	server.sendmail(sender, targets, msg.as_string())
	server.quit()
## Local setup
thisIP = config.broker_address_homeserver
client = mqtt.Client()
# Connect to broker
client.connect("127.0.0.1", 1883, 60)
# Subscribe to topics
client.subscribe("home/ground/front_room/front_lights")
client.subscribe("home/ground/front_room/rear_lights")
# Make action on message received
client.on_message=on_message
# Main loop 2 execute forever
while True:
	if counter != pwm_gnd_front_lights_local:
		client.publish("home/ground/front_room/front_lights_rm", payload=counter, qos=1, retain=True)
		pwm_gnd_front_lights_local = counter
		# On change reset flag
		pwm_has_changed = 0
		print pwm_gnd_front_lights_local
		if billionth_loop == 1:
			billionth_email
			billionth_loop = 0
	sleep(0.01)
################### ~/bin/homechain/python2.py contents ################### python2.py contents

# Start processes
subprocess.run(python1.py)
subprocess.run(python2.py)
sudo python python1.py & sudo python python2.py
sudo python python_1.py & sudo python python_2.py
## https://learn.adafruit.com/diy-esp8266-home-security-with-lua-and-mqtt/configuring-mqtt-on-the-raspberry-pi
#Test
print("1. Import mqtt...")
import paho.mqtt.client as mqtt
print("2. Defining on_connect...")
def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions wil$
        client.subscribe("home/ground/front_room/front_lights")
# The callback for when a PUBLISH message is received from the server.
print("3. Defining on_message...")
def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
print("4. Defining on_publish...")
def on_publish():
        print("Message sent!")
print("5. Establishing mqqt.Client...")
client = mqtt.Client("127.0.0.1")
print("6. Establishing on_connect callback...")
client.on_connect = on_connect
print("7. Establishing on_message callback...")
client.on_message = on_message
print("7.1 Establishing on_publish callback...")
client.on_publish = on_publish
print("8. Connecting to client...")
#client.connect("iot.eclipse.org", 1883, 60)
client.connect("127.0.0.1", 1883, 60)
print("9. Establishing topic...")
topic = "home/ground/front_room/front_lights_rm"
print("10. Publishing message topic...")
client.publish(topic, payload="30", qos=1, retain=True)
print("11. Calling on_publish...")
on_publish
print("End")


