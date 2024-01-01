from services.scraper import CrawlerService
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import Database
import re
from selenium.webdriver.common.action_chains import ActionChains
from services.game import ServerService

codashopUrl = "https://www.codashop.com/id-id/mobile-legends"

def SelectServer(el, index):
	spectator = ActionChains(el)
	selector = ".dropdown-select__placeholder"
	optionSelector = ".result:nth-child(" + index + ")"

	targetEl = el.find_element(By.CSS_SELECTOR, selector)
	# spectator.move_by_offset(624, 144).click().perform()
	time.sleep(9)
	spectator.move_to_element(targetEl).click().perform()
	time.sleep(2)
	resultElements = el.find_elements(By.CSS_SELECTOR, optionSelector) 

	if len(resultElements) > 0:
		resultEl = resultElements[0]
		spectator.move_to_element(resultEl).click().perform()
	# closeButtonEl.click()
	# closeElements = el.find_elements(By.CSS_SELECTOR, closeSelector)
	
	# optionEl = el.find_element(By.CSS_SELECTOR, optionSelector)
def GetModalLabel(driver, timeout = 4):
	buyingButton = driver.find_element(By.CSS_SELECTOR, "#mdn-submit")
	buyingButton.click()
	time.sleep(timeout)
	labelElements = driver.find_elements(By.CSS_SELECTOR, "p.modal-header__title")
	# if len(labelElements) == 0:
	# 	return GetModalLabel(driver, timeout=timeout + 2)

	labelElement = labelElements[0]

	label = labelElement.text
	return label

def CrawlByUI(userGameId, codashopSlug, textualServerId=None, serverIndex=None):
	baseUrl = "https://www.codashop.com/id-id"
	targetUrl = baseUrl + "/" + codashopSlug
	driver = CrawlerService.OpendAndGetPage(targetUrl, "input#userId")

	userInput = driver.find_element(By.CSS_SELECTOR, "input#userId")
	shoppingItems = driver.find_elements(By.CSS_SELECTOR, ".form-section__denom")
	shoppingItem = shoppingItems[1]
	payments = driver.find_elements(By.CSS_SELECTOR, ".form-section__pc-container")
	payment = payments[0]

	userInput.send_keys(userGameId)
	if serverIndex is not None:
		SelectServer(driver, index=serverIndex)
	elif textualServerId is not None: 
		serverIdInput = driver.find_element(By.CSS_SELECTOR, "input#zoneId")
		serverIdInput.send_keys(textualServerId)

	shoppingItem.click()
	payment.click()
	time.sleep(0.3)
	try:
		label = GetModalLabel(driver)
	except:
		return CrawlByUI(
			userGameId, 
			codashopSlug,
			textualServerId=textualServerId, 
			serverIndex=serverIndex
		)

	return label

def GetIdentifiedUsername(userGameId, codashopSlug, textualServerId=None, serverIndex=None):
	resultLabel = CrawlByUI(userGameId, codashopSlug, textualServerId, serverIndex=serverIndex)
	notFoundPattern = r"(tidak ditemukan)"
	foundLabel = "Detail pesanan"
	response = { "userGameId": userGameId }
	if re.match(notFoundPattern, resultLabel):
		response["isAvailable"] = False
	elif resultLabel == foundLabel:
		response["isAvailable"] = True
	else:
		response["isAvailable"] = False

	return response

def GetCodashopDetail(gameSlug):
	query = 'SELECT id, "codashopSlug", "additionalField", "additionalFieldType" FROM "MTCodashopGame" WHERE "gameSlug" = \'' + gameSlug +  '\''
	dbResult = Database.FetchFromQuery(query)
	firstRow = dbResult[0]
	response = {
		"id": firstRow[0],
		"codashopSlug": firstRow[1],
		"additionalField": firstRow[2],
		"additionalFieldType": firstRow[3]
	}

	return response


def GetUsernameAvailability(userId, gameSlug, textualServerId=None, fieldType=None):
	codashopDetail = GetCodashopDetail(gameSlug)
	codashopSlug = codashopDetail["codashopSlug"]
	codashopIndex = None
	if fieldType == "OPTIONS":
		serverDetail = ServerService.GetServerDetail(gameSlug, textualServerId)
		if serverDetail is None:
			raise Exception("Server is not found")
		codashopIndex = serverDetail["codashopIndex"]

	data = GetIdentifiedUsername(userId, codashopSlug, textualServerId, serverIndex=codashopIndex)
	return data




