import logging
from time import sleep
from Util import *
from test_case.src.PageFactory import PageFactory
from .TelegraphicTransferPage import TelegraphicTransferPage


# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: TelegraphicTransfer_sta.py
@time: 2017/8/15 15:24
'''


class TelegraphicTransferTest(MyUnittest):

    def create_TT(self):
        telegraphic_transfer = PageFactory.get_telegraphic_transfer_page_instance(self.driver)
        telegraphic_transfer.login_cb(self.url, self.login_id, self.company_id)
        telegraphic_transfer.open_menu("Payments", "Telegraphic Transfer")
        telegraphic_transfer.select_from_account('LEONA ALBRECHT - 0018001843 - SGD')
        telegraphic_transfer.select_payment_currency('SGD')
        telegraphic_transfer.enter_amount('10')
        telegraphic_transfer.scroll_up_and_down(0, 500)
        telegraphic_transfer.select_beneficiary(2)
        telegraphic_transfer.enter_instruction('Instruction to DBS Bank')
        telegraphic_transfer.scroll_up_and_down(0, 1000)
        telegraphic_transfer.click_preview_button()
        sleep(3)
        telegraphic_transfer.scroll_up_and_down(0, 1000)
        telegraphic_transfer.click_submit_button()
        self.success_message = telegraphic_transfer.get_success_message()
        self.instruction_id = telegraphic_transfer.get_success_message().split()[2]

    def copy_TT(self):
        telegraphic_transfer = PageFactory.get_telegraphic_transfer_page_instance(self.driver)
        telegraphic_transfer.get_to_view_payment_page(self.instruction_id)
        sleep(5)
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_copy_button()
        sleep(6)
        telegraphic_transfer.enter_payment_details('Copy From TT')
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_preview_button()
        sleep(5)
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_submit_button()
        self.success_message = telegraphic_transfer.get_success_message()

    def edit_TT(self):
        telegraphic_transfer = PageFactory.get_telegraphic_transfer_page_instance(self.driver)
        telegraphic_transfer.get_to_view_payment_page(self.instruction_id)
        sleep(5)
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_edit_button()
        sleep(5)
        telegraphic_transfer.enter_payment_details('Edit TT')
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_preview_on_edit_page()
        sleep(5)
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_submit_button()
        self.success_message = telegraphic_transfer.get_success_message()

    @log(logger=logging.getLogger(__name__))
    def test_1_create_TT(self):
        """测试能通过old UI成功创建一条Telegraphic Transfer"""
        self.create_TT()
        function.take_screenshot(self.driver, '1_telegraphic_transfer_create.jpg')
        self.assertIn('has been created successfully', self.success_message)
        PageFactory.clean_page_instance()

    @log(logger=logging.getLogger(__name__))
    def test_2_copy_TT(self):
        """测试能通过old UI成功复制一条Telegraphic Transfer"""
        self.create_TT()
        self.copy_TT()
        function.take_screenshot(self.driver, '4_telegraphic_transfer_copy.jpg')
        self.assertIn('has been created successfully', self.success_message)
        PageFactory.clean_page_instance()

    @log(logger=logging.getLogger(__name__))
    def test_3_edit_TT(self):
        """测试能通过old UI成功modify一条Telegraphic Transfer"""
        self.create_TT()
        self.edit_TT()
        function.take_screenshot(self.driver, '5_telegraphic_transfer_edit.jpg')
        self.assertIn('has been modified successfully', self.success_message)
        PageFactory.clean_page_instance()

    @log(logger=logging.getLogger(__name__))
    def test_4_my_approval_approve_TT(self):
        """测试在my approval list 页面通过select的方式approve telegraphic transfer"""
        self.create_TT()
        telegraphic_transfer = PageFactory.get_telegraphic_transfer_page_instance(self.driver)
        sleep(3)
        telegraphic_transfer.open_menu("Payments", "My Approvals")
        telegraphic_transfer.click_tab(TelegraphicTransferPage.list_per_transaction_tab_loc)
        telegraphic_transfer.enter_reference(TelegraphicTransferPage.reference_loc, self.instruction_id)
        telegraphic_transfer.click_go_button(TelegraphicTransferPage.approval_list_go_button_loc)
        telegraphic_transfer.select_transaction_in_list()
        telegraphic_transfer.scroll_up_and_down(0, 1000)
        telegraphic_transfer.click_approve_button(TelegraphicTransferPage.my_approval_approve_button_loc)
        telegraphic_transfer.enter_approve_response(TelegraphicTransferPage.approve_response_loc, "approve")
        telegraphic_transfer.click_approve_payment_button(TelegraphicTransferPage.approve_payment_button_loc)
        self.success_message = telegraphic_transfer.get_success_message()
        function.take_screenshot(self.driver, '27_my_approval_telegraphic_transfer_approve.jpg')
        self.assertIn('has been approved successfully', self.success_message)
        PageFactory.clean_page_instance()
