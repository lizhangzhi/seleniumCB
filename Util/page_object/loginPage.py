from selenium.webdriver.common.by import By
from .basePage import BasePage
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: loginPage.py
@time: 2017/8/14 15:42
CB登陆页面基本操作方法
'''


class LoginPage(BasePage):

    loginId_loc = (By.NAME, "ssoUserid")
    companyId_loc = (By.NAME, "ssoCompanyID")
    cbBtn_loc = (By.NAME, "submit_sbuserLogin")
    nextBtn_loc = (By.ID, "previewButton_Link")

    def type_loginid(self, loginid):
        self.find_element(self.loginId_loc).send_keys(loginid)

    def type_companyid(self, companyid):
        self.find_element(self.companyId_loc).send_keys(companyid)

    def click_cbbutton(self):
        self.find_element(self.cbBtn_loc).click()

    def click_nextbutton(self):
        self.find_element(self.nextBtn_loc).click()

    def logincb(self, url, loginid, companyid):
        self.open(url)
        self.type_loginid(loginid)
        self.type_companyid(companyid)
        self.click_cbbutton()
        self.click_nextbutton()
