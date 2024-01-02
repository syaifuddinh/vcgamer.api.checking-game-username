from utils import Database
from services.game import GameService
from flask import Flask, jsonify, request

def Get():
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

	return jsonify({
		"status": 200,
		"message": None,
		"data": data
	})

def Show(gameSlug):
	data = GameService.GetGameAttribute(gameSlug)

	return jsonify({
		"status": 200,
		"message": None,
		"data": data
	})