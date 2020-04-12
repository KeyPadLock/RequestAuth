# importing the requests library 
import requests 
import hashlib
import time
import threading
import RPi.GPIO as GPIO

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

# global variables
isTimeout = False
tries = 0
MAXRETRIES = 4

# validate password at API endpoint
def validate(passwd, URL):

	# hash the pin number
	hashPass = hashlib.sha224(passwd.encode('utf8')).hexdigest()

	# defining a params dict for the parameters to be sent to the API 
	REQJSON = {'pass':hashPass} 

	# sending post request and saving the response as response object 
	r = requests.post(url = URL, data = REQJSON) 

	# extracting data in json format 
	data = r.json() 

	return data['isValid']

# light up indicator LED: pin 22 -> Green, pin 17 -> Red, pin 27 -> Yellow
def indicate(pinNum, timeout = 0):
	# reset all LEDs first
	GPIO.output(22, GPIO.LOW)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(27, GPIO.LOW)

	# turn on the specified LED
	GPIO.output(pinNum, GPIO.HIGH)

	# light the LED for 5 seconds plus timeout time
	time.sleep(5+timeout)

	# turn off the LED
	GPIO.output(pinNum, GPIO.LOW)

def handleInput(p):
	global isTimeout, tries, MAXRETRIES

	# validate the input through the API
	valid = validate(p, "http://10.0.0.190:3000/auth")

	# if the pin is valid or not
	if(valid):
		print("Access Granted")
		# start thread to idnicate Green light
		thread = threading.Thread(target=indicate, args=(22,))
		thread.start()
		# reset the tries to count
		tries = 0
	else:
		print("Access Denied")
		if(tries < MAXRETRIES):
			# start thread to indicate Red Light
			thread = threading.Thread(target=indicate, args=(17,))
			thread.start()			
			# increment the tries count
			tries += 1
		else:
			print("Timout for 30s")
			tries = 0
			# start thread to indicate Yellow light plus timeout time of 25s
			isTimeout = True
			thread = threading.Thread(target=indicate, args=(27,25))
			thread.start()				
			# wait for the thread to finish to enforce timeout
			thread.join()
			isTimeout = False


if __name__ == '__main__':

	# always look for input
	while(True):
		# get input
		p = input()

		# if in timeout state, don't accept input
		if(isTimeout):
			print("Input Rejected: Timeout")
		else:
			# start thread to handle input
			thread = threading.Thread(target=handleInput, args=(p,))
			thread.start()
