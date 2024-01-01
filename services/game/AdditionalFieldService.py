from utils import Database

def GetAvailability(gameSlug):
	query = 'SELECT COUNT(id) AS amount FROM "MTAdditionalField" WHERE "gameSlug" = \'' + gameSlug + '\''
	dbResult = Database.FirstFromQuery(query)
	amount = dbResult[0] 

	return amount > 0

def GetAdditionalField(gameSlug):
	result = None
	if GetAvailability(gameSlug) == True:
		query = 'SELECT "additionalField", "additionalFieldLabel", "additionalFieldType" FROM "MTAdditionalField" WHERE "gameSlug" = \'' + gameSlug + '\''
		dbResult = Database.FirstFromQuery(query)
		result = { 
			"additionalField": dbResult[0],
			"additionalFieldLabel": dbResult[1], 
			"additionalFieldType": dbResult[2] 
		}

	return result