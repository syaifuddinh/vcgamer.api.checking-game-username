from sanic import Sanic
from controllers.game import IndexController
from controllers.game import CheckingGameController

def Init():
	app = Sanic.get_app("CheckingGameApp")
	app.add_route(IndexController.Get, "/game", methods=["GET"] )
	app.add_route(CheckingGameController.GetUsernameAvailability, "/check", methods=["GET"] )
