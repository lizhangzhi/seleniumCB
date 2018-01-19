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
        sleep(5)
        telegraphic_transfer.open_menu("Payments", "Telegraphic Transfer")
        telegraphic_transfer.select_from_account('LEONA ALBRECHT - 0018001843 - SGD')
        telegraphic_transfer.select_payment_currency('SGD')
        telegraphic_transfer.enter_amount('10')
        telegraphic_transfer.select_beneficiary()
        telegraphic_transfer.enter_instruction('Instruction to DBS Bank')
        telegraphic_transfer.scroll_down()
        telegraphic_transfer.click_preview_button()
        sleep(3)
        telegraphic_transfer.scroll_down()
        telegraphic_transfer.click_submit_button()
        self.success_message = telegraphic_transfer.get_success_message()

    def test_createTT(self):
        # function.take_screenshot(self.driver, 'create tt.jpg')
        self.create_TT()
        self.assertIn('has been created successfully', self.success_message)
