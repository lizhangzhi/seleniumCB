from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage
from time import sleep

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: TelegraphicTransferPage.py
@time: 2018/1/19 19:43
'''


class TelegraphicTransferPage(PaymentPage):

    instruction_to_DBS_Bank_loc = (By.ID, 'messageToBank')

    def enter_instruction(self, value):
        self.find_element(self.instruction_to_DBS_Bank_loc).send_keys(value)

