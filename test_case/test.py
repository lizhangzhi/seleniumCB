# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path='./../drivers/geckodriver')
driver.get("https://192.168.0.245:9444/s1gcb/logon/loginSSO")
loginID = WebDriverWait(driver, 30, 1).until(EC.visibility_of_element_located((By.NAME, "ssoUserid")))
loginID.send_keys("SG2BFE1S04")
companyID = WebDriverWait(driver, 30, 1).until(EC.visibility_of_element_located((By.NAME, "ssoCompanyID")))
companyID.send_keys("SG2BFE1")
loginBtn = WebDriverWait(driver, 30, 1).until(EC.element_to_be_clickable((By.NAME, "submit_sbuserLogin")))
loginBtn.click()
nextBtn = WebDriverWait(driver, 30, 1).until(EC.element_to_be_clickable((By.ID, "previewButton_Link")))
nextBtn.click()
sleep(5)
WebDriverWait(driver, 30, 1).until(EC.visibility_of_element_located((By.ID, "pmt")))
driver.execute_script("document.getElementById('pmt').parentElement.children[1]."
                      + "style='opacity:1; margin-left: 0; width:320px;'")
ttlink = WebDriverWait(driver, 30, 1).until(EC.element_to_be_clickable((By.LINK_TEXT, "Telegraphic Transfer")))
ttlink.click()
WebDriverWait(driver, 30, 1).until(EC.visibility_of_element_located((By.ID, 'fromParty')))
fromaccount_selector = Select(driver.find_element_by_id('fromParty'))
fromaccount_selector.select_by_visible_text('LEONA ALBRECHT - 0018001843 - SGD')
sleep(1)
paymentcurrency_select = Select(driver.find_element_by_id('paymentCurrency_currencyCode'))
paymentcurrency_select.select_by_value('SGD')
amount = WebDriverWait(driver, 30, 1).until(EC.visibility_of_element_located((By.ID, 'amount_value_control')))
amount.send_keys('10')
existingbeneficiary_selector = Select(driver.find_element_by_id('toParty'))
existingbeneficiary_selector.select_by_index(2)
sleep(5)
# previewBtn = WebDriverWait(driver, 30, 1).until(EC.element_to_be_clickable((By.ID, 'previewButton_Link')))
# previewBtn.click()
previewBtn = driver.find_element_by_id('previewButton_Link')
driver.execute_script("arguments[0].click();", previewBtn.getWebElement())
# previewBtn.click()
sleep(15)
# WebDriverWait(driver, 30, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.sectionBoxTitle'), 'Preview Telegraphic Transfer'))
# submitBtn = WebDriverWait(driver, 30, 1).until(EC.element_to_be_clickable((By.ID, 'submitButton_Link')))
# submitBtn.click()
# sleep(10)
driver.close()