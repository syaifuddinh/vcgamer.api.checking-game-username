from sanic import Sanic
from controllers.auth import RegistrationController
from controllers.auth import AuthController

def Init():
	app = Sanic.get_app("CheckingGameApp")
	app.add_route(RegistrationController.Register, "/auth/register", methods=["POST"] )
	app.add_route(AuthController.Login, "/auth/login", methods=["POST"] )
	app.add_route(AuthController.GetApiKey, "/auth/api-key", methods=["GET"] )
