from services.api import ApiService

# Replace 'your_api_url' with the actual URL of the API you want to interact with

def GetUsernameValidity():
	codashopUrl = "https://order-sg.codashop.com/validate"
	params = {
	    "voucherTypeName":"MOBILE_LEGENDS",
	    "userId":"1531254246",
	    "zoneId":"16425"
	}
	data = ApiService.Post(codashopUrl, params)

	return data
