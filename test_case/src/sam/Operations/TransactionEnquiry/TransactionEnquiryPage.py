from Util import *
# -*- coding: utf-8 -*-
__author__ = 'janet'
'''
@file: TransactionEnquiryPage.py
@time: 2018/4/10 14:09
'''


class TransactionEnquiryPage(BasePage):
    # start date定位
    start_date_loc = (By.NAME, 'startDate')
    # search button定位
    search_button_loc = (By.NAME, 'submit_search')
    # reference link定位
    reference_link_loc = (By.XPATH, "//a[contains(@href,'/transactionenquiry/bom/transactionenquiry')]")
    # print 按钮定位
    print_button_loc = (By.PARTIAL_LINK_TEXT, 'Print-Friendly')
    session_text_loc = (By.CLASS_NAME, 'secthd')

    def enter_start_date(self, value):
        self.send_keys(self.start_date_loc, value, True, True)

    def click_search_button(self):
        self.find_element(self.search_button_loc, clickable=True).click()

    def click_reference_link(self):
        self.find_elements(self.reference_link_loc).pop(0).click()

    def click_print_button(self):
        self.find_element(self.print_button_loc, clickable=True).click()

    def get_session_text(self):
        return self.find_element(self.session_text_loc).text
