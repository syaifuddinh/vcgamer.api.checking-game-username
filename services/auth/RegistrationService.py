from utils import Database
from utils import String
from utils import Bcrypt

def StoreToDB(email, password, fullname, apiKey):
	query = f'''
		INSERT INTO "MTUser" (
			email, fullname,
			password, "apiKey"
		) VALUES (
			'{email}', '{fullname}',
			'{password}', '{apiKey}'
		)
	'''

	Database.Execute(query)

def GetNewAPIKey():
	newApiKey = String.Random(16) 
	checkingQuery = '''
		SELECT COUNT(id) as amount 
		FROM "MTUser" 
		WHERE "apiKey" = '{newApiKey}' 
	'''
	dbResult = Database.FirstFromQuery(checkingQuery)
	isExist = dbResult[0] > 0
	if isExist == True:
		return GetNewAPIKey()

	return newApiKey

def ValidateEmail(email):
	checkingQuery = f'''
		SELECT COUNT(id) as amount 
		FROM "MTUser" 
		WHERE email = '{email}' 
	'''
	dbResult = Database.FirstFromQuery(checkingQuery)
	isExist = dbResult[0] > 0
	if isExist == True:
		raise Exception("Email is already registered")

def GetEncrytedPassword(password):
	return Bcrypt.Hash(password)

def Register(email, password, fullname):
	ValidateEmail(email)
	apiKey = GetNewAPIKey()
	encryptedPassword = GetEncrytedPassword(password)
	StoreToDB(email=email, password=encryptedPassword, fullname=fullname, apiKey=apiKey)