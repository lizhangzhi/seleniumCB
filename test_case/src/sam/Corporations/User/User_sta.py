import logging
from test_case.src.sam.SamPage import *
from test_case.src.sam.Corporations.User.UserPage import UserPage
# -*- coding: utf-8 -*-
__author__ = 'janet'
'''
@file: User_sta.py
@time: 2018/4/10 14:09
'''


class UserTest(myunit.MyUnittest):

    def CreateUser(self):
        login_page = LoginPage(self.driver)
        login_page.logincb(self.url, self.sam_login_id, "", login_sam=True)
        sam_page = SamPage(self.driver)
        sam_page.go_to_edit_corporation_page("DBSSG", "customerId", "SG2BFE1")
        sam_page.click_user_tab()

        create_user_page = UserPage(self.driver)
        create_user_page.click_new_user_link()
        create_user_page.set_value_userid()
        create_user_page.set_value_username()
        create_user_page.set_value_email()
        create_user_page.click_preview_button()
        create_user_page.click_submit_button()
        # create_user_page.function_services_link()
        self.success_message = create_user_page.get_session_text()
        self.user_name = self.success_message.split()[3]

    def ApprovalUser(self):
        login_page = LoginPage(self.driver)
        login_page.logincb(self.url, self.sam_login_approver, "", login_sam=True)
        sam_page = SamPage(self.driver)
        sam_page.go_to_edit_corporation_page("DBSSG", "customerId", "SG2BFE1")
        sam_page.click_user_tab()

        approval_user_page = UserPage(self.driver)
        approval_user_page.set_value_search_by("familyName")
        approval_user_page.set_value_search_for(self.user_name)
        approval_user_page.click_search_button()
        approval_user_page.click_approval_status_link()
        approval_user_page.click_approval_button()
        self.success_message = approval_user_page.get_session_text()

    @log(logger=logging.getLogger(__name__))
    def test_1_CreateUser(self):
        """测试SAM端能Create User"""
        self.CreateUser()
        function.take_screenshot(self.driver, '29_SAM_Create_User.jpg')
        self.assertIn('has been successfully submitted', self.success_message)

    @log(logger=logging.getLogger(__name__))
    def test_2_ApprovalUser(self):
        """测试SAM端能Approve User"""
        self.CreateUser()
        self.ApprovalUser()
        function.take_screenshot(self.driver, '30_SAM_Approve_User.jpg')
        self.assertIn('have been approved', self.success_message)
