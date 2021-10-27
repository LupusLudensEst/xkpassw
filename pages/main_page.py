from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from Screenshot import Screenshot_Clipping
import time

# Locators
URL_FLD = (By.XPATH, "//input[@inputmode='search']")
DMN_MN_ONE = (By.CLASS_NAME, "multiselect__single")
DMN_MN_TWO = (By.CSS_SELECTOR, "svg.target__icon.icon")
SRCH_BTN = (By.XPATH, "//button[@name='enter_short']") #(By.XPATH, "//button[@class='button search__btn button--color-blue button--v-default button--size-lg']")
TITLE = (By.XPATH, "(//div[@class='line-clamp-cell'])[1]")
ALEXA_RANK = (By.XPATH, "(//div[@class='cell table__td'])[3]")
REGISTAR = (By.XPATH, "(//div[@class='cell table__td'])[4]")
ISSUER_ORG = (By.XPATH, "(//div[@class='cell table__td'])[5]")
XKP_TEXT_IS_HERE = (By.ID, "donate_container")
CRDTS_ONE_HERE = (By.XPATH, "(//a[@target='_blank'])[6]")
URL_BARTB_HERE = (By.XPATH, "(//a[@target='_blank'])[4]")
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

class MainPage(Page):

    # 001 Vulnerability test
    # Login https://spyse.com/
    def lgn_spyse(self, spyse):
        self.driver.get(spyse)

    # Input https://xkpasswd.net/s/ to search field
    def inpt_our_url(self, url):
        # 2. Choose Domain from drop-dawn menu
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(DMN_MN_ONE)).click()
        target = wait.until(EC.element_to_be_clickable(DMN_MN_TWO))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(on_element=target)
        actions.perform()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(URL_FLD)).clear()
        wait.until(EC.presence_of_element_located(URL_FLD)).send_keys(url)

    # Click on Search button
    def clck_srch_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(SRCH_BTN)).click()

    # Find security score, critical risk, medium risk, elevated risk, issuer DN
    def fnd_all_data(self):
        wait = WebDriverWait(self.driver, 10)
        title = wait.until(EC.visibility_of_element_located(TITLE)).text.lower()
        alexa_rank = wait.until(EC.visibility_of_element_located(ALEXA_RANK)).text.lower()
        registar = wait.until(EC.visibility_of_element_located(REGISTAR)).text.lower()
        issuer_org = wait.until(EC.visibility_of_element_located(ISSUER_ORG)).text.lower()
        print(f'Security score: "{title}";\nCritical risk: "{alexa_rank}";\nMedium risk: "{registar}"\n'
              f'Elevated risk: "{issuer_org}"')

    # Make a screenshot of the whole page
    def mk_scrnsht(self):
        ob = Screenshot_Clipping.Screenshot()
        url = self.driver.current_url
        today = time.strftime(f'%Y_%m_%d')
        now = time.strftime(f'%H_%M_%S')
        file_name = 'vulnerability_' + today + '_' + now + '.jpg'
        img_url = ob.full_Screenshot(self.driver,
                                     save_path=r'C:\Everything\IT\Testing\Automation_08_09_2019\xkpassw\screen_shots',
                                     image_name=file_name)
        print(img_url)

    # End of the above code

    # 002 Verify texts(see steps below are here)
    def vrfy_this_srvs_here(self, txt):
        # Verify text "XKPasswd - A Secure Memorable Password Generator" is here
        wait = WebDriverWait(self.driver, 10)
        expected_text = txt
        actual_text = wait.until(EC.visibility_of_element_located(XKP_TEXT_IS_HERE)).text
        print(f'Actual text: "{actual_text}"')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}"\n')

        # Verify text "Bart Busschots" is here
    def vrfy_brt_bssch_here(self, txt):
        wait = WebDriverWait(self.driver, 10)
        expected_text = txt
        actual_text = wait.until(EC.visibility_of_element_located(CRDTS_ONE_HERE)).text
        print(f'Actual text: "{actual_text}"')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}"\n')

        # Verify URL "www.bartb.ie/xkpasswd" is here
    def vrfy_url_brtb_here(self, txt):
        wait = WebDriverWait(self.driver, 10)
        expected_text = txt
        actual_text = wait.until(EC.visibility_of_element_located(URL_BARTB_HERE)).text
        print(f'Actual text: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}"\n')

    # End of the above code

    # 003 Generate password with default options
    # Click on all 7 buttons APPLEID, DEFAULT, NTLM, SECURITYQ, WEB16, WEB32, WIFI
    def clck_svn_btns(self):
        #  Click on APPLEID button
        self.driver.find_element(*APPLD_BTN).click()

        # Click on DEFAULT button
        self.driver.find_element(*DFLT_BTN).click()

        # Click on NTLM button
        self.driver.find_element(*NTLM_BTN).click()

        # Click on SECURITYQ button
        self.driver.find_element(*SECURITYQ_BTN).click()

        # Click on WEB16 button
        self.driver.find_element(*WEB16_BTN).click()

        # Click on WEB32 button
        self.driver.find_element(*WEB32_BTN).click()

        # Click on WIFIbutton
        self.driver.find_element(*WIFI_BTN).click()

        # Click on XKCD button
        self.driver.find_element(*XKCD_BTN).click()

         # Click on Generate 3 Passwords button
    def clck_thr_pswd_btn(self):
        wait = WebDriverWait(self.driver, 10)
        target = wait.until(EC.element_to_be_clickable(GNRT_PSWDS_BTN))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click(on_element=target)
        actions.perform()

        # Verify Passwords Field is not empty and has a content
    def pswd_fld_hs_cntnt(self, rows, cols):
        expected_substring = rows
        assert expected_substring in self.driver.find_element(*PSWRDS_FLD).get_attribute('rows'), \
            f"Expected PIN to have '{expected_substring}' in its src."
        attribute_value = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "generated_password"))).get_attribute("rows")
        print(f'Attribute rows value: {attribute_value}')
        expected_substring = cols
        assert expected_substring in self.driver.find_element(*PSWRDS_FLD).get_attribute('cols'), \
            f"Expected PIN to have '{expected_substring}' in its src."
        attribute_value = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "generated_password"))).get_attribute("cols")
        print(f'Attribute cols value: {attribute_value}')

        # Verify STRENGTH Field is not empty
    def strngth_fld_hs_cntnt(self, strngth_pswd):
        wait = WebDriverWait(self.driver, 10)
        expected_text = strngth_pswd
        actual_text = (wait.until(EC.presence_of_element_located(STRNGT_FLD)).text)
        assert  expected_text in actual_text
        print(f'Expected text: "{strngth_pswd}"; Actual text: "{actual_text}" is of "{type(actual_text)}"')
        if len(actual_text) != 0:
            print(f"Strength field is not empty, and of {type(actual_text)}")
        else:
            print(f"Check Strength field of {type(actual_text)}")

    # End of the above code


