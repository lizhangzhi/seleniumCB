import logging
from time import sleep
from Util import *
from test_case.src.PageFactory import PageFactory
from .BillPaymentPage import BillPaymentPage
from test_case.src.cb.Approvals.OfflineApprovalsPage import OfflineApprovalsPage
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: BillPayment_sta.py
@time: 2018/3/29 17:04
'''


class BillPaymentTest(MyUnittest):

    def create_bill_payment(self):
        """创建一条bill payment"""
        bill_payment = PageFactory.get_bill_payment_page_instance(self.driver)
        bill_payment.login_cb(self.url, self.login_id, self.company_id)
        bill_payment.open_menu("Payments", "Bill Payment")
        bill_payment.select_billing_organisation(2)
        bill_payment.select_from_account(from_account_loc=BillPaymentPage.from_account_loc,
                                         account_number="LEONA ALBRECHT - 0018001843 - SGD")
        bill_payment.enter_bill_reference("1234567890")
        bill_payment.enter_amount(amount_loc=BillPaymentPage.amount_loc, value="10")
        bill_payment.click_preview_button()
        bill_payment.click_submit_button()
        self.instruction_id = bill_payment.get_success_message().split()[2]
        sleep(3)

    @log(logger=logging.getLogger(__name__))
    def test_1_offline_approve_bill_payment(self):
        """offline approve list在view页面approve bill payment"""
        try:
            self.create_bill_payment()
            bill_payment = PageFactory.get_bill_payment_page_instance(self.driver)
            bill_payment.open_menu("Payments", "Offline Approvals")
            bill_payment.click_tab(OfflineApprovalsPage.list_per_transaction_tab_loc)
            bill_payment.enter_reference(OfflineApprovalsPage.reference_loc, self.instruction_id)
            bill_payment.click_go_button(OfflineApprovalsPage.offline_approval_go_button_loc)
            bill_payment.click_reference_link(self.instruction_id)
            bill_payment.enter_approve_response("approve")
            bill_payment.select_approver(OfflineApprovalsPage.approver_dropdown_loc, "SG2BFE1S01@SG2BFE1")
            bill_payment.click_approve_button(BillPaymentPage.approve_payment_button_loc)
            # bill_payment.wait_page_load(OfflineApprovalsPage.title_loc)
            self.success_message = bill_payment.get_success_message()
            function.take_screenshot(self.driver, '24_offline_approve_bill_payment.jpg')
            self.assertTrue(self.success_message)
        finally:
            PageFactory.clean_page_instance()
