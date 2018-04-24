import logging
from test_case.src.sam.SamPage import *
from .PanelAuthorizationPage import PanelAuthorizationPage

# -*- coding: utf-8 -*-
__author__ = 'janet'
'''
@file: PanelAuthorization_sta.py
@time: 2018/4/10 14:43
'''


class PanelAuthorizationTest(myunit.MyUnittest):

    def CreateGroup(self):
        login_page = LoginPage(self.driver)
        login_page.logincb(self.url, self.sam_login_id, "", login_sam=True)
        sam_page = SamPage(self.driver)
        sam_page.go_to_edit_corporation_page("DBSHK", "customerId", "HKP2A01")
        sam_page.click_pa_link()

        create_group_page = PanelAuthorizationPage(self.driver)
        create_group_page.click_new_group_button()
        create_group_page.set_values_group_name()
        create_group_page.select_user()
        create_group_page.click_add_users_button()
        create_group_page.click_preview_button()
        create_group_page.click_submit_button()
        self.success_message = create_group_page.get_session_text()

    def CreateProfile(self):
        login_page = LoginPage(self.driver)
        login_page.logincb(self.url, self.sam_login_id, "", login_sam=True)
        sam_page = SamPage(self.driver)
        sam_page.go_to_edit_corporation_page("DBSHK", "customerId", "HKP2A01")
        sam_page.click_pa_link()

        create_group_page = PanelAuthorizationPage(self.driver)
        create_group_page.click_new_profile_button()
        create_group_page.set_value_profile_name()
        create_group_page.set_value_profile_description("ProfileDescription")
        create_group_page.set_value_min_amount(0)
        create_group_page.set_value_max_amount(1)
        create_group_page.select_group()
        create_group_page.click_preview_button()
        create_group_page.click_submit_button()
        self.success_message = create_group_page.get_session_text()

    @log(logger=logging.getLogger(__name__))
    def test_1_CreateGroup(self):
        """在SAM>Panel Authorization下创建Group"""
        self.CreateGroup()
        function.take_screenshot(self.driver, '31_panel_authorization_create_group.jpg')
        self.assertIn('has been successfully created', self.success_message)

    @log(logger=logging.getLogger(__name__))
    def test_2_createProfile(self):
        """在SAM>Panel Authorization下创建Profile"""
        self.CreateProfile()
        function.take_screenshot(self.driver, '32_panel_authorization_create_profile.jpg')
        self.assertIn('has been successfully created', self.success_message)
