from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage
from time import sleep

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: FastPaymentPage.py
@time: 2018/1/19 20:54
'''


class FastPaymentPage(PaymentPage):

    # purpose code的定位
    purpose_code_loc = (By.ID, 'reasonForPayment_anchor')
    purpose_code_filter_loc = (By.CLASS_NAME, 'filter_pp')
    purpose_code_value_loc = (By.CLASS_NAME, 'FilterTextcontain')

    def select_purpose_code(self):
        self.find_element(self.purpose_code_loc, clickable=True).click()
        self.find_element(self.purpose_code_filter_loc).send_keys('ALLW')
        sleep(1)
        self.find_element(self.purpose_code_value_loc, clickable=True).click()
