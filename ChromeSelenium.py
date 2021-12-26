import time

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
driver.get('https://login.microsoftonline.com/common/oauth2/authorize?client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&resource=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3DeyJ2ZXJzaW9uIjoxLCJkYXRhIjp7IklkZW50aXR5UHJvdmlkZXIiOiJBZm1lYmFtQk1Rb01HSHQ5MEdwVk93aldqMV9yWXkxQUd5TkJWUzVwdHN2cEg4ZzMtcjV0ck1VVHk1VTl0T3UwbU5JQV9sYzRXekU0Vm5SYlpmU3NUUlkiLCIucmVkaXJlY3QiOiJodHRwczovL2Zvcm1zLm9mZmljZS5jb20vcGFnZXMvcmVzcG9uc2VwYWdlLmFzcHg_aWQ9bjdqeEJ1Z0hUMGEwQ093YlJYQV9NWUh5R1VhRWZoTk51Mmo5N1F2UWFZbFVORGREU2taQk9GTktWREkwTUVrd1RWbzBOMDgyV1VFM1RpNHUmc2lkPWYwNDc2NjZjLTcyYjktNDA0MC1hYmU3LWVlNWY5YjRjZmI3ZSJ9fQ&response_mode=form_post&nonce=637761137156942511.YzgzZmIwYTYtZWU5ZC00NDQ4LWE1YTMtNmQ2OGYzYWM0NmZkYmEzZThmZTctNTY4YS00NmQ3LTkwNTItYThkMGVmMTVhNmQz&redirect_uri=https%3A%2F%2Fforms.office.com%2Flanding&msafed=0&x-client-SKU=ID_NET472&x-client-ver=6.14.1.0&sso_reload=true')

input_search=driver.find_element_by_css_selector('input[name="loginfmt"')
input_search.send_keys('hoan.dt204974@sis.hust.edu.vn')

driver.find_element_by_id('idSIButton9').click()

time.sleep(3)
input_search=driver.find_element_by_css_selector('input[name="Password"')
input_search.send_keys('031202008945')

driver.find_element_by_id('submitButton').click()
time.sleep(3)
driver.find_element_by_id('KmsiCheckboxField').click()
driver.find_element_by_id('idSIButton9').click()



