from sanic.response import json
from utils import Database
from services.auth import RegistrationService
from flask import Flask, jsonify, request

def Register():
	keyword = request.args.get("keyword")
	data = None

	try:
		email = request.json.get("email")
		password = request.get_json()["password"]
		fullname = request.get_json()["fullname"]
		if email is None:
			raise Exception("Email is required")
		if password is None:
			raise Exception("Password is required")
		if fullname is None:
			raise Exception("Fullname is required")
			
		RegistrationService.Register(
			fullname=fullname,
			email=email,
			password=password
		)

	except Exception as e:
		return jsonify({
			"status": 401,
			"message" : f'{e}',
			"data": data
		})		

	return jsonify({
		"status": 200,
		"message": "Registration is success",
		"data": data
	})
