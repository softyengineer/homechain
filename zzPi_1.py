# # import paho.mqtt.client as mqtt #import the client1
# # import time
# # ############
# # def on_message(client, userdata, message):
    # # print("message received " ,str(message.payload.decode("utf-8")))
    # # print("message topic=",message.topic)
    # # print("message qos=",message.qos)
    # # print("message retain flag=",message.retain)
# # ########################################
# # broker_address="192.168.1.184"
# # #broker_address="iot.eclipse.org"
# # print("creating new instance")
# # client = mqtt.Client("P1") #create new instance
# # client.on_message=on_message #attach function to callback
# # print("connecting to broker")
# # client.connect(broker_address) #connect to broker
# # client.loop_start() #start the loop
# # print("Subscribing to topic","house/bulbs/bulb1")
# # client.subscribe("house/bulbs/bulb1")
# # print("Publishing message to topic","house/bulbs/bulb1")

# # client.publish("house/bulbs/bulb1","OFF")

# # time.sleep(4) # wait
# # client.loop_stop() #stop the loop

#https://pypi.org/project/paho-mqtt/

# Python Programs
# 1. Read encoder value
# 1.1 Modify PWM output
# 2. Broadcast value
# 4. Receive value
# 5. Save value

################### ~/homechain/config.py contents ################### config.py contents
pwm_output_local = 15.0
pwm_has_changed_front_lights = 1
pwm_gnd_front_lights = 0
billionth_loop = 0
broker_address_pi_1 = "192.168.1.101"
broker_address_homeserver = "192.168.1.99"
gain = 2
################### ~/homechain/config.py contents ################### config.py contents

################### ~/homechain/python1.py contents ################### python1.py contents
## Global setup
import config
from RPi import GPIO
from time import sleep
# Import pwm_output_local and billionth_loop as integers
pwm_output_local = config.pwm_output_local
billionth_loop = config.billionth_loop
# Definitions
pwm_has_changed = config.pwm_has_changed_front_lights
count = 1
# Encoder right pins
clk_r = 17
dt_r = 18
butn_r = 27
counter_r = 0
difference_r = 0
# Encoder left pins
clk_l = 8
dt_l = 11
butn_l = 7
counter_l = 0
difference_l = 0
# PWM pin setup (7)
lt = 4
pwm_freq = 2000
gain = config.gain
pwm_internal = 0
# Config
GPIO.setmode(GPIO.BCM)
# GPIO pins for encoder right
GPIO.setup(clk_r, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt_r, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(butn_r, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO pins for encoder left
GPIO.setup(clk_l, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt_l, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(butn_l, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO pins for light
GPIO.setup(lt, GPIO.OUT)
p = GPIO.PWM(lt, pwm_freq)
# Read state of pins
clk_rLastState = GPIO.input(clk_r)
btn_rState = GPIO.input(butn_r)
clk_lLastState = GPIO.input(clk_l)
btn_lState = GPIO.input(butn_l)
# Start light
p.start(pwm_output_local)
try:
	# Main loop 1, execute forever
	while True:
		clk_rState = GPIO.input(clk_r)
		clk_lState = GPIO.input(clk_l)
		dt_rState = GPIO.input(dt_r)
		dt_lState = GPIO.input(dt_l)
		btn_rState = GPIO.input(butn_r)
		btn_lState = GPIO.input(butn_l)
		# R-H encoder
		if clk_rState != clk_rLastState:
			if dt_rState != clk_rState:
				counter_r += 1
				difference_r = 1
			else:
				counter_r -= 1
				difference_r = -1
			#Modify PWM pin for r-h light
			pwm_output_local = pwm_output_local + (difference * gain) # 2 for gain
			if pwm_output_local < 0:
				pwm_output_local = 0
			if pwm_output_local > 100:
				pwm_output_local = 100
			# On change set flag
			pwm_has_changed = 1
		# L-H encoder
		if clk_lState != clk_lLastState:
			if dt_lState != clk_lState:
				counter_l += 1
				difference_l = 1
			else:
				counter_l -= 1
				difference_l = -1
			#Modify PWM pin for light
			pwm_output_remote = pwm_output_remote + (difference * gain) # 2 for gain
			if pwm_output_remote < 0:
				pwm_output_remote = 0
			if pwm_output_remote > 100:
				pwm_output_remote = 100
			clk_rLastState = clk_rState
			clk_lLastState = clk_rState
		# Send e-mail after the 1 billionth loop
		if count > 0:
			count += 1
			if count == 1000000000000:
				billionth_loop = 1
				# Only do once
				count = 0
		# Button press
		# pwm = - pwm
		# Button press
		## Setup pins
		if btn_rState == 0:
			pwm_output_local = 0
			pwm_has_changed = 1
		if btn_lState == 0:
			pwm_output_remote = 0
		# Monitor for change flag
		if pwm_has_changed != 0:
			# Blend
			pwm_internal = (0.95 * pwm_internal) + (0.05 * pwm_output_local)
			p.ChangeDutyCycle(pwm_internal)
			if pwm_internal - pwm_output_local = 0:
				pwm_has_changed = 0
			# Debug
			print "pwm_internal = " + pwm_internal
			print pwm_output_local
	sleep(0.0001)
finally:	#?
	GPIO.cleanup()
################### python1.py contents ################### python1.py contents
		
		
################### homechain/python_2.py contents ################### python_2.py contents
def on_message(client, userdata, message):
	# On change detected modify pwm global value and set flag
	pwm_output_local = message.payload.decode("utf-8")
	pwm_has_changed = 1
	print pwm_output_local
def billionth_email():
	smtp_ssl_host = 'mail.tomdwyer.co.uk'  # smtp.mail.yahoo.com
	smtp_ssl_port = 465
	username = 'homechain@tomdwyer.co.uk'
	password = 'qhaHZUEZDHlz4PP6kavI'
	sender = 'homechain@tomdwyer.co.uk'
	targets = ['tom.uwe@gmail.com', 'tim@thedwyers.co.uk']
	msg = MIMEText('One billion loops of code successfully run, Pi_Zero 1')
	msg['Subject'] = 'Congratulations!'
	msg['From'] = sender
	msg['To'] = ', '.join(targets)
	server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
	server.login(username, password)
	server.sendmail(sender, targets, msg.as_string())
	server.quit()
## Global setup
import config
import paho.mqtt.client as mqtt
import smtplib
from email.mime.text import MIMEText
pwm_output_local = config.pwm_output_local
billionth_loop = config.billionth_loop
## Local setup
thisIP = config.broker_address_pi_1
client = mqtt.Client(thisIP)
# Connect to broker
client.connect(thisIP)
# Subscribe to topic
client.subscribe("home/ground/front_room/front_lights_rm")
# Make action for when message received
client.on_message=on_message ### ??? Will this cause the code to hang here until a message is received??
# Main loop 2, execute forever
while True:
	if pwm_output_local != pwm_local_local:
		pwm_local_local = pwm_output_local
		client.publish("home/ground/front_room/front_lights", payload=pwm_output_local, qos="1", Retain="True")
		# mosquitto_pub -d -h localhost -q 0 -t "home/ground/front_room/front_lights" -m pwm_output
	if pwm_output_remote != pwm_local_remote:
		pwm_local_remote = pwm_output_remote
		client.publish("home/ground/front_room/rear_lights", payload=pwm_output_remote, qos="1", Retain="True")
		# mosquitto_pub -d -h localhost -q 0 -t "home/ground/front_room/front_lights" -m pwm_output
	if billionth_loop == 1:
		billionth_email
		billionth_loop = 0
	sleep(1)
################### homechain/python2.py contents ################### 

# Install pip
sudo apt-get update
sudo apt-get install python-pip
# Install maho mqtt

# Start processes
sudo python python1.py & sudo python python2.py