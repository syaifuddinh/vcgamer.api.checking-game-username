from sanic import Sanic
from sanic.response import json
from aoiklivereload import LiveReloader
from dotenv import load_dotenv
import os
from routes import Game
from sanic_cors import CORS
from controllers import TestingController

load_dotenv()

app = Sanic("CheckingGameApp")
CORS(app, resources={r"*": {"origins": "*"}}, automatic_options=True)
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

if __name__ == "__main__":

	# Hot reload

    # reloader = LiveReloader()
    # reloader.start_watcher_thread()
    # end of Hot reload

    app.run(host="0.0.0.0", port=3001)