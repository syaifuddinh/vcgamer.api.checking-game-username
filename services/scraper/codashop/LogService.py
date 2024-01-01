from services.log import LogService

providerName = "CODASHOP"

def LogForInitiating(emailSource, gameSlug, userGameId):
	LogService.LogForInitiating(emailSource=emailSource, gameSlug=gameSlug, providerName=providerName, userGameId=userGameId)

def LogForFound(emailSource, gameSlug, userGameId):
	LogService.LogForFound(emailSource=emailSource, gameSlug=gameSlug, providerName=providerName, userGameId=userGameId)

def LogForNotFound(emailSource, gameSlug, userGameId):
	LogService.LogForNotFound(emailSource=emailSource, gameSlug=gameSlug, providerName=providerName, userGameId=userGameId)

def LogForFail(emailSource, gameSlug, userGameId):
	LogService.LogForFail(emailSource=emailSource, gameSlug=gameSlug, providerName=providerName, userGameId=userGameId)

