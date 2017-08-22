from test_case.src.cb.payments.paymentsPage import PaymentPage

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: TelegraphicTransferPage.py
@time: 2017/8/17 15:39
'''


def create_telegraphic_transfer(driver):

	PaymentPage(driver).open_paymentmenulist()
	PaymentPage(driver).to_telegraphictransfer()
	PaymentPage(driver).select_fromaccount()
	PaymentPage(driver).select_paymentcurrency()
	PaymentPage(driver).enter_amount('10')
	PaymentPage(driver).select_beneficiary()
