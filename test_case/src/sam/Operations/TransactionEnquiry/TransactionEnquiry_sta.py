import logging
from Util import *
from .TransactionEnquiryPage import TransactionEnquiryPage
# -*- coding: utf-8 -*-
__author__ = 'janet'
'''
@file: TransactionEnquiry_sta.py
@time: 2018/4/10 14:09
'''


class TransactionEnquiryTest(myunit.MyUnittest):

    def transaction_enquiry(self):
        login_page = LoginPage(self.driver)
        login_page.logincb(self.url, self.sam_login_id, "", login_sam=True)

        transaction_enquiry_page = TransactionEnquiryPage(self.driver)
        transaction_enquiry_page.open_menu("OPERATIONS", "TRANSACTION ENQUIRY")
        transaction_enquiry_page = TransactionEnquiryPage(self.driver)
        transaction_enquiry_page.enter_start_date("01-Apr-2018")
        transaction_enquiry_page.click_search_button()
        transaction_enquiry_page.click_reference_link()
        transaction_enquiry_page.click_print_button()
        self.success_message = transaction_enquiry_page.get_session_text()

    @log(logger=logging.getLogger(__name__))
    def test_transaction_enquiry(self):
        """在SAM>OPERATIONS>TRANSACTION ENQUIRY页面查看数据是否正常显示"""
        self.transaction_enquiry()
        function.take_screenshot(self.driver, '33_transaction_enquiry.jpg')
        self.assertIn('Transaction Information', self.success_message)
