import logging
from time import sleep
from Util import *
from test_case.src.PageFactory import PageFactory
from .GiroPaymentPage import GiroPaymentPage


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
        giro_payment.click_approve_payment_button(GiroPaymentPage.approve_payment_button_loc)
        giro_payment.enter_approve_response(GiroPaymentPage.approve_response_loc, 'response')
        giro_payment.click_submit_button()
        self.success_message = giro_payment.get_success_message()

    @log(logger=logging.getLogger(__name__))
    def test_1_reject_LVT(self):
        """测试old ui能在view页面reject一条Giro Payment"""
        self.create_LVT()
        self.reject_LVT()
        function.take_screenshot(self.driver, '7_giro_payment_reject.jpg')
        self.assertIn('has been rejected successfully', self.success_message)
        PageFactory.clean_page_instance()

    @log(logger=logging.getLogger(__name__))
    def test_2_delete_LVT(self):
        """测试old ui能在view页面delete一条Giro Payment"""
        self.create_LVT()
        self.delete_LVT()
        function.take_screenshot(self.driver, '8_giro_payment_delete.jpg')
        self.assertIn('has been deleted successfully', self.success_message)
        PageFactory.clean_page_instance()

    @log(logger=logging.getLogger(__name__))
    def test_3_approve_LVT(self):
        """测试old ui能在view页面approve一条Giro Payment"""
        self.create_LVT()
        self.approve_LVT()
        function.take_screenshot(self.driver, '9_giro_payment_approve.jpg')
        self.assertIn('has been approved successfully', self.success_message)
        PageFactory.clean_page_instance()

    @log(logger=logging.getLogger(__name__))
    def test_4_approve_by_group(self):
        """测试在my approval list点击到View Group页面执行approve group"""
        self.create_LVT()
        giro_payment = PageFactory.get_giro_payment_page_instance(self.driver)
        giro_payment.open_menu("Payments", "Transfer Center")
        giro_payment.click_filter_button()
        giro_payment.enter_reference(GiroPaymentPage.reference_loc, self.instruction_id)
        giro_payment.click_go_button(GiroPaymentPage.go_button_loc)
        giro_payment.select_transaction_in_center()
        giro_payment.click_add_to_new_group_button()
        giro_payment.click_preview_group_button()
        sleep(3)
        giro_payment.click_submit_group_button()
        self.group_id = giro_payment.get_success_message().split()[4]
        print(self.group_id)
        giro_payment.open_menu("Payments", "My Approvals")
        giro_payment.click_tab(GiroPaymentPage.by_group_tab_loc)
        giro_payment.enter_reference(GiroPaymentPage.reference_loc, self.group_id)
        giro_payment.click_go_button(GiroPaymentPage.approval_list_go_button_loc)
        giro_payment.click_reference_link(self.group_id)
        sleep(3)
        giro_payment.scroll_up_and_down(0, 1000)
        giro_payment.click_approve_group_button()
        giro_payment.enter_approve_response(GiroPaymentPage.approve_response_loc, "approve")
        giro_payment.click_preview_group_button()
        self.success_message = giro_payment.get_success_message()
        function.take_screenshot(self.driver, '25_my_approval_approve_group.jpg')
        self.assertIn('has been approved successfully.', self.success_message)
        PageFactory.clean_page_instance()
