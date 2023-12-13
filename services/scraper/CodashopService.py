from services.scraper import CrawlerService
from services.api import CodashopApiService
import time
from selenium.webdriver.common.by import By

codashopUrl = "https://www.codashop.com/id-id/mobile-legends"

def CrawlRegularly(userId, codashopGameSlug):
	data = CodashopApiService.GetUsernameValidity(userId, codashopGameSlug)
	return data	

def GetUsernameAvailability(userId, gameSlug):
	data = CrawlRegularly(userId, "MOBILE_LEGENDS")
	return data


