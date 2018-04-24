from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: CrossBorderACHPage.py
@time: 2018/3/29 15:17
'''


class CrossBorderACHPage(PaymentPage):

    # Account的定位
    account_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='fromAccount']/div/input")
    account_value_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='fromAccount']/div/div[2]/div/span")
    # Country的定位
    country_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname= 'countrySelected']/div/input")
    country_value_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname= 'countrySelected']/div/div[2]/div/span")
    # Debit Type的定位
    debit_type_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname= 'debitTypeObjectSelected']/div/input")
    debit_type_value_ux_loc = (By.XPATH,
                               "//auto-complete[@formcontrolname= 'debitTypeObjectSelected']/div/div[2]/div/span")
    # Beneficiary 的定位（选择existing beneficiary的第一个bene)
    beneficiary_ux_loc = (By.XPATH, "//div[@class='payee-list']/filter-item-component[1]/section/div/div/div/button")
    # Amount的定位
    amount_ux_loc = (By.XPATH, "//dbs-input[@formcontrolname='payeeAmount']/span/div/input")
    # next button的定位
    next_button_ux_loc = (By.XPATH, "//button[@translate = 'labelPreviewTransfer']")
    # preview页面edit icon的定位
    edit_icon_loc = (By.CLASS_NAME, "icon-edit")
    # submit button的定位
    submit_button_ux_loc = (By.CLASS_NAME, "btn.btn-dbs-solid.next")

    def select_debit_type_ux(self, debit_type_ux_loc, debit_type_value_ux_loc, value):
        """Cross Border ACH 页面选择Debit Type的值"""
        self.find_element(debit_type_ux_loc, clickable=True).click()
        self.find_element(debit_type_ux_loc, clickable=True).send_keys(value)
        self.find_element(debit_type_value_ux_loc, clickable=True).click()
