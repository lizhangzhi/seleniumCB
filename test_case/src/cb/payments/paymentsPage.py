from selenium.webdriver.common.by import By
from test_case.page_object.basePage import BasePage
from time import sleep
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: paymentsPage.py
@time: 2017/8/17 15:46
编写payment菜单下页面的通用操作方法
'''


class PaymentPage(BasePage):

	paymentMenu_loc = (By.ID, 'pmt')
	telegraphicTransferLink_loc = (By.LINK_TEXT, 'Telegraphic Transfer')
	fromaccount_loc = (By.ID, 'fromParty')
	paymentcurrency_loc = (By.ID, 'paymentCurrency_currencyCode')
	amount_loc = (By.ID, 'amount_value_control')
	beneficiary_loc = (By.ID, 'toParty')

	def open_payment_menu(self):
		self.find_element(self.paymentMenu_loc)
		self.script("document.getElementById('pmt').parentElement.children[1]."
							+ "style='opacity:1; margin-left: 0; width:320px;'")
		sleep(3)

	def to_telegraphic_transfer(self):
		self.find_element(self.telegraphicTransferLink_loc).click()

	def select_from_account(self):
		self.select_dropdown(self.fromaccount_loc).select_by_visible_text('LEONA ALBRECHT - 0018001843 - SGD')

	def select_payment_currency(self):
		self.select_dropdown(self.paymentcurrency_loc).select_by_value('SGD')

	def enter_amount(self, value):
		self.find_element(self.amount_loc).send_keys(value)

	def select_beneficiary(self):
		self.select_dropdown(self.beneficiary_loc).select_by_index(2)
		sleep(3)
