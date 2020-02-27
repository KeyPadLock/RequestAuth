# importing the requests library 
import requests 

# api-endpoint 
URL = "http://10.0.0.211:3000/auth"

passwd = "5407"

# defining a params dict for the parameters to be sent to the API 
REQJSON = {'pass':passwd} 

# sending post request and saving the response as response object 
r = requests.post(url = URL, data = REQJSON) 

# extracting data in json format 
data = r.json() 

print ("isValid: ", data['isValid'])