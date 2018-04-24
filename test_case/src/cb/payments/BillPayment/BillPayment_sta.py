import logging
from time import sleep
from Util import *
from test_case.src.PageFactory import PageFactory
from .BillPaymentPage import BillPaymentPage
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
        bill_payment.select_from_account("LEONA ALBRECHT - 0018001843 - SGD")
        bill_payment.enter_bill_reference("1234567890")
        bill_payment.enter_amount("10")
        bill_payment.click_preview_button()
        bill_payment.click_submit_button()
        self.instruction_id = bill_payment.get_success_message().split()[2]
        sleep(3)

    @log(logger=logging.getLogger(__name__))
    def test_1_offline_approve_bill_payment(self):
        """offline approve list在view页面approve bill payment"""
        self.create_bill_payment()
        bill_payment = PageFactory.get_bill_payment_page_instance(self.driver)
        bill_payment.open_menu("Payments", "Offline Approvals")
        bill_payment.click_tab(BillPaymentPage.list_per_transaction_tab_loc)
        bill_payment.enter_reference(BillPaymentPage.reference_loc, self.instruction_id)
        bill_payment.click_go_button(BillPaymentPage.offline_approval_go_button_loc)
        bill_payment.click_reference_link(self.instruction_id)
        bill_payment.enter_approve_response(BillPaymentPage.approve_response_loc, "approve")
        bill_payment.select_approver(BillPaymentPage.approver_dropdown_loc, "SG2BFE1S01@SG2BFE1")
        bill_payment.click_approve_payment_button(BillPaymentPage.approve_payment_button_loc)
        self.success_message = bill_payment.get_success_message()
        function.take_screenshot(self.driver, '24_offline_approve_bill_payment.jpg')
        self.assertEqual('Please update your current to proceed with the transfer.', self.success_message)
