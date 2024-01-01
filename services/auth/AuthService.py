from utils import Database
from utils import Bcrypt
from utils import JWT
from services.auth import UserService

errorMessage = "Email or password is wrong"

def IsRegistered(email, password):
	userDetail = UserService.GetDetailByEmail(email)
	if userDetail is None:
		return False

	storedPassword = userDetail["password"]
	isValid = Bcrypt.GetValidity(password, storedPassword)
	return isValid 

def Login(email, password):
	isRegistered = IsRegistered(email, password)
	if isRegistered == False:
		raise Exception(errorMessage)

	data = JWT.Generate(email)

	return data

def GetApiKey(email):
	query = f'''
		SELECT "apiKey" FROM "MTUser" WHERE email='{email}'
	'''
	dbResult = Database.FirstFromQuery(query)
	response = {
		"apiKey": dbResult[0]
	};
	return response