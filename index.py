from dotenv import load_dotenv
import os
from routes import Game
from routes import Auth
from controllers import TestingController

# from configs.CORS import add_cors_headers 
# from configs.Options import setup_options 
from flask import Flask, jsonify, request


load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_books():
    return jsonify({"status": 200, "message": "Flask success ss"})


@app.route("/test", methods=['GET'])
async def Test(request):
	return TestingController.Get(request)



Game.Init(app)
Auth.Init(app)


if __name__ == "__main__":
	app.run(debug=True)