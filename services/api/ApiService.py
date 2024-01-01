import requests
import json

# Replace 'your_api_url' with the actual URL of the API you want to interact with

def Get(apiUrl):
	# Make a GET request to the API
	response = requests.get(apiUrl)
	data = {}
	# Check if the request was successful (status code 200)
	if response.status_code == 200:
		# Parse the JSON data returned by the API
		data = response.json()
	else:
		# Print an error message if the request was not successful
		print(f"Error: {response.status_code} - {response.text}")

	return data

def Post(apiUrl, params):
	# Make a GET request to the API
	headers = {'Content-Type': 'application/json'}
	jsonData = json.dumps(params)
	response = requests.post(apiUrl, data=jsonData, headers=headers)
	data = {}
	# Check if the request was successful (status code 200)
	if response.status_code == 200:
		# Parse the JSON data returned by the API
		data = response.json()
	else:
		# Print an error message if the request was not successful
		print(f"Error: {response.status_code} - {response.text}")

	return data
