from test_case.model import myunit
from test_case.page_object.loginPage import LoginPage
from test_case.src.cb.payments.paymentsPage import PaymentPage

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: TelegraphicTransfer_sta.py
@time: 2017/8/15 15:24
'''


class TelegraphicTransferTest(myunit.MyUnittest):

	def createTT(self):

		login = LoginPage(self.driver)
		login.logincb(self.url, self.login_id, self.company_id)
		telegraphic_transfer = PaymentPage(self.driver)
		telegraphic_transfer.open_payment_menu()
		telegraphic_transfer.to_telegraphic_transfer()
		telegraphic_transfer.select_from_account()
		telegraphic_transfer.select_payment_currency()
		telegraphic_transfer.enter_amount('10')
		telegraphic_transfer.select_beneficiary()
		# telegraphic_transfer.click_preview_button()
		# telegraphic_transfer.click_submit_button()

	def test_createTT(self):
		# function.take_screenshot(self.driver, 'create tt.jpg')
		self.createTT()
		self.assertEqual(3, 3)
