from sanic.response import json
from services.log import LogService
from utils import Date
from services.scraper.jollymax import JollymaxService
from services.scraper import CrawlerService
from services.game import AdditionalFieldService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from services.auth import RegistrationService

def TestGenshin():
	url = "https://www.codashop.com/id-id/genshin-impact"
	el = CrawlerService.OpendAndGetPage(url)
	spectator = ActionChains(el)
	selector = ".dropdown-select__placeholder"
	optionSelector = ".result:nth-child(2)"

	targetEl = el.find_element(By.CSS_SELECTOR, selector)
	# spectator.move_by_offset(624, 144).click().perform()
	time.sleep(10)
	spectator.move_to_element(targetEl).click().perform()
	time.sleep(2)
	resultElements = el.find_elements(By.CSS_SELECTOR, optionSelector) 

	if len(resultElements) > 0:
		resultEl = resultElements[0]
		spectator.move_to_element(resultEl).click().perform()
	# closeButtonEl.click()
	# closeElements = el.find_elements(By.CSS_SELECTOR, closeSelector)
	
	# optionEl = el.find_element(By.CSS_SELECTOR, optionSelector)
	time.sleep(120)

def Get(request):

	data = RegistrationService.GetEncrytedPassword("mobile-legends")

	return json({
		"statusCode": 200,
		"data": data
	})
