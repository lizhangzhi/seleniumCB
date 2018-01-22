from Util import *
from test_case.src.cb.payments.TelegraphicTansfer.TelegraphicTransferPage import TelegraphicTransferPage
from time import sleep

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: TelegraphicTransfer_sta.py
@time: 2017/8/15 15:24
'''


class TelegraphicTransferTest(MyUnittest):

    def create_TT(self):
        telegraphic_transfer = TelegraphicTransferPage(self.driver)
        telegraphic_transfer.login_cb(self.url, self.login_id, self.company_id)
        telegraphic_transfer.open_menu("Payments", "Telegraphic Transfer")
        telegraphic_transfer.select_from_account('LEONA ALBRECHT - 0018001843 - SGD')
        telegraphic_transfer.select_payment_currency('SGD')
        telegraphic_transfer.enter_amount('10')
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
        telegraphic_transfer = TelegraphicTransferPage(self.driver)
        telegraphic_transfer.get_to_view_payment_page(self.instruction_id)
        sleep(5)
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_copy_button()
        sleep(3)
        telegraphic_transfer.enter_payment_details('Copy From TT')
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_preview_button()
        sleep(5)
        telegraphic_transfer.scroll_up_and_down(0, 2000)
        telegraphic_transfer.click_submit_button()
        self.success_message = telegraphic_transfer.get_success_message()

    def edit_TT(self):
        telegraphic_transfer = TelegraphicTransferPage(self.driver)
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

    def test_1_create_TT(self):
        self.create_TT()
        function.take_screenshot(self.driver, 'create_telegraphic_transfer.jpg')
        self.assertIn('has been created successfully', self.success_message)

    def test_2_copy_TT(self):
        self.create_TT()
        self.copy_TT()
        function.take_screenshot(self.driver, 'copy_telegraphic_transfer.jpg')
        self.assertIn('has been created successfully', self.success_message)

    def test_3_edit_TT(self):
        self.create_TT()
        self.edit_TT()
        function.take_screenshot(self.driver, 'edit_telegraphic_transfer.jpg')
        self.assertIn('has been modified successfully', self.success_message)
