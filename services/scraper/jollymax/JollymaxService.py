from services.scraper import CrawlerService
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import Database
from services.api import ApiService

jollymaxUrl = "https://api.jollymax.com/jolly-gateway/topup/order/check-uid"

def GetJollymaxDetailByJollymaxSlug(jollymaxSlug):
	query = 'SELECT id, "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType" FROM "MTJollymaxGame" WHERE "jollymaxSlug" = \'' + jollymaxSlug +  '\''
	dbResult = Database.FetchFromQuery(query)
	firstRow = dbResult[0]
	response = {
		"id": firstRow[0],
		"jollymaxSlug": firstRow[1],
		"jollymaxAppId": firstRow[2],
		"jollymaxGoodId": firstRow[3],
		"additionalField": firstRow[4],
		"additionalFieldType": firstRow[5]
	}

	return response


def CrawlByAPI(userGameId, jollymaxSlug, textualServerId=None):
	detail = GetJollymaxDetailByJollymaxSlug(jollymaxSlug)
	jollymax = {
		"appId": detail["jollymaxAppId"],
		"goodId": detail["jollymaxGoodId"],
		"alias": detail["jollymaxSlug"]
	}
	params = {
		"token": "de649e4339bd47c6b2eced5891a59623",
		"jmsId": "",
		"appId": jollymax["appId"],
		"roleName": "",
		"country": "id",
		"language": "en",
		"appAlias": jollymax["alias"],
		"platformName": "",
		"serverId": textualServerId,
		"goodsId": jollymax["goodId"],
		"payTypeId": "801988",
		"userId": userGameId,
		"activityId": "",
		"serverName": "",
		"domain": "www.jollymax.com",
		"deviceId": "0f64a714e3ab495aafb5e66c4a768cc9"
	}
	data = ApiService.Post(jollymaxUrl, params)
	return data

def GetIdentifiedUsername(userGameId, jollymaxSlug, textualServerId = None):
	crawlingResult = CrawlByAPI(userGameId, jollymaxSlug, textualServerId)
	resultLabel = crawlingResult["data"]["isValid"]
	notFoundLabel = 0
	foundLabel = 1
	response = { "userGameId": userGameId }
	if resultLabel == notFoundLabel:
		response["isAvailable"] = False
	elif resultLabel == foundLabel:
		response["isAvailable"] = True
	else:
		response["isAvailable"] = False

	return response

def GetJollymaxDetail(gameSlug):
	query = 'SELECT id, "jollymaxSlug", "additionalField", "additionalFieldType" FROM "MTJollymaxGame" WHERE "gameSlug" = \'' + gameSlug +  '\''
	dbResult = Database.FetchFromQuery(query)
	firstRow = dbResult[0]
	response = {
		"id": firstRow[0],
		"jollymaxSlug": firstRow[1],
		"additionalField": firstRow[2],
		"additionalFieldType": firstRow[3]
	}

	return response

def GetUsernameAvailability(userId, gameSlug, textualServerId = None):
	codashopDetail = GetJollymaxDetail(gameSlug)
	jollymaxSlug = codashopDetail["jollymaxSlug"]
	data = GetIdentifiedUsername(userId, jollymaxSlug, textualServerId)
	return data




