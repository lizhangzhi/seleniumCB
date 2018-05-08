# from time import sleep
import logging
from Util import *
# from .AccountTransferPage import AccountTransferPage
from test_case.src.PageFactory import PageFactory
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: AccountTransfer_sta.py
@time: 2018/4/3 16:17
'''


class AccountTransferTest(MyUnittest):

    # def create_account_transfer(self):
    #     account_transfer = AccountTransferPage(self.driver)
    #     account_transfer.login_cb(self.url, "TWP2A01M01", "TWP2A01")
    #     account_transfer.open_menu("Payments", "Account Transfer")
    #     account_transfer.select_from_account("RISTORISTO - 036008014561 - USD")
    #     account_transfer.enter_amount("10")
    #     account_transfer.select_beneficiary(3)
    #     account_transfer.scroll_up_and_down(0, 400)
    #     account_transfer.select_outward_remittance(3)
    #     account_transfer.select_purpose_code(AccountTransferPage.purpose_code_loc,
    #                                          AccountTransferPage.purpose_code_filter_loc,
    #                                          "111",
    #                                          AccountTransferPage.purpose_code_filter_value_loc)
    #     account_transfer.scroll_up_and_down(0, 1000)
    #     account_transfer.click_preview_button()
    #     sleep(3)
    #     account_transfer.scroll_up_and_down(0, 1000)
    #     account_transfer.click_submit_button()
    #     self.success_message = account_transfer.get_success_message()
    #     self.instruction_id = account_transfer.get_success_message().split()[2]

    @log(logger=logging.getLogger(__name__))
    def test_1_CBCFX_create_ACT(self):
        """通过判断payment date原本的输入框是不可见的，验证CBCFX是否生效"""
        # self.create_account_transfer()
        try:
            account_transfer = PageFactory.get_account_transfer_page_instance(self.driver)
            account_transfer.login_cb(self.url, "TWP2A01M01", "TWP2A01")
            account_transfer.open_menu("Payments", "Account Transfer")
            account_transfer.select_from_account(account_number="RISTORISTO - 036008014561 - USD")
            function.take_screenshot(self.driver, '19_CBCFX_account_transfer.jpg')
            # self.assertIn('has been created successfully', self.success_message)
            self.assertFalse(account_transfer.payment_date_display())
        finally:
            PageFactory.clean_page_instance()
