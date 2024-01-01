from utils import Database
from utils import String
from utils import Bcrypt

def GetDetailByEmail(email):
	query = f'''
		SELECT id, fullname, password, "apiKey" 
		FROM "MTUser"
		WHERE email = '{email}'  
	'''
	dbResult = Database.FirstFromQuery(query)
	result = None
	if dbResult is not None:
		result = {
			"id": dbResult[0],
			"fullname": dbResult[1],
			"password": dbResult[2],
			"apiKey": dbResult[3]
		}

	return result