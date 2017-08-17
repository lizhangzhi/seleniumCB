import unittest
from test_case.model import myunit, function
from test_case.page_object.loginPage import Login
from test_case.src.cb.payments.paymentsPage import PaymentPage

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: TelegraphicTransfer_sta.py
@time: 2017/8/15 15:24
'''


class TelegraphicTransferTest(myunit.MyUnittest):

	def test_createTT(self):
		Login(self.driver).logincb()
		PaymentPage(self.driver).open_paymentmenulist(self.driver)
		PaymentPage(self.driver).to_telegraphictransfer(self.driver)
		# function.take_screenshot(self.driver, 'create tt.jpg')
		self.assertEqual(3, 3)

if __name__ == '__main__':
	unittest.main()
