from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage
from time import sleep

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: PartnerBankPayment_sta_test.py
@time: 2018/1/17 14:22
'''


class PartnerBankPaymentTest(MyUnittest):

    def login_cb(self, url, login_id, company_id):
        login = LoginPage(self.driver)
        login.logincb(url, login_id, company_id)

    def get_to_view_payment_page(self, instruction_id):
        partner_bank_payment = PaymentPage(self.driver)
        partner_bank_payment.open_menu("Payments", "Transfer Center")
        partner_bank_payment.click_filter_button()
        partner_bank_payment.enter_reference(instruction_id)
        partner_bank_payment.click_go_button()
        partner_bank_payment.click_reference_link(instruction_id)

    def createTDT(self):
        sleep(10)
        partner_bank_payment = PaymentPage(self.driver)
        partner_bank_payment.open_menu("Payments", "Partner Bank Payment")
        sleep(60)
        partner_bank_payment.switch_to_frame()
        partner_bank_payment.select_country_ux()
        partner_bank_payment.select_account_ux()
        partner_bank_payment.select_type_ux()
        partner_bank_payment.select_beneficiary_ux()
        partner_bank_payment.enter_amount_ux('10')
        partner_bank_payment.scroll_down()
        partner_bank_payment.click_next_button_ux()
        partner_bank_payment.scroll_down()
        partner_bank_payment.click_submit_button_ux()
        self.success_message = partner_bank_payment.get_success_message_ux()
        self.instruction_id = partner_bank_payment.get_success_message_ux().split()[3]
        partner_bank_payment.switch_to_frame(out=True)

    def editTDT(self):
        partner_bank_payment = PaymentPage(self.driver)
        self.get_to_view_payment_page(self.instruction_id)
        partner_bank_payment.switch_to_frame()
        partner_bank_payment.click_edit_icon_ux()
        partner_bank_payment.enter_amount_ux('20')
        partner_bank_payment.scroll_down()
        partner_bank_payment.click_next_button_ux()
        partner_bank_payment.scroll_down()
        partner_bank_payment.click_submit_button_ux()
        self.edit_success_message = partner_bank_payment.get_success_message_ux()
        partner_bank_payment.switch_to_frame(out=True)

    def approveTDT(self):
        partner_bank_payment = PaymentPage(self.driver)
        self.get_to_view_payment_page(self.instruction_id)
        partner_bank_payment.switch_to_frame()
        partner_bank_payment.click_approve_button_ux()
        partner_bank_payment.click_challenge_button_ux()
        partner_bank_payment.enter_response_ux('me')
        partner_bank_payment.click_approve_button_ux()
        self.approve_success_message = partner_bank_payment.get_approve_success_message_ux()

    def test_1_create_edit_approve_TDT(self):
        self.login_cb(self.url, self.login_id, self.company_id)
        self.createTDT()
        self.assertIn('has been created successfully', self.success_message)
        self.editTDT()
        self.assertIn('has been modified successfully', self.edit_success_message)
        self.approveTDT()
        self.assertIn('has been successfully approved', self.approve_success_message)

    def test_2_viewTDT_by_confidential(self):
        self.login_cb(self.url, self.login_id, self.company_id)
        self.createTDT()
        self.login_cb(self.url, 'SG2BFE1S06', 'SG2BFE1')
        self.get_to_view_payment_page(self.instruction_id)
        partner_bank_payment = PaymentPage(self.driver)
        partner_bank_payment.switch_to_frame()
        self.confidential_message = partner_bank_payment.get_payee_confidential_ux()
        print(self.confidential_message)
        self.assertIn('Confidential information, you are not entitled to view Beneficiary Details',
                      self.confidential_message)

    def test_3_viewTDT_by_no_confidential(self):
        self.login_cb(self.url, 'SG2BFE1S06', 'SG2BFE1')
        self.createTDT()
        self.login_cb(self.url, self.login_id, self.company_id)
        self.get_to_view_payment_page(self.instruction_id)
        partner_bank_payment = PaymentPage(self.driver)
        partner_bank_payment.switch_to_frame()
        self.assertTrue(partner_bank_payment.get_payee_list_ux())