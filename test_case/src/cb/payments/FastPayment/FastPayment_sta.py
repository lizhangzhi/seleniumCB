import time
from time import sleep
from Util import *
from test_case.src.PageFactory import PageFactory


# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: FastPayment_sta.py
@time: 2018/1/19 20:52
'''


class FastPaymentTest(MyUnittest):
    now = time.strftime("%Y%m%d%H%M%S")

    def create_approve_now_GPP(self):
        fast_payment = PageFactory.get_fast_payment_page_instance(self.driver)
        fast_payment.login_cb(self.url, self.login_id, self.company_id)
        fast_payment.open_menu("Payments", "FAST Payment")
        fast_payment.select_from_account('LEONA ALBRECHT - 0018001843 - SGD')
        fast_payment.enter_amount('10')
        fast_payment.select_purpose_code()
        fast_payment.select_beneficiary(2)
        fast_payment.scroll_up_and_down(0, 1000)
        fast_payment.click_approve_now_checkbox()
        fast_payment.click_preview_button()
        sleep(3)
        fast_payment.scroll_up_and_down(0, 1000)
        fast_payment.enter_approve_now_response('1')
        fast_payment.click_approve_payment_button()
        self.success_message = fast_payment.get_success_message()

    def create_with_template_GPP(self):
        fast_payment = PageFactory.get_fast_payment_page_instance(self.driver)
        fast_payment.login_cb(self.url, self.login_id, self.company_id)
        fast_payment.open_menu("Payments", "FAST Payment")
        fast_payment.select_from_account('LEONA ALBRECHT - 0018001843 - SGD')
        fast_payment.enter_amount('10')
        fast_payment.select_purpose_code()
        fast_payment.select_beneficiary(2)
        fast_payment.scroll_up_and_down(0, 1000)
        fast_payment.click_save_as_template_checkbox('GPPTem' + self.now)
        fast_payment.click_preview_button()
        sleep(3)
        fast_payment.scroll_up_and_down(0, 1000)
        fast_payment.click_submit_button()
        self.success_message = fast_payment.get_success_message()

    def save_as_draft_GPP(self):
        fast_payment = PageFactory.get_fast_payment_page_instance(self.driver)
        fast_payment.login_cb(self.url, self.login_id, self.company_id)
        fast_payment.open_menu("Payments", "FAST Payment")
        fast_payment.select_from_account('LEONA ALBRECHT - 0018001843 - SGD')
        fast_payment.enter_amount('10')
        fast_payment.select_purpose_code()
        fast_payment.select_beneficiary(2)
        fast_payment.scroll_up_and_down(0, 1000)
        fast_payment.click_submit_button()
        self.success_message = fast_payment.get_success_message()

    def test_1_create_approve_now_GPP(self):
        self.create_approve_now_GPP()
        function.take_screenshot(self.driver, '2_fast_payment_approve_now.jpg')
        self.assertIn('has been created successfully with status Approved', self.success_message)
        PageFactory.clean_page_instance()

    def test_2_create_with_template_GPP(self):
        self.create_with_template_GPP()
        function.take_screenshot(self.driver, '3_fast_payment_create_with_template.jpg')
        self.assertIn('has been created successfully', self.success_message)
        self.assertIn('FAST Payment template', self.success_message)
        PageFactory.clean_page_instance()

    def test_3_save_as_draft_GPP(self):
        self.save_as_draft_GPP()
        function.take_screenshot(self.driver, '6_fast_payment_save_as_draft.jpg')
        self.assertIn('has been created successfully with status Saved.', self.success_message)
        PageFactory.clean_page_instance()
