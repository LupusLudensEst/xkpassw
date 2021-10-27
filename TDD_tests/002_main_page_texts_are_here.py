from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
XKP_TEXT_IS_HERE = (By.ID, "donate_container")
CRDTS_ONE_HERE = (By.XPATH, "(//a[@target='_blank'])[6]")
URL_BARTB_HERE = (By.XPATH, "(//a[@target='_blank'])[4]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://xkpasswd.net/s/' )

# 2. Verify text "XKPasswd - A Secure Memorable Password Generator" is here
expected_text = "This service is provided entirely for free and without ads, but the server is not free to run. Please consider making a small contribution towards those costs."
actual_text = wait.until(EC.visibility_of_element_located(XKP_TEXT_IS_HERE)).text
print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}"\n')

# 3. Verify text "Bart Busschots" is here
expected_text = "Bart Busschots"
actual_text = wait.until(EC.visibility_of_element_located(CRDTS_ONE_HERE)).text
print(f'Actual text: "{actual_text}"')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}"\n')

# 4. Verify URL "www.bartb.ie/xkpasswd" is here
expected_text = "www.bartb.ie/xkpasswd"
actual_text = wait.until(EC.visibility_of_element_located(URL_BARTB_HERE)).text
print(f'Actual text: "{actual_text}"')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}"\n')

driver.close()

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()
