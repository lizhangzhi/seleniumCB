import unittest
from .driver import browser

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: myunit.py
@time: 2017/8/17 10:15
'''


class MyUnittest(unittest.TestCase):
	def setUp(self):
		self.driver = browser()
		self.driver.implicitly_wait(10)

	def tearDown(self):
		self.driver.quit()
