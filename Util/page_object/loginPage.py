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
    samBtn_loc = (By.NAME, "submit_csrLogin")

    dashboard_welcome_loc = (By.XPATH, "//*[@class='container-fluid']/div/div/div/span[1]")

    def type_login_id(self, loginid):
        self.find_element(self.loginId_loc).send_keys(loginid)

    def type_company_id(self, companyid):
        self.find_element(self.companyId_loc).send_keys(companyid)

    def click_cb_button(self):
        self.find_element(self.cbBtn_loc, clickable=True).click()

    def click_next_button(self):
        self.find_element(self.nextBtn_loc, clickable=True).click()

    def wait_dashboard_load(self):
        self.find_element(self.dashboard_welcome_loc)

    def click_sambutton(self):
        self.find_element(self.samBtn_loc).click()

    def logincb(self, url, loginid, companyid, login_sam=False):
        """登陆函数
        login_sam: 默认为False代表默认登陆CB端，如果设为True则登陆SAM端
        """
        self.open(url)
        self.type_login_id(loginid)
        self.type_company_id(companyid)
        if login_sam:
            self.click_sambutton()
        else:
            self.click_cb_button()
            self.click_next_button()
            self.wait_dashboard_load()
