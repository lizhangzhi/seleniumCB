from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: GiroPaymentPage.py
@time: 2018/1/22 10:25
'''


class GiroPaymentPage(PaymentPage):

    amount_loc = (By.ID, 'amount_value')

    def enter_amount(self, value):
        self.find_element(self.amount_loc).send_keys(value)
