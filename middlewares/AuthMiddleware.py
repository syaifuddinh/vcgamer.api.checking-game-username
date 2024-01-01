from sanic.response import json
from utils import JWT
import re

def PassRoute(host, url):
	disallowed = ["/game", "/log", "/auth/api-key"]
	result = False
	print(f'''
		host : {host}, url : {url}
	''')
	for route in disallowed:
		pattern = r'(' + host + '\\' + route + ')'
		if re.search(pattern, url):
			result = True
			break
	return result


async def ValidateToken(request):
	isTested = PassRoute(request.host, request.url)
	if isTested:
		try:
			authData = request.headers.get("Authorization")
			slicedAuth = authData.split(" ")
			if slicedAuth[0] != "Bearer":
				raise Exception("Unauthorized")

			payload = JWT.Decode(slicedAuth[1])
			print("jwt : ")
			print(slicedAuth[1])
			if payload is None:
				raise Exception("Unauthorized")
		except Exception as e:
			print(e)
			return json({
				"status": 401,
				"message": "Unauthorized"
			})
