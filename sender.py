# importing the requests library 
import requests 
import hashlib
import time

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
	MAXRETRIES = 4
	tries = 0
	while(True):
		p = input()
		valid = validate(p, "http://10.0.0.190:3000/auth")
		if(valid):
			print("Access Granted")
			tries = 0
		else:
			print("Access Denied")
			if(tries < MAXRETRIES):
				tries += 1
			else:
				print("Timout for 30s")
				tries = 0
				time.sleep(30)
			
