from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: PartnerBankPaymentPage.py
@time: 2018/1/19 18:57
'''


class PartnerBankPaymentPage(PaymentPage):

    # Account的定位
    account_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='fromAccount']/div/input")
    account_value_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='fromAccount']/div/div[2]/div/span")
    # Amount的定位
    amount_ux_loc = (By.XPATH, "//dbs-input[@formcontrolname='payeeAmount']/span/div/input")
    # Country的定位
    country_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname= 'countrySelected']")
    country_value_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname= 'countrySelected']/div/div[2]/div[1]/span")
    # Beneficiary 的定位（选择existing beneficiary的第一个bene)
    beneficiary_ux_loc = (By.XPATH, "//div[@class='payee-list']/filter-item-component[1]/section/div/div/div/button")
    # Payment Type的定位
    type_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='ptnbnkPmtSelect']")
    type_value_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='ptnbnkPmtSelect']/div/div[2]/div[4]/span")
    # Payee部分显示confidential信息的定位
    payee_ux_loc = (By.XPATH, "//div[@class='payee-list']/div[3]/p")
    # Payee部分有显示payee的定位
    item_ux_loc = (By.XPATH, "//div[@class='payee-list']/filter-item-component/section")
    # hash value字段定位
    hash_value_loc = (By.XPATH, "//*[@translate='bulk.labelHashValue4PtnBnk']")
    # next button的定位
    next_button_ux_loc = (By.XPATH, "//button[@translate = 'labelPreviewTransfer']")
    # next button的定位
    submit_button_ux_loc = (By.XPATH, "//button[@translate = 'labelSubmit']")
    # edit button的定位
    edit_icon_ux_loc = (By.XPATH, "//label[@translate='labelEdit']")
    # approve button的定位
    approve_button_ux_loc = (By.XPATH, "//div[@class='form-group no-print']/div/button[5]")
    # response 输入框定位
    response_ux_loc = (By.XPATH, "//dbs-input[@name='responseCode']/span/div/input")
    # approve message的定位
    approve_success_message_ux_loc = (By.XPATH, "//md-dialog-container[@class='mat-dialog-container']")

    def select_country_ux(self):
        self.find_element(self.country_ux_loc, clickable=True).click()
        self.find_element(self.country_value_ux_loc, clickable=True).click()

    def select_type_ux(self):
        self.find_element(self.type_ux_loc, clickable=True).click()
        self.find_element(self.type_value_ux_loc, clickable=True).click()

    def get_payee_confidential_ux(self):
        return self.find_element(self.payee_ux_loc).text

    def get_payee_list_ux(self):
        return self.find_element(self.item_ux_loc)

    def wait_view_page_load(self):
        self.find_element(self.hash_value_loc)
