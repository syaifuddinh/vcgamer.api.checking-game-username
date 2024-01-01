from utils import Database

def GetServerDetail(gameSlug, serverId):
	query = f'''
	SELECT "codashopIndex" FROM "MTServer" 
	WHERE "gameSlug" = '{gameSlug}' AND "serverSlug"='{serverId}'
	'''
	print("server query :")
	print(query)
	dbResult = Database.FirstFromQuery(query)
	response = {
		"codashopIndex": dbResult[0]
	}

	return response

def GetServer(gameSlug):
	query = f'''
		SELECT "id", "serverSlug", "serverName" 
		FROM "MTServer"
		WHERE "gameSlug" = '{gameSlug}'
	'''
	dbResult = Database.FetchFromQuery(query)
	response = None
	if len(dbResult) > 0:
		response = [{
			"id": item[0], 
			"slug": item[1], 
			"name": item[2]
		} for item in dbResult] 

	return response