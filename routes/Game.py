from sanic import Sanic
from controllers.game import IndexController
from controllers.game import CheckingGameController
from controllers.game import LogController
from sanic.response import json
from middlewares import AuthMiddleware

def Init():
	app = Sanic.get_app("CheckingGameApp")

	@app.middleware("request")
	async def RegisterMiddleware(request):
		return await AuthMiddleware.ValidateToken(request)

	app.add_route(
		IndexController.Get, 
		"/game", 
		methods=["GET"]
	)
	app.add_route(
		IndexController.Show, 
		"/game/<gameSlug>", 
		methods=["GET"]
	)
	app.add_route(CheckingGameController.GetUsernameAvailability, "/check/<gameSlug>", methods=["POST"] )
	app.add_route(LogController.GetLog, "/log", methods=["GET"] )
