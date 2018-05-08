import logging
from Util import *
from .PartnerBankPaymentPage import PartnerBankPaymentPage
from test_case.src.PageFactory import PageFactory
from time import sleep

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: PartnerBankPayment_sta.py
@time: 2018/1/17 14:22
'''


class PartnerBankPaymentTest(MyUnittest):

    def create_TDT(self):
        partner_bank_payment = PageFactory.get_partner_bank_payment_page_instance(self.driver)
        partner_bank_payment.open_menu("Payments", "Partner Bank Payment")
        partner_bank_payment.switch_to_frame()
        partner_bank_payment.select_country(PartnerBankPaymentPage.country_ux_loc,
                                            PartnerBankPaymentPage.country_value_ux_loc,
                                            'MALAYSIA')
        sleep(3)
        partner_bank_payment.select_from_account(ux_flag=True,
                                                 account_ux_loc=PartnerBankPaymentPage.account_ux_loc,
                                                 account_value_ux_loc=PartnerBankPaymentPage.account_value_ux_loc,
                                                 account_number='545454NameCIMB CIBBMYKLXXX 545454')
        partner_bank_payment.select_type_ux()
        partner_bank_payment.select_beneficiary(ux_bulk=True,
                                                beneficiary_ux_loc=PartnerBankPaymentPage.beneficiary_ux_loc)
        partner_bank_payment.enter_amount(ux_flag=True, amount_loc=PartnerBankPaymentPage.amount_ux_loc, value='10')
        partner_bank_payment.scroll_up_and_down(0, 1000)
        partner_bank_payment.click_preview_button(ux_flag=True,
                                                  preview_button_loc=PartnerBankPaymentPage.next_button_ux_loc)
        partner_bank_payment.scroll_up_and_down(0, 1000)
        partner_bank_payment.click_submit_button(ux_flag=True,
                                                 submit_button_loc=PartnerBankPaymentPage.submit_button_ux_loc)
        self.success_message = partner_bank_payment.get_success_message(ux_flag=True)
        self.instruction_id = partner_bank_payment.get_success_message(ux_flag=True).split()[3]
        partner_bank_payment.switch_to_frame(out=True)

    def edit_TDT(self):
        partner_bank_payment = PageFactory.get_partner_bank_payment_page_instance(self.driver)
        partner_bank_payment.get_to_view_payment_page(self.instruction_id)
        partner_bank_payment.switch_to_frame()
        partner_bank_payment.wait_view_page_load()
        sleep(3)
        partner_bank_payment.click_edit_button(ux_flag=True, edit_button_loc=PartnerBankPaymentPage.edit_icon_ux_loc)
        sleep(3)
        partner_bank_payment.enter_amount(ux_flag=True, amount_loc=PartnerBankPaymentPage.amount_ux_loc, value='20')
        partner_bank_payment.scroll_up_and_down(0, 1500)
        partner_bank_payment.click_preview_button(ux_flag=True,
                                                  preview_button_loc=PartnerBankPaymentPage.next_button_ux_loc)
        partner_bank_payment.scroll_up_and_down(0, 1500)
        partner_bank_payment.click_submit_button(ux_flag=True,
                                                 submit_button_loc=PartnerBankPaymentPage.submit_button_ux_loc)
        self.edit_success_message = partner_bank_payment.get_success_message(ux_flag=True)
        partner_bank_payment.switch_to_frame(out=True)

    def approve_TDT(self):
        partner_bank_payment = PageFactory.get_partner_bank_payment_page_instance(self.driver)
        partner_bank_payment.get_to_view_payment_page(self.instruction_id)
        partner_bank_payment.switch_to_frame()
        partner_bank_payment.wait_page_load(PartnerBankPaymentPage.hash_value_loc)
        sleep(2)
        partner_bank_payment.scroll_up_and_down(0, 3000)
        partner_bank_payment.click_approve_button(PartnerBankPaymentPage.approve_button_ux_loc)
        partner_bank_payment.scroll_up_and_down(0, 3000)
        # partner_bank_payment.click_challenge_button_ux()
        partner_bank_payment.enter_approve_response(approve_response_loc=PartnerBankPaymentPage.response_ux_loc,
                                                    value='me')
        partner_bank_payment.click_approve_button(PartnerBankPaymentPage.approve_button_ux_loc)
        self.approve_success_message = partner_bank_payment. \
            get_success_message(ux_flag=True,
                                success_message_ux_loc=PartnerBankPaymentPage.approve_success_message_ux_loc)

    @log(logger=logging.getLogger(__name__))
    def test_1_create_TDT(self):
        """测试能创建一条Partner Bank Payment"""
        try:
            partner_bank_payment = PageFactory.get_partner_bank_payment_page_instance(self.driver)
            partner_bank_payment.login_cb(self.url, self.login_id, self.company_id)
            self.create_TDT()
            function.take_screenshot(self.driver, '10_partner_bank_payment_create.jpg')
            self.assertIn('has been created successfully', self.success_message)
        finally:
            PageFactory.clean_page_instance()

    @log(logger=logging.getLogger(__name__))
    def test_2_approve_TDT(self):
        """测试能在View页面Approve一条Partner Bank Payment"""
        try:
            partner_bank_payment = PageFactory.get_partner_bank_payment_page_instance(self.driver)
            partner_bank_payment.login_cb(self.url, self.login_id, self.company_id)
            self.create_TDT()
            self.approve_TDT()
            function.take_screenshot(self.driver, '11_partner_bank_payment_approve.jpg')
            self.assertIn('has been successfully approved', self.approve_success_message)
        finally:
            PageFactory.clean_page_instance()

    @log(logger=logging.getLogger(__name__))
    def test_3_edit_TDT(self):
        """测试能在View页面modify一条Partner Bank Payment"""
        try:
            partner_bank_payment = PageFactory.get_partner_bank_payment_page_instance(self.driver)
            partner_bank_payment.login_cb(self.url, self.login_id, self.company_id)
            self.create_TDT()
            self.edit_TDT()
            function.take_screenshot(self.driver, '12_partner_bank_payment_edit.jpg')
            self.assertIn('has been modified successfully', self.edit_success_message)
        finally:
            PageFactory.clean_page_instance()

    @log(logger=logging.getLogger(__name__))
    def test_4_viewTDT_by_confidential(self):
        """
        测试如果login user有Partner Bank Payment - confidential权限，
        在其他user创建的Partner Bank Payment的view页面,能查看Beneficiary信息"""
        try:
            partner_bank_payment = PageFactory.get_partner_bank_payment_page_instance(self.driver)
            partner_bank_payment.login_cb(self.url, 'SG2BFE1S06', 'SG2BFE1')
            self.create_TDT()
            partner_bank_payment.login_cb(self.url, self.login_id, self.company_id)
            partner_bank_payment.get_to_view_payment_page(self.instruction_id)
            partner_bank_payment.switch_to_frame()
            partner_bank_payment.wait_view_page_load()
            function.take_screenshot(self.driver, '13_partner_bank_payment_confidential_to_view.jpg')
            self.assertTrue(partner_bank_payment.get_payee_list_ux())
        finally:
            PageFactory.clean_page_instance()

    @log(logger=logging.getLogger(__name__))
    def test_5_viewTDT_by_no_confidential(self):
        """
        测试如果login user没有Partner Bank Payment - confidential权限，
        在其他user创建的Partner Bank Payment的view页面,无法查看Beneficiary信息"""
        try:
            partner_bank_payment = PageFactory.get_partner_bank_payment_page_instance(self.driver)
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
        finally:
            PageFactory.clean_page_instance()
