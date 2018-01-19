from Util import *
from test_case.src.cb.payments.FastPayment.FastPaymentPage import FastPaymentPage
from time import sleep

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: FastPayment_sta_test.py
@time: 2018/1/19 20:52
'''


class FastPaymentTest(MyUnittest):

    def create_GPP(self):
        fast_payment = FastPaymentPage(self.driver)
        fast_payment.login_cb(self.url, self.login_id, self.company_id)
        sleep(5)
        fast_payment.open_menu("Payments", "FAST Payment")
        fast_payment.select_from_account('LEONA ALBRECHT - 0018001843 - SGD')
        fast_payment.enter_amount('10')
        fast_payment.select_purpose_code()
        fast_payment.select_beneficiary()
        fast_payment.scroll_down()
        fast_payment.click_approve_now_checkbox()
        fast_payment.click_preview_button()
        sleep(3)
        fast_payment.scroll_down()
        fast_payment.enter_approve_now_response('1')
        fast_payment.click_approve_payment_button()
        self.success_message = fast_payment.get_success_message()
        self.instruction_id = fast_payment.get_success_message().split()[2]

    def test_1_create_GPP(self):
        # function.take_screenshot(self.driver, 'create_fast_payment.jpg')
        self.create_GPP()
        self.assertIn('has been created successfully with status Approved', self.success_message)
