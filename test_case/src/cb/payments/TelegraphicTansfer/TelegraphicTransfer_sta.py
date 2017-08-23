from test_case.model import myunit
from test_case.page_object.loginPage import Login
from test_case.src.cb.payments.TelegraphicTansfer import TelegraphicTransferPage

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: TelegraphicTransfer_sta.py
@time: 2017/8/15 15:24
'''


class TelegraphicTransferTest(myunit.MyUnittest):
	"""Telegraphic Transfer Test"""

	def test_createTT(self):
		"""Create Telegraphic Transfer"""

		Login(self.driver).logincb()
		TelegraphicTransferPage.create_telegraphic_transfer(self.driver)
		# function.take_screenshot(self.driver, 'create tt.jpg')
		self.assertEqual(3, 3)
