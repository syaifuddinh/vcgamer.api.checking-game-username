from selenium import webdriver
import time

def OpendAndGetPage(pageUrl):
	driver = webdriver.Chrome()
	driver.get(pageUrl)
	time.sleep(3)

	return driver
