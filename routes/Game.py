from sanic import Sanic
from controllers.game import IndexController
from controllers.game import CheckingGameController
from controllers.game import LogController
from sanic.response import json
from middlewares import AuthMiddleware
from flask import Flask, jsonify, request

def Init(app):

	app.add_url_rule(
		"/game", 
		"game",
		IndexController.Get
	)
	app.add_url_rule(
		"/game/<string:gameSlug>", 
		"game-detail",
		IndexController.Show, 
		methods=["GET"]
	)
	app.add_url_rule(
		"/check/<string:gameSlug>",
		"checking-game",
		CheckingGameController.GetUsernameAvailability, 
		methods=["POST"]
	)
	app.add_url_rule(
		"/log", 
		"log", 
		LogController.GetLog, 
		methods=["GET"]
	)
