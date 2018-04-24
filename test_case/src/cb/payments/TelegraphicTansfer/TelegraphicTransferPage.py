from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: TelegraphicTransferPage.py
@time: 2018/1/19 19:43
'''


class TelegraphicTransferPage(PaymentPage):

    # Instruction To DBS Bank 文本框的定位
    instruction_to_DBS_Bank_loc = (By.ID, 'messageToBank')
    # Approval list 页面By Transaction tab下，Go按钮的定位
    approval_list_go_button_loc = (By.ID, "submitpending_Link")
    # list 页面查找到的transaction前的checkbox的定位
    transaction_checkbox_loc = (By.ID, "0-FileApprovalList_pending")
    # list 页面approve按钮的定位
    my_approval_approve_button_loc = (By.ID, "approveButtonpending_Link")
    # Approve Payment 按钮的定位
    approve_payment_button_loc = (By.ID, 'submitButton_Link')
    # my approval list页面search section里reference的定位
    reference_loc = (By.XPATH, "//div[@id='tab-2fileApprovalCentre_Tabs']"
                               "/form/div[2]/div[2]/div/div/div[2]/div/div[6]/input")

    def enter_instruction(self, value):
        self.find_element(self.instruction_to_DBS_Bank_loc).send_keys(value)

    def select_transaction_in_list(self):
        """在center页面勾选所查到的transaction前的checkbox"""
        self.find_element(self.transaction_checkbox_loc).click()