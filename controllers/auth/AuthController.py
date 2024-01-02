from sanic.response import json
from utils import Database
from utils import JWT
from services.auth import AuthService
from flask import Flask, jsonify, request

def Login():
	keyword = request.args.get("keyword")
	data = None

	try:
		email = request.get_json()["email"]
		password = request.get_json()["password"]
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
		return jsonify({
			"status": 401,
			"message" : f'{e}',
			"data": data
		})		

	return jsonify({
		"status": 200,
		"message": "Login is success",
		"data": data
	})

def GetApiKey():
	authData = dict(request.headers)["Authorization"]
	slicedAuth = authData.split(" ")
	payload = JWT.Decode(slicedAuth[1])
	print("payload :")
	print(payload)
	email = payload["email"]
	data = AuthService.GetApiKey(email)
	return jsonify({
		"status": 200,
		"message": None,
		"data": data
	})