from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage
# from time import sleep

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: PartnerBankPaymentPage.py
@time: 2018/1/19 18:57
'''


class PartnerBankPaymentPage(PaymentPage):
    # Partner Bank Country的定位
    country_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname= 'countrySelected']")
    country_value_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname= 'countrySelected']/div/div[2]/div[1]/span")
    # Payment Type的定位
    type_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='ptnbnkPmtSelect']")
    type_value_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='ptnbnkPmtSelect']/div/div[2]/div[4]/span")
    # Payee部分显示confidential信息的定位
    payee_ux_loc = (By.XPATH, "//div[@class='payee-list']/div[3]/p")
    # Payee部分有显示payee的定位
    item_ux_loc = (By.XPATH, "//div[@class='payee-list']/filter-item-component/section")

    def select_country_ux(self):
        self.find_element(self.country_ux_loc).click()
        self.find_element(self.country_value_ux_loc).click()

    def select_type_ux(self):
        self.find_element(self.type_ux_loc).click()
        self.find_element(self.type_value_ux_loc).click()

    def get_payee_confidential_ux(self):
        return self.find_element(self.payee_ux_loc).text

    def get_payee_list_ux(self):
        return self.find_element(self.item_ux_loc)
