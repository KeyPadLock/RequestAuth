# importing the requests library 
import requests 
import hashlib
import time
import RPi.GPIO as GPIO
from keypadcode import keypad_init, get_code, blink_red, blink_green

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


if __name__ == '__main__':

	keypad_init()

	try:
		# always look for input
		while(True):
			# get input
			p = get_code()
			print(p)

			valid = validate(p, "http://10.0.0.190:3000/auth")
			if(valid):
				print("Valid")
				blink_green()
			else:
				print("Invalid")
				blink_red()

	except:
		print("Exception encountered... Cleaning up GPIO pins")
	finally:
		GPIO.cleanup()
