from services.api import ApiService

# Replace 'your_api_url' with the actual URL of the API you want to interact with

def GetUsernameValidity(userId, codashopGameSlug):
	codashopUrl = "https://order-sg.codashop.com/validate"
	params = {
	    # "voucherTypeName":"MOBILE_LEGENDS",
	    "voucherTypeName":codashopGameSlug,
	    "userId":userId,
	    "zoneId":"16425"
	}
	data = ApiService.Post(codashopUrl, params)
	response = {}
	if("result" in data):
		response["isValid"] = True
		response["username"] = data["result"]["username"]
	else:
		response["isValid"] = False
		response["username"] = ""

	return response
