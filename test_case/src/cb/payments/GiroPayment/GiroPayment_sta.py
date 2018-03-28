from time import sleep
from Util import *
from test_case.src.PageFactory import PageFactory


# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: GiroPayment_sta.py
@time: 2018/1/22 10:25
'''


class GiroPaymentTest(MyUnittest):

    def create_LVT(self):
        giro_payment = PageFactory.get_giro_payment_page_instance(self.driver)
        giro_payment.login_cb(self.url, self.login_id, self.company_id)
        giro_payment.open_menu("Payments", "GIRO Payment")
        giro_payment.select_from_account('LEONA ALBRECHT - 0018001843 - SGD')
        giro_payment.enter_amount('10')
        giro_payment.select_beneficiary(3)
        giro_payment.scroll_up_and_down(0, 1000)
        giro_payment.click_preview_button()
        sleep(3)
        giro_payment.scroll_up_and_down(0, 1000)
        giro_payment.click_submit_button()
        self.success_message = giro_payment.get_success_message()
        self.instruction_id = giro_payment.get_success_message().split()[2]

    def reject_LVT(self):
        giro_payment = PageFactory.get_giro_payment_page_instance(self.driver)
        giro_payment.get_to_view_payment_page(self.instruction_id)
        sleep(5)
        giro_payment.scroll_up_and_down(0, 1000)
        giro_payment.click_reject_button()
        sleep(5)
        giro_payment.scroll_up_and_down(0, 1000)
        giro_payment.click_submit_button()
        self.success_message = giro_payment.get_success_message()

    def delete_LVT(self):
        giro_payment = PageFactory.get_giro_payment_page_instance(self.driver)
        giro_payment.get_to_view_payment_page(self.instruction_id)
        sleep(5)
        giro_payment.scroll_up_and_down(0, 1000)
        giro_payment.click_delete_button_loc()
        sleep(3)
        giro_payment.scroll_up_and_down(0, 1000)
        giro_payment.click_submit_button()
        self.success_message = giro_payment.get_success_message()

    def approve_LVT(self):
        giro_payment = PageFactory.get_giro_payment_page_instance(self.driver)
        giro_payment.get_to_view_payment_page(self.instruction_id)
        sleep(5)
        giro_payment.scroll_up_and_down(0, 1000)
        giro_payment.click_approve_payment_button()
        giro_payment.enter_approve_now_response('response')
        giro_payment.click_submit_button()
        self.success_message = giro_payment.get_success_message()

    def test_1_reject_LVT(self):
        self.create_LVT()
        self.reject_LVT()
        function.take_screenshot(self.driver, '7_giro_payment_reject.jpg')
        self.assertIn('has been rejected successfully', self.success_message)
        PageFactory.clean_page_instance()

    def test_2_delete_LVT(self):
        self.create_LVT()
        self.delete_LVT()
        function.take_screenshot(self.driver, '8_giro_payment_delete.jpg')
        self.assertIn('has been deleted successfully', self.success_message)
        PageFactory.clean_page_instance()

    def test_3_approve_LVT(self):
        self.create_LVT()
        self.approve_LVT()
        function.take_screenshot(self.driver, '9_giro_payment_approve.jpg')
        self.assertIn('has been approved successfully', self.success_message)
        PageFactory.clean_page_instance()
