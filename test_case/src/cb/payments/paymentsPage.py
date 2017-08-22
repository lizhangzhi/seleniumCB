from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
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
	fromaccount_loc = (By.ID, 'fromParty')
	paymentcurrency_loc = (By.ID, 'paymentCurrency_currencyCode')
	amount_loc = (By.ID, 'amount_value_control')
	beneficiary_loc = (By.ID, 'toParty')

	def open_paymentmenulist(self):

		WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located(self.paymentMenu_loc))
		self.script("document.getElementById('pmt').parentElement.children[1]."
							+ "style='opacity:1; margin-left: 0; width:320px;'")
		sleep(3)

	def to_telegraphictransfer(self):

		telegraphic_transfer_link = WebDriverWait(self.driver, 30, 1)\
			.until(EC.element_to_be_clickable(self.telegraphicTransferLink_loc))
		telegraphic_transfer_link.click()

	def select_fromaccount(self):

		WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located(self.fromaccount_loc))
		fromaccount_selector = Select(self.driver.find_element_by_id('fromParty'))
		fromaccount_selector.select_by_visible_text('LEONA ALBRECHT - 0018001843 - SGD')

	def select_paymentcurrency(self):

		WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located(self.paymentcurrency_loc))
		paymentcurrency_select = Select(self.driver.find_element_by_id('paymentCurrency_currencyCode'))
		paymentcurrency_select.select_by_value('SGD')

	def enter_amount(self, value):

		WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located(self.amount_loc))
		amount = WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located(self.amount_loc))
		amount.send_keys(value)

	def select_beneficiary(self):

		WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located(self.beneficiary_loc))
		beneficiary_selector = Select(self.driver.find_element_by_id('toParty'))
		beneficiary_selector.select_by_index(2)
		sleep(5)
