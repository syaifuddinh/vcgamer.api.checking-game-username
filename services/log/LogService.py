from utils import Database
from utils import Date

def GetLogDescription(descriptionSlug):
	slugs = {
		"INITIATING": {"description": "User starts checking username"},
		"SUCCESS": {"description": "User has checked username successfully"},
		"FAIL": {"description": "User has checked username unsuccessfully"}
	}

	result = ""
	if descriptionSlug in slugs:
		selected = slugs[descriptionSlug]
		result = selected["description"]

	return result
def Insert(emailSource, gameSlug, providerName, userGameId, activityStatus, descriptionSlug, userGameAvailabilityStatus=""):
	description = GetLogDescription(descriptionSlug)
	transactionTime = Date.Now()
	query = f'''
		INSERT INTO  "TRLog" (
			"emailSource",
			"gameSlug",
			"providerName",
			"userGameId",
			"transactionTime",
			"activityStatus",
			"userGameAvailabilityStatus",
			"descriptionSlug",
			"description"
		) 
		VALUES (
			'{emailSource}',
			'{gameSlug}',
			'{providerName}',
			'{userGameId}',
			CAST('{transactionTime}' AS TIMESTAMP),
			'{activityStatus}',
			'{userGameAvailabilityStatus}',
			'{descriptionSlug}',
			'{description}'
		)
	'''
	Database.Execute(query)

def LogForInitiating(emailSource, gameSlug, providerName, userGameId):
	descriptionSlug = "INITIATING"
	activityStatus = "COMPLETED"
	Insert(emailSource, gameSlug, providerName, userGameId, activityStatus, descriptionSlug)

def LogForSuccess(emailSource, gameSlug, providerName, userGameId, userGameAvailabilityStatus):
	descriptionSlug = "SUCCESS"
	activityStatus = "COMPLETED"
	Insert(emailSource, gameSlug, providerName, userGameId, activityStatus, descriptionSlug, userGameAvailabilityStatus)

def LogForFound(emailSource, gameSlug, providerName, userGameId):
	userGameAvailabilityStatus = "FOUND";	
	LogForSuccess(emailSource, gameSlug, providerName, userGameId, userGameAvailabilityStatus)

def LogForNotFound(emailSource, gameSlug, providerName, userGameId):
	userGameAvailabilityStatus = "NOT-FOUND";	
	LogForSuccess(emailSource, gameSlug, providerName, userGameId, userGameAvailabilityStatus)

def LogForFail(emailSource, gameSlug, providerName, userGameId):
	descriptionSlug = "FAIL"
	activityStatus = "INCOMPLETED"
	Insert(emailSource, gameSlug, providerName, userGameId, activityStatus, descriptionSlug)
