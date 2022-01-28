import time
import openpyxl as xl
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

chrome_options = webdriver.ChromeOptions()
prefs = {
	"profile.managed_default_content_settings.images": 2
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('./chromedriver', options = chrome_options)


'''driver.get('https://login.microsoftonline.com/common/oauth2/authorize?client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&resource=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3DeyJ2ZXJzaW9uIjoxLCJkYXRhIjp7IklkZW50aXR5UHJvdmlkZXIiOiJBWXR0OEtfWDJjYVRZYmI1REMzZ2FrOUJhVXdzN3dDY2h0engzOHJtakxnTndZWWNqLXRNOFc4dWlBWTBLUnR3anlwWEx3QnJNOThHWG42YUUzTUJZT1EiLCIucmVkaXJlY3QiOiJodHRwczovL2Zvcm1zLm9mZmljZS5jb20vUGFnZXMvUmVzcG9uc2VQYWdlLmFzcHg_aWQ9bjdqeEJ1Z0hUMGEwQ093YlJYQV9NZTdmeVNucDlmeER0LUZHbUVQSUcwNVVRbGRRUmxSU1JVeGFWRGhaTWtKQ01VOU9Ra2hTVkZReVR5NHUmc2lkPTAzNWNhOTQzLWY2MGEtNDc2Ny1iODQyLWQ4ODE1NmZhMmYxZCJ9fQ&response_mode=form_post&nonce=637761623338779491.MjMzMmYzYmUtMjFhNC00ZjQwLTk1ZGQtYWRjM2MzM2FiNTZmMTk3Y2ZiYjMtY2MyOS00OTU2LWE0NTQtMDg2MzAzM2Q1NWFh&redirect_uri=https%3A%2F%2Fforms.office.com%2Flanding&msafed=0&x-client-SKU=ID_NET472&x-client-ver=6.14.1.0&sso_reload=true')
time.sleep(2)

input_search=driver.find_element_by_css_selector('input[name="loginfmt"')
input_search.send_keys('hoan.dt204974@sis.hust.edu.vn')
driver.find_element_by_id('idSIButton9').click()

time.sleep(3)
input_search=driver.find_element_by_css_selector('input[name="Password"')
input_search.send_keys('031202008945')

driver.find_element_by_id('submitButton').click()
time.sleep(1)
driver.find_element_by_id('KmsiCheckboxField').click()
driver.find_element_by_id('idSIButton9').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/label/input').click()
driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/label/input').click()
driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/label/input').click()
'''

driver.get('https://forms.office.com/r/0jwCWvT9Gb')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/label/input').click()
driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/label/input').click()
#driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()
