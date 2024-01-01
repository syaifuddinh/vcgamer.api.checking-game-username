from sanic.response import json
from utils import Database
from services.game import GameService 
from exceptions import ValidationError 
from services.game import AdditionalFieldService

def GetUsernameAvailability(request, gameSlug):
	isAvailable = GameService.GetGameAvailability(gameSlug)
	data = None

	if isAvailable == False:
		return json({
			"status": 404,
			"message": None 
		})

	try:
		userId = request.json.get("userId")
		if(userId is None):
			raise Exception("User ID / Game ID is required")

		meta = AdditionalFieldService.GetAdditionalField(gameSlug)
		additionalFieldRequest = None
		additionalFieldType = None
		if meta is not None:
			additionalField = meta["additionalField"]
			additionalFieldLabel = meta["additionalFieldLabel"]
			additionalFieldType = meta["additionalFieldType"]
			additionalFieldRequest = request.json.get(additionalField)
			if additionalFieldRequest is None:
				raise Exception(additionalFieldLabel + " is required")

		data = GameService.GetUsernameAvailability(userId, gameSlug, textualServerId=additionalFieldRequest, fieldType=additionalFieldType)
	except Exception as e:
		return json({
			"status": 400,
			"message": f'{e}',
			"data": None
		})		

	return json({
		"status": 200,
		"message": None,
		"data": data
	})
