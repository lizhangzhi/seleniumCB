from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: BillPaymentPage.py
@time: 2018/3/29 17:05
'''


class BillPaymentPage(PaymentPage):
    """bill payment的page object"""

    # Billing Organisation下拉框的定位
    billing_organisation_loc = (By.XPATH, "//select[@id='boAutoArrayList_0__bo_organization']")
    # From Account的下拉框定位
    from_account_loc = (By.ID, 'boAutoArrayList_0__bo_debitAccount')
    # Bill Reference 输入框的定位
    bill_reference_loc = (By.ID, "boAutoArrayList_0__bo_billaccountnumber")
    # Amount 输入框的定位
    amount_loc = (By.XPATH, "//input[@id='boAutoArrayList_0__bo_amount']")
    # offline approve页面search section里reference的定位
    reference_loc = (By.XPATH, "//div[@id='tab-2fileOfflineApprovalCentre_Tabs']"
                               "/form/div[2]/div[2]/div/div/div[2]/div/div[8]/input")

    def select_billing_organisation(self, number):
        """选择billing organisation"""
        self.select_dropdown(self.billing_organisation_loc).select_by_index(number)

    def select_from_account(self, account_text):
        """选择from account"""
        self.select_dropdown(self.from_account_loc).select_by_visible_text(account_text)

    def enter_bill_reference(self, value):
        """输入bill reference值"""
        self.find_element(self.bill_reference_loc).send_keys(value)

    def enter_amount(self, value):
        """输入amount的值"""
        self.find_element(self.amount_loc).send_keys(value)

    def select_approver(self, approver_dropdown_loc, value):
        """在offline approve payment页面选择approver"""
        self.select_dropdown(approver_dropdown_loc).select_by_value(value)

    def enter_reference(self, reference_loc, value):
        """在offline approve list页面search section填入reference值"""
        self.find_element(reference_loc).send_keys(value)
