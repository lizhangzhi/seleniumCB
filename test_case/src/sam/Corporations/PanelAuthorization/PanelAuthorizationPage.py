from Util import *
import time
# -*- coding: utf-8 -*-
__author__ = 'lifangdong'
'''
@file: PanelAuthorizationPage.py
@time: 2018/4/10 14:45
'''


class PanelAuthorizationPage(BasePage):
    # for new group
    new_group_button = (By.XPATH, "//a[contains(@href,'corp/panelAuth/createPanelGroup')]")
    group_name_loc = (By.NAME, "pnlGrpName")
    group_name = "Sanity" + time.strftime('%d%H%M%S', time.localtime())
    user_list = (By.NAME, "nonSelectedUsers")
    add_user_button = (By.PARTIAL_LINK_TEXT, "Add Users")
    preview_button = (By.NAME, "submit_preview")
    submit_button = (By.NAME, "submit_submit")
    session_text_loc = (By.ID, 'msgBlockSuccess-successText')

    # for new profile
    new_profile_button = (By.XPATH, "//a[contains(@href,'corp/panelAuth/createProfile')]")
    profile_name_loc = (By.NAME, "profileName")
    profile_name = "Profile" + time.strftime('%Y%m%d%H%M%S', time.localtime())
    profile_description_loc = (By.NAME, "profileDesc")
    min_amount_loc = (By.NAME, "tiers[0].minAmount")
    max_amount_loc = (By.NAME, "tiers[0].maxAmount")
    group_level_loc = (By.NAME, "tiers[0].panels[0].groups[0]")

    def click_new_group_button(self):
        self.find_element(self.new_group_button, clickable=True).click()

    def set_values_group_name(self):
        self.send_keys(self.group_name_loc, self.group_name, True, True)

    def select_user(self):
        self.select_dropdown(self.user_list).select_by_index(3)

    def click_add_users_button(self):
        self.find_element(self.add_user_button, clickable=True).click()

    def click_preview_button(self):
        self.find_element(self.preview_button, clickable=True).click()

    def click_submit_button(self):
        self.find_element(self.submit_button, clickable=True).click()

    def get_session_text(self):
        return self.find_element(self.session_text_loc).text

    def click_new_profile_button(self):
        self.find_element(self.new_profile_button, clickable=True).click()

    def set_value_profile_name(self):
        self.send_keys(self.profile_name_loc, self.profile_name, True, True)

    def set_value_profile_description(self, value):
        self.send_keys(self.profile_description_loc, value, True, True)

    def set_value_min_amount(self, value):
        self.send_keys(self.min_amount_loc, value, True, True)

    def set_value_max_amount(self, value):
        self.send_keys(self.max_amount_loc, value, True, True)

    def select_group(self):
        self.select_dropdown(self.group_level_loc).select_by_value("1")
