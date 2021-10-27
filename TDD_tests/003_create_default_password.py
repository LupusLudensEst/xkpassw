from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
APPLD_BTN = (By.XPATH, "//input[@value='APPLEID']")
DFLT_BTN = (By.XPATH, "//input[@value='DEFAULT']")
NTLM_BTN = (By.XPATH, "//input[@value='NTLM']")
SECURITYQ_BTN = (By.XPATH, "//input[@value='SECURITYQ']")
WEB16_BTN = (By.XPATH, "//input[@value='WEB16']")
WEB32_BTN = (By.XPATH, "//input[@value='WEB32']")
WIFI_BTN = (By.XPATH, "//input[@value='WIFI']")
XKCD_BTN = (By.XPATH, "//input[@value='XKCD']")
GNRT_PSWDS_BTN = (By.ID, "generate_password_btn")
PSWRDS_FLD = (By.XPATH, "//textarea[@rows='3']")
STRNGT_FLD = (By.XPATH, "(//span[@class='losenge good'])[1]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://xkpasswd.net/s/' )

# 2. Click on APPLEID button
driver.find_element(*APPLD_BTN).click()

# 3. Click on DEFAULT button
driver.find_element(*DFLT_BTN).click()

# 4. Click on NTLM button
driver.find_element(*NTLM_BTN).click()

# 4. Click on SECURITYQ button
driver.find_element(*SECURITYQ_BTN).click()

# 5. Click on WEB16 button
driver.find_element(*WEB16_BTN).click()

# 6. Click on WEB32 button
driver.find_element(*WEB32_BTN).click()

# 7. Click on WIFIbutton
driver.find_element(*WIFI_BTN).click()

# 7. Click on XKCD button
driver.find_element(*XKCD_BTN).click()

# 8. Click on Generate 3 Passwords button
target = wait.until(EC.element_to_be_clickable(GNRT_PSWDS_BTN))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click(on_element = target)
actions.perform()

# 9. Verify Passwords Field is not empty and has a content
expected_substring = '3'
assert expected_substring in driver.find_element(*PSWRDS_FLD).get_attribute('rows'), \
            f"Expected PIN to have '{expected_substring}' in its rows."
attribute_value = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "generated_password"))).get_attribute("rows")
print(f'Attribute rows value: {attribute_value}')
expected_substring = '64'
assert expected_substring in driver.find_element(*PSWRDS_FLD).get_attribute('cols'), \
            f"Expected PIN to have '{expected_substring}' in its src."
attribute_value = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "generated_password"))).get_attribute("cols")
print(f'Attribute cols value: {attribute_value}')

# 10. Verify STRENGTH Field is not empty
actual_text = (wait.until(EC.presence_of_element_located(STRNGT_FLD)).text)
print(f'{actual_text} is of "{type(actual_text)}"')
if len(actual_text) != 0:
    print(f"Strength field is not empty, and of {type(actual_text)}")
else:
    print(f"Check Strength field of {type(actual_text)}")

driver.close()

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()





