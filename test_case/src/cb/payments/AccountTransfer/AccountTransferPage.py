from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: AccountTransferPage.py
@time: 2018/4/3 16:17
'''


class AccountTransferPage(PaymentPage):
    """account transfer 的page object"""

    # TW : Domestic/ Overseas Outward Remittance的下拉框定位
    outward_remittance_loc = (By.ID, "remittanceType")
    # TW : Purpose Code的下拉框定位
    purpose_code_loc = (By.ID, "reasonForPayment_anchor")
    purpose_code_filter_loc = (By.CLASS_NAME, "filter_pp")
    purpose_code_filter_value_loc = (By.CLASS_NAME, "FilterTextChild")
    # TW : Payment Date的定位
    payment_date_loc = (By.ID, "executionDate")

    def select_outward_remittance(self, value):
        """选择outward remittance"""
        self.select_dropdown(self.outward_remittance_loc).select_by_index(value)

    def payment_date_display(self):
        """判断payment date原本的输入框是否是可见的"""
        return self.find_element(self.payment_date_loc, presence=True).is_displayed()
