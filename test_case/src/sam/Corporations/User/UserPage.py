from Util import *
import time

# -*- coding: utf-8 -*-
__author__ = 'lifangdong'
'''
@file: PanelAuthorizationPage.py
@time: 2018/4/10 14:45
'''


class UserPage(BasePage):
    # user tab下new user link定位
    new_user_link = (By.XPATH, "//a[contains(@href,'corp/corporationEdit/addUser')]")
    # new user页面user id定位
    userid_loc = (By.NAME, "loginId")
    # new user页面user name定位
    username_loc = (By.NAME, "lastName")
    # new user页面user email定位
    email_loc = (By.NAME, "email")
    # new user页面Preview按钮定位
    preview_button = (By.NAME, "submit_preview")
    # new user页面Submit按钮定位
    submit_user_button = (By.NAME, "submit_submit")
    session_text_loc = (By.ID, 'msgBlockSuccess-successText')
    # new user页面的user id，user name，email通过系统时间命名
    userid = time.strftime('%Y%m%d%H%M%S', time.localtime())
    user_name = userid + "Name"
    user_email = userid + "@pactera.com"
    # user level Account services link定位
    account_services_link = (By.XPATH, "//a[contains(@href,'corp/entitlement/entitlementAccountList')]")
    # user level Function services link定位
    function_services_link = (By.XPATH, "//a[contains(@href,'corp/UserFunctionalAccess')]")

    # user tab下检索user
    search_by = (By.NAME, "columnName")
    search_value = (By.NAME, "columnValue")
    search_button = (By.NAME, "submit")
    # user tab下approval status link定位
    approval_status_link = (By.XPATH, "//a[contains(@href,'corp/corporationEditUser/approve')]")
    # Approval button定位
    approval_user_button = (By.NAME, "submit_approve")

    def click_new_user_link(self):
        self.find_element(self.new_user_link, clickable=True).click()

    def set_value_userid(self):
        self.send_keys(self.userid_loc, self.userid, True, True)

    def set_value_username(self):
        self.send_keys(self.username_loc, self.user_name, True, True)

    def set_value_email(self):
        self.send_keys(self.email_loc, self.user_email, True, True)

    def click_preview_button(self):
        self.find_element(self.preview_button, clickable=True).click()

    def click_submit_button(self):
        self.find_element(self.submit_user_button, clickable=True).click()

    def click_function_services_link(self):
        self.find_element(self.function_services_link, clickable=True).click()

    def get_session_text(self):
        return self.find_element(self.session_text_loc).text

    def set_value_search_by(self, value):
        self.select_dropdown(self.search_by).select_by_value(value)

    def set_value_search_for(self, value):
        self.send_keys(self.search_value, value, True, True)

    def click_search_button(self):
        self.find_element(self.search_button, clickable=True).click()

    def click_approval_status_link(self):
        self.find_element(self.approval_status_link, clickable=True).click()

    def click_approval_button(self):
        self.find_element(self.approval_user_button, clickable=True).click()
