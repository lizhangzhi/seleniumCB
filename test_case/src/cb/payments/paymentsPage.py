from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_case.page_object.base import Page
from time import sleep
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: paymentsPage.py
@time: 2017/8/17 15:46
'''


class PaymentPage(Page):

	# locator
	paymentMenu_loc = (By.ID, 'pmt')
	telegraphicTransferLink_loc = (By.LINK_TEXT, 'Telegraphic Transfer')

	def open_paymentmenulist(self, driver):

		WebDriverWait(driver, 30, 1).until(EC.visibility_of_element_located(self.paymentMenu_loc))
		self.script("document.getElementById('pmt').parentElement.children[1]."
							+ "style='opacity:1; margin-left: 0; width:320px;'")
		sleep(10)

	def to_telegraphictransfer(self, driver):

		telegraphic_transfer_link = WebDriverWait(driver, 30, 1)\
			.until(EC.element_to_be_clickable(self.telegraphicTransferLink_loc))
		telegraphic_transfer_link.click()
