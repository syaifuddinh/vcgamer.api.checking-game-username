from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def OpendAndGetPage(pageUrl, testingSelector = None, timeout = 2):
	if timeout > 7:
		raise Exception("Can't crawl through codashop")
	driver = webdriver.Chrome()
	driver.get(pageUrl)
	time.sleep(timeout)
	if testingSelector is not None:
		testingElements = driver.find_elements(By.CSS_SELECTOR, testingSelector)
		if len(testingElements) == 0:
			return OpendAndGetPage(pageUrl, testingSelector, timeout=timeout + 1.5)

	return driver
