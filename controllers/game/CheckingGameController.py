from sanic.response import json
from utils import Database

def GetUsernameAvailability(request):
	keyword = request.args.get("keyword")
	gameQuery = '''
		SELECT id, slug, "name", "thumbnailUrl" 
		FROM public."MTGame" 
	''';
	if(keyword):
		gameQuery += f'WHERE LOWER("name") LIKE TRIM(LOWER(\'%{keyword}%\'))'
	gameList = Database.FetchFromQuery(gameQuery)
	data = [{
		"id": item[0], 
		"slug": item[1], 
		"name": item[2],
		"thumbnailUrl": item[3]
	} for item in gameList] 

	return json({
		"statusCode": 200,
		"data": data
	})
