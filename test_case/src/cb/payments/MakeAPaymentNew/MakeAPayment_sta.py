from Util import *
from test_case.src.PageFactory import PageFactory
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: MakeAPayment_sta.py
@time: 2018/3/21 15:48
'''


class MakeAPaymentTest(MyUnittest):

    def create_vn_tt(self):
        make_a_payment = PageFactory.get_make_a_payment_page_instance(self.driver)
        make_a_payment.open_menu("Payments", "Make a payment [New]")
        make_a_payment.switch_to_frame()
        make_a_payment.wait_ux_page_load()
        make_a_payment.select_account_ux('22334444555')
        make_a_payment.select_payment_currency_ux("USD")
        make_a_payment.enter_amount_ux('9')
        make_a_payment.scroll_up_and_down(0, 500)
        make_a_payment.select_beneficiary_ux('TTInternationalBene - ANZBVNV0472 - 12313123')
        make_a_payment.select_purpose_code_ux()
        make_a_payment.scroll_up_and_down(0, 3000)
        make_a_payment.select_bank_charges_ux()
        make_a_payment.enter_payment_details_ux('payment details')
        make_a_payment.click_next_button_ux()
        make_a_payment.scroll_up_and_down(0, 2000)
        make_a_payment.click_submit_button_ux()
        self.success_message = make_a_payment.get_success_message_ux()
        self.instruction_id = make_a_payment.get_success_message_ux().split()[2]
        make_a_payment.switch_to_frame(out=True)

    def test_1_create_vn_tt(self):
        make_a_payment = PageFactory.get_make_a_payment_page_instance(self.driver)
        make_a_payment.login_cb(self.url, 'VNP2A03S11', 'VNP2A03')
        self.create_vn_tt()
        function.take_screenshot(self.driver, '17_vn_product_create_TT.jpg')
        self.assertIn('has been created successfully', self.success_message)
