from Util import *
from test_case.src.cb.payments.PartnerBankPayment.PartnerBankPaymentPage import PartnerBankPaymentPage
from time import sleep

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: PartnerBankPayment_sta.py
@time: 2018/1/17 14:22
'''


class PartnerBankPaymentTest(MyUnittest):

    def create_TDT(self):
        partner_bank_payment = PartnerBankPaymentPage(self.driver)
        partner_bank_payment.open_menu("Payments", "Partner Bank Payment")
        partner_bank_payment.switch_to_frame()
        partner_bank_payment.select_country_ux()
        sleep(3)
        partner_bank_payment.select_account_ux()
        partner_bank_payment.select_type_ux()
        partner_bank_payment.select_beneficiary_ux()
        partner_bank_payment.enter_amount_ux('10')
        partner_bank_payment.scroll_up_and_down(0, 1000)
        partner_bank_payment.click_next_button_ux()
        partner_bank_payment.scroll_up_and_down(0, 1000)
        partner_bank_payment.click_submit_button_ux()
        self.success_message = partner_bank_payment.get_success_message_ux()
        self.instruction_id = partner_bank_payment.get_success_message_ux().split()[3]
        partner_bank_payment.switch_to_frame(out=True)

    def edit_TDT(self):
        partner_bank_payment = PartnerBankPaymentPage(self.driver)
        partner_bank_payment.get_to_view_payment_page(self.instruction_id)
        partner_bank_payment.switch_to_frame()
        partner_bank_payment.wait_view_page_load()
        partner_bank_payment.click_edit_icon_ux()
        sleep(3)
        partner_bank_payment.enter_amount_ux('20')
        partner_bank_payment.scroll_up_and_down(0, 1000)
        partner_bank_payment.click_next_button_ux()
        partner_bank_payment.scroll_up_and_down(0, 1000)
        partner_bank_payment.click_submit_button_ux()
        self.edit_success_message = partner_bank_payment.get_success_message_ux()
        partner_bank_payment.switch_to_frame(out=True)

    def approve_TDT(self):
        partner_bank_payment = PartnerBankPaymentPage(self.driver)
        partner_bank_payment.get_to_view_payment_page(self.instruction_id)
        partner_bank_payment.switch_to_frame()
        partner_bank_payment.wait_view_page_load()
        partner_bank_payment.scroll_up_and_down(0, 3000)
        partner_bank_payment.click_approve_button_ux()
        partner_bank_payment.scroll_up_and_down(0, 3000)
        # partner_bank_payment.click_challenge_button_ux()
        partner_bank_payment.enter_response_ux('me')
        partner_bank_payment.click_approve_button_ux()
        self.approve_success_message = partner_bank_payment.get_approve_success_message_ux()

    # # 创建一条partner bank
    def test_1_create_TDT(self):
        partner_bank_payment = PartnerBankPaymentPage(self.driver)
        partner_bank_payment.login_cb(self.url, self.login_id, self.company_id)
        self.create_TDT()
        function.take_screenshot(self.driver, '10_partner_bank_payment_create.jpg')
        self.assertIn('has been created successfully', self.success_message)

    # 创建一条partner bank ,然后approve
    def test_2_approve_TDT(self):
        partner_bank_payment = PartnerBankPaymentPage(self.driver)
        partner_bank_payment.login_cb(self.url, self.login_id, self.company_id)
        self.create_TDT()
        self.approve_TDT()
        function.take_screenshot(self.driver, '11_partner_bank_payment_approve.jpg')
        self.assertIn('has been successfully approved', self.approve_success_message)

    # 创建一条partner bank ,然后edit
    def test_3_edit_TDT(self):
        partner_bank_payment = PartnerBankPaymentPage(self.driver)
        partner_bank_payment.login_cb(self.url, self.login_id, self.company_id)
        self.create_TDT()
        self.edit_TDT()
        function.take_screenshot(self.driver, '12_partner_bank_payment_edit.jpg')
        self.assertIn('has been modified successfully', self.edit_success_message)

    # 用有partner bank - confidential权限的user去view 别的user创建的partner bank -payroll
    def test_4_viewTDT_by_confidential(self):
        partner_bank_payment = PartnerBankPaymentPage(self.driver)
        partner_bank_payment.login_cb(self.url, 'SG2BFE1S06', 'SG2BFE1')
        self.create_TDT()
        partner_bank_payment.login_cb(self.url, self.login_id, self.company_id)
        partner_bank_payment.get_to_view_payment_page(self.instruction_id)
        partner_bank_payment.switch_to_frame()
        partner_bank_payment.wait_view_page_load()
        function.take_screenshot(self.driver, '13_partner_bank_payment_confidential_to_view.jpg')
        self.assertTrue(partner_bank_payment.get_payee_list_ux())

    # 用没有partner bank - confidential权限的user去view 别的user创建的partner bank -payroll
    def test_5_viewTDT_by_no_confidential(self):
        partner_bank_payment = PartnerBankPaymentPage(self.driver)
        partner_bank_payment.login_cb(self.url, self.login_id, self.company_id)
        self.create_TDT()
        partner_bank_payment.login_cb(self.url, 'SG2BFE1S06', 'SG2BFE1')
        partner_bank_payment.get_to_view_payment_page(self.instruction_id)
        partner_bank_payment.switch_to_frame()
        partner_bank_payment.wait_view_page_load()
        self.confidential_message = partner_bank_payment.get_payee_confidential_ux()
        function.take_screenshot(self.driver, '14_partner_bank_payment_no_confidential_to_view.jpg')
        self.assertIn('Confidential information, you are not entitled to view Beneficiary Details',
                      self.confidential_message)
