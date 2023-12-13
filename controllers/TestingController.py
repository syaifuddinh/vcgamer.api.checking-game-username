from sanic.response import json
from services.scraper import CodashopService 

def Get(request):
	userId = request.args.get("userId")
	data = CodashopService.GetUsernameAvailability(userId, "")

	return json({
		"statusCode": 200,
		"data": data
	})
