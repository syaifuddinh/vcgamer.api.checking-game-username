from sanic.response import json
from utils import Database
from utils import JWT
from services.auth import AuthService

def Login(request):
	keyword = request.args.get("keyword")
	data = None

	try:
		email = request.json.get("email")
		password = request.json.get("password")
		if email is None:
			raise Exception("Email is required")
		if password is None:
			raise Exception("Password is required")

		token = AuthService.Login(
			email=email,
			password=password
		)
		data = { "token": token }

	except Exception as e:
		return json({
			"status": 401,
			"message" : f'{e}',
			"data": data
		})		

	return json({
		"status": 200,
		"message": "Login is success",
		"data": data
	})

def GetApiKey(request):
	authData = request.headers.get("Authorization")
	slicedAuth = authData.split(" ")
	payload = JWT.Decode(slicedAuth[1])
	print("payload :")
	print(payload)
	email = payload["email"]
	data = AuthService.GetApiKey(email)
	return json({
		"status": 200,
		"message": None,
		"data": data
	})