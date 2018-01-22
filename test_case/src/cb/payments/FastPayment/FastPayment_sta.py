from Util import *
from test_case.src.cb.payments.FastPayment.FastPaymentPage import FastPaymentPage
from time import sleep
import time

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: FastPayment_sta.py
@time: 2018/1/19 20:52
'''


class FastPaymentTest(MyUnittest):
    now = time.strftime("%Y%m%d%H%M%S")

    def create_approve_now_GPP(self):
        fast_payment = FastPaymentPage(self.driver)
        fast_payment.login_cb(self.url, self.login_id, self.company_id)
        sleep(5)
        fast_payment.open_menu("Payments", "FAST Payment")
        fast_payment.select_from_account('LEONA ALBRECHT - 0018001843 - SGD')
        fast_payment.enter_amount('10')
        fast_payment.select_purpose_code()
        fast_payment.select_beneficiary(2)
        fast_payment.scroll_down()
        fast_payment.click_approve_now_checkbox()
        fast_payment.click_preview_button()
        sleep(3)
        fast_payment.scroll_down()
        fast_payment.enter_approve_now_response('1')
        fast_payment.click_approve_payment_button()
        self.success_message = fast_payment.get_success_message()

    def create_with_template_GPP(self):
        fast_payment = FastPaymentPage(self.driver)
        fast_payment.login_cb(self.url, self.login_id, self.company_id)
        sleep(5)
        fast_payment.open_menu("Payments", "FAST Payment")
        fast_payment.select_from_account('LEONA ALBRECHT - 0018001843 - SGD')
        fast_payment.enter_amount('10')
        fast_payment.select_purpose_code()
        fast_payment.select_beneficiary(2)
        fast_payment.scroll_down()
        fast_payment.click_save_as_template_checkbox('GPPTem' + self.now)
        fast_payment.click_preview_button()
        sleep(3)
        fast_payment.scroll_down()
        fast_payment.click_submit_button()
        self.success_message = fast_payment.get_success_message()

    def save_as_draft_GPP(self):
        fast_payment = FastPaymentPage(self.driver)
        fast_payment.login_cb(self.url, self.login_id, self.company_id)
        sleep(5)
        fast_payment.open_menu("Payments", "FAST Payment")
        fast_payment.select_from_account('LEONA ALBRECHT - 0018001843 - SGD')
        fast_payment.enter_amount('10')
        fast_payment.select_purpose_code()
        fast_payment.select_beneficiary(2)
        fast_payment.scroll_down()
        fast_payment.click_submit_button()
        self.success_message = fast_payment.get_success_message()

    def test_1_create_approve_now_GPP(self):
        # function.take_screenshot(self.driver, 'approve_now_fast_payment.jpg')
        self.create_approve_now_GPP()
        self.assertIn('has been created successfully with status Approved', self.success_message)

    def test_2_create_with_template_GPP(self):
        # function.take_screenshot(self.driver, 'create_with_template_fast_payment.jpg')
        self.create_with_template_GPP()
        self.assertIn('has been created successfully', self.success_message)
        self.assertIn('FAST Payment template', self.success_message)

    def test_3_save_as_draft_GPP(self):
        # function.take_screenshot(self.driver, 'save_as_draft_fast_payment.jpg')
        self.save_as_draft_GPP()
        self.assertIn('has been created successfully with status Saved.', self.success_message)
