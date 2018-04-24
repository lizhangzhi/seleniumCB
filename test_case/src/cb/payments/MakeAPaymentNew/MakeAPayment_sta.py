import logging
from Util import *
from .MakeAPaymentPage import MakeAPaymentPage
from test_case.src.PageFactory import PageFactory
from time import sleep
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
        make_a_payment.wait_ux_page_load(MakeAPaymentPage.page_title_ux_loc)
        sleep(3)
        make_a_payment.select_account_ux(MakeAPaymentPage.account_ux_loc,
                                         MakeAPaymentPage.account_value_ux_loc,
                                         '30000061189')
        make_a_payment.select_payment_currency_ux(MakeAPaymentPage.payment_currency_ux_loc,
                                                  MakeAPaymentPage.payment_currency_textbox_ux_loc,
                                                  MakeAPaymentPage.payment_currency_value_ux_loc,
                                                  "USD")
        make_a_payment.enter_amount_ux(MakeAPaymentPage.amount_ux_loc, '9')
        make_a_payment.scroll_up_and_down(0, 500)
        make_a_payment.select_beneficiary_single_ux(MakeAPaymentPage.beneficiary_ux_loc,
                                                    MakeAPaymentPage.beneficiary_value_ux_loc,
                                                    'AutomationScriptPayee')
        make_a_payment.select_purpose_code_ux(MakeAPaymentPage.purpose_code_ux_loc,
                                              MakeAPaymentPage.purpose_code_value_ux_loc)
        make_a_payment.scroll_up_and_down(0, 3000)
        make_a_payment.select_bank_charges_ux(MakeAPaymentPage.bank_charges_ux_loc)
        make_a_payment.enter_payment_details_ux(MakeAPaymentPage.payment_details_ux_loc,
                                                'payment details')
        make_a_payment.click_next_button_ux(MakeAPaymentPage.next_button_ux_loc)
        make_a_payment.scroll_up_and_down(0, 2000)
        make_a_payment.click_submit_button_ux(MakeAPaymentPage.submit_button_ux_loc)
        self.success_message = make_a_payment.get_success_message_ux()
        self.instruction_id = make_a_payment.get_success_message_ux().split()[2]
        make_a_payment.switch_to_frame(out=True)

    @log(logger=logging.getLogger(__name__))
    def test_1_create_vn_tt(self):
        """测试能通过Make A Payment创建一条VN Telegraphic Transfer"""
        make_a_payment = PageFactory.get_make_a_payment_page_instance(self.driver)
        make_a_payment.login_cb(self.url, 'VNUAT1A02', 'VNUAT1')
        self.create_vn_tt()
        function.take_screenshot(self.driver, '17_vn_product_create_TT.jpg')
        self.assertIn('has been created successfully', self.success_message)
        PageFactory.clean_page_instance()
