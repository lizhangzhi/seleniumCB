from selenium.webdriver.common.by import By
from .base import Page

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: loginPage.py
@time: 2017/8/14 15:42
'''


class Login(Page):
	url = ''

	# locator
	loginId_loc = (By.ID, "ssoUserid")
	companyId_loc = (By.ID, "ssoCompanyID")
	cbBtn_loc = (By.NAME, "submit_sbuserLogin")
	nextBtn_loc = (By.ID, "previewButton_Link")

	# type login id
	def type_loginid(self, loginid):
		self.find_element(*self.loginId_loc).send_keys(loginid)

	# type company id
	def type_companyid(self, companyid):
		self.find_element(*self.companyId_loc).send_keys(companyid)

	# click CB button
	def click_cbbutton(self):
		self.find_element(*self.cbBtn_loc).click()

	# click next button
	def click_nextbutton(self):
		self.find_element(*self.nextBtn_loc).click()

	# login CB side
	def logincb(self, loginid='SG2BFE1S01', companyid='SG2BFE1'):
		self.open()
		self.type_loginid(loginid)
		self.type_companyid(companyid)
		self.click_cbbutton()
		self.click_nextbutton()
