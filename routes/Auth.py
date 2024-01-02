from sanic import Sanic
from controllers.auth import RegistrationController
from controllers.auth import AuthController

def Init(app):
	app.add_url_rule(
		"/auth/register", 
		"registration",
		RegistrationController.Register, 
		methods=["POST"] 
	)
	app.add_url_rule(
		"/auth/login", 
		"login", 
		AuthController.Login, 
		methods=["POST"] )
	app.add_url_rule(
		"/auth/api-key", 
		"get-api-key",
		AuthController.GetApiKey, 
		methods=["GET"] 
	)
