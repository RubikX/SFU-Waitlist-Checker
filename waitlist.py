from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("https://www.go.sfu.ca")

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

driver.implicitly_wait(10)

username = driver.find_element_by_id('user')
password = driver.find_element_by_id('pwd')

username.clear()
password.clear()

username.send_keys(username_input)
password.send_keys(password_input)

driver.find_element_by_name('Submit').click()

drop_down = driver.find_element_by_id('DERIVED_SSS_SCL_SSS_MORE_ACADEMICS')
element = driver.find_element_by_id('DERIVED_SSS_SCL_SSS_GO_1');
actions = ActionChains(driver)
actions.move_to_element(drop_down)
actions.click(drop_down)
select_box = Select(drop_down)

try:
	actions.move_to_element(select_box.select_by_value('1002'))
	actions.click(select_box)
	actions.perform()

except AttributeError:
	pass

actions.move_to_element(element)
actions.click(element)
actions.perform()

driver.implicitly_wait(10)
iframe = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.frame(iframe)

waitlists = []

for i in range(0,10):
	try:
		waitlists.append(int(driver.find_element_by_css_selector('#DERIVED_SSE_DSP_WAITLIST_POS\${}'.format(str(i))).text))

	except NoSuchElementException:
		continue



