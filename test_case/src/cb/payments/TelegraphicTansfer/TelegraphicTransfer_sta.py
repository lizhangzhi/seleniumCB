from time import sleep
from Util import *
from test_case.src.PageFactory import PageFactory


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
        telegraphic_transfer.wait_page_load()
        telegraphic_transfer.scroll_up_and_down(0, 1000)
        telegraphic_transfer.click_submit_button()
        self.success_message = telegraphic_transfer.get_success_message()
        self.instruction_id = telegraphic_transfer.get_success_message().split()[2]

    def copy_TT(self):
        telegraphic_transfer = PageFactory.get_telegraphic_transfer_page_instance(self.driver)
        telegraphic_transfer.get_to_view_payment_page(self.instruction_id)
        telegraphic_transfer.wait_page_load()
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_copy_button()
        telegraphic_transfer.wait_page_load()
        telegraphic_transfer.enter_payment_details('Copy From TT')
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_preview_button()
        telegraphic_transfer.wait_page_load()
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_submit_button()
        self.success_message = telegraphic_transfer.get_success_message()

    def edit_TT(self):
        telegraphic_transfer = PageFactory.get_telegraphic_transfer_page_instance(self.driver)
        telegraphic_transfer.get_to_view_payment_page(self.instruction_id)
        telegraphic_transfer.wait_page_load()
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_edit_button()
        telegraphic_transfer.wait_page_load()
        telegraphic_transfer.enter_payment_details('Edit TT')
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_preview_on_edit_page()
        telegraphic_transfer.wait_page_load()
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_submit_button()
        self.success_message = telegraphic_transfer.get_success_message()

    def test_1_create_TT(self):
        self.create_TT()
        function.take_screenshot(self.driver, '1_telegraphic_transfer_create.jpg')
        self.assertIn('has been created successfully', self.success_message)
        PageFactory.clean_page_instance()

    def test_2_copy_TT(self):
        self.create_TT()
        self.copy_TT()
        function.take_screenshot(self.driver, '4_telegraphic_transfer_copy.jpg')
        self.assertIn('has been created successfully', self.success_message)
        PageFactory.clean_page_instance()

    def test_3_edit_TT(self):
        self.create_TT()
        self.edit_TT()
        function.take_screenshot(self.driver, '5_telegraphic_transfer_edit.jpg')
        self.assertIn('has been modified successfully', self.success_message)
        PageFactory.clean_page_instance()
