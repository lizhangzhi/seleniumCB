from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: GiroPaymentPage.py
@time: 2018/1/22 10:25
'''


class GiroPaymentPage(PaymentPage):

    # amount输入框的定位
    amount_loc = (By.ID, 'amount_value')
    # center页面查找到的transaction前的checkbox的定位
    transaction_checkbox_loc = (By.ID, "0-TransferCenter_pending")
    # Center页面Add To New Group按钮的定位
    add_to_new_group_button_loc = (By.ID, "addPmtToNewGroupButtonpending_Link")
    # Preview Group按钮的定位
    preview_group_button_loc = (By.ID, "submitButton_Link")
    # approval list页面By Group tab的定位
    by_group_tab_loc = (By.XPATH, "//a[@tabid='groupingTab']")
    # approval list 页面By Group tab下，Go按钮的定位
    approval_list_go_button_loc = (By.ID, "submitgrouping_Link")
    # approve group按钮的定位
    approve_group_button_loc = (By.ID, "approveGrpButton_Link")
    # approve payment按钮的定位
    approve_payment_button_loc = (By.ID, 'approveButton_Link')

    def select_transaction_in_center(self):
        """在center页面勾选所查到的transaction前的checkbox"""
        self.find_element(self.transaction_checkbox_loc).click()

    def click_add_to_new_group_button(self):
        """点击Add To New Group按钮"""
        self.find_element(self.add_to_new_group_button_loc).click()

    def click_preview_group_button(self):
        """在Create Group或者Edit Group页面点击Preview Group按钮"""
        self.find_element(self.preview_group_button_loc).click()

    def click_submit_group_button(self):
        """在preview group页面点击submit group按钮"""
        self.find_elements(self.preview_group_button_loc).pop().click()

    def click_approve_group_button(self):
        """点击Approve Group按钮"""
        self.find_element(self.approve_group_button_loc).click()
