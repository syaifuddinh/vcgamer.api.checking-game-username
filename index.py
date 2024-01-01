from sanic import Sanic
from sanic.response import json
from aoiklivereload import LiveReloader
from dotenv import load_dotenv
import os
from routes import Game
from routes import Auth
from controllers import TestingController

# from configs.CORS import add_cors_headers 
# from configs.Options import setup_options 
from sanic_cors import CORS, cross_origin


def application(environ, start_response):
	load_dotenv()

	app = Sanic("CheckingGameApp")
	app.config.db = {
		"name": os.environ.get("DB_NAME"),
		"username": os.environ.get("DB_USER"),
		"host": os.environ.get("DB_HOST"),
		"password": os.environ.get("DB_PASSWORD"),
		"port": os.environ.get("DB_PORT")
	}

	@app.get("/")
	async def Index(request):
		return json({
			"isSuccess": True, 
			"statusCode": 200,
			"dbName": app.config.db["name"]
		})

	@app.get("/test")
	async def Test(request):
		return TestingController.Get(request)



	Game.Init()
	Auth.Init()

	CORS(app, resources={r"/*": {"origins": "*"}})
	# app.register_listener(setup_options, "before_server_start")
	# app.register_middleware(add_cors_headers, "response")

	if __name__ == "__main__":

		# Hot reload

	    # reloader = LiveReloader()
	    # reloader.start_watcher_thread()
	    # end of Hot reload

	    app.run(host="0.0.0.0", port=3001)