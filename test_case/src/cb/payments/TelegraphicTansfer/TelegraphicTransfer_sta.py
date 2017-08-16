import unittest, sys
from selenium import webdriver
from page_object.loginPage import Login

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: TelegraphicTransfer_sta.py
@time: 2017/8/15 15:24
'''


class TelegraphicTransferTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox(executable_path='./../drivers/geckodriver')
		Login(self.driver).logincb()

	def tearDown(self):
		self.driver.quit()

	def test_createTT(self):
		self.assertEqual(3, 3)

if __name__ == '__main__':
	unittest.main()
