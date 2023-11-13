import requests

API_URL = " "
headers = {""}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Give me a list of 10 companies in the S&P 500 that have the highest market cap?",
})

print(output)
