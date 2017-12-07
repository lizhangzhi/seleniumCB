from Util import *

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: paymentsPage.py
@time: 2017/8/17 15:46
编写payment菜单下页面的通用操作方法
'''


class PaymentPage(BasePage):

    fromaccount_loc = (By.ID, 'fromParty')
    paymentcurrency_loc = (By.ID, 'paymentCurrency_currencyCode')
    amount_loc = (By.ID, 'amount_value_control')
    beneficiary_loc = (By.ID, 'toParty')
    preview_button_loc = (By.ID, 'previewButton_Link')
    instruction_to_DBS_Bank_loc = (By.ID, 'messageToBank')
    submit_button_loc = (By.ID, 'submitButton_Link')
    success_message_loc = (By.ID, 'my_list')

    def select_from_account(self, account_text):
        self.select_dropdown(self.fromaccount_loc).select_by_visible_text(account_text)

    def select_payment_currency(self, currency):
        self.select_dropdown(self.paymentcurrency_loc).select_by_value(currency)

    def enter_amount(self, value):
        self.find_element(self.amount_loc).send_keys(value)

    def select_beneficiary(self):
        self.select_dropdown(self.beneficiary_loc).select_by_index(2)

    def enter_instruction(self, value):
        self.find_element(self.instruction_to_DBS_Bank_loc).send_keys(value)

    def click_preview_button(self):
        self.find_element(self.preview_button_loc).click()

    def click_submit_button(self):
        self.find_element(self.submit_button_loc).click()

    def get_success_message(self):
        return self.find_element(self.success_message_loc).text
