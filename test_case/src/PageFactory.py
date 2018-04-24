from test_case.src.cb.payments.FastPayment.FastPaymentPage import FastPaymentPage
from test_case.src.cb.payments.GiroPayment.GiroPaymentPage import GiroPaymentPage
from test_case.src.cb.payments.MakeAPaymentNew.MakeAPaymentPage import MakeAPaymentPage
from test_case.src.cb.payments.PartnerBankPayment.PartnerBankPaymentPage import PartnerBankPaymentPage
from test_case.src.cb.payments.TelegraphicTansfer.TelegraphicTransferPage import TelegraphicTransferPage
from test_case.src.cb.payments.CrossBorderACH.CrossBorderACHPage import CrossBorderACHPage
from test_case.src.cb.payments.BillPayment.BillPaymentPage import BillPaymentPage
from test_case.src.cb.payments.AccountTransfer.AccountTransferPage import AccountTransferPage
from test_case.src.cb.FileServices.UploadFile.UploadFilePage import UploadFilePage

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: PaymentsPageFactory.py
@time: 2018/3/23 18:10
'''


class PageFactory(object):
    """判断是否已经存在一个page的实例，是的话返回实例，不是的话实例化一个返回"""

    fast_payment_page = None
    giro_payment_page = None
    make_a_payment_page = None
    partner_bank_payment_page = None
    telegraphic_transfer_page = None
    cross_border_page = None
    bill_payment_page = None
    account_transfer_page = None
    upload_file_page = None

    @staticmethod
    def get_fast_payment_page_instance(driver):
        """fast payment的page实例"""
        if PageFactory.fast_payment_page is None:
            PageFactory.fast_payment_page = FastPaymentPage(driver)
        return PageFactory.fast_payment_page

    @staticmethod
    def get_giro_payment_page_instance(driver):
        """giro payment的page实例"""
        if PageFactory.giro_payment_page is None:
            PageFactory.giro_payment_page = GiroPaymentPage(driver)
        return PageFactory.giro_payment_page

    @staticmethod
    def get_make_a_payment_page_instance(driver):
        """make a payment的page实例"""
        if PageFactory.make_a_payment_page is None:
            PageFactory.make_a_payment_page = MakeAPaymentPage(driver)
        return PageFactory.make_a_payment_page

    @staticmethod
    def get_partner_bank_payment_page_instance(driver):
        """partner bank payment的page实例"""
        if PageFactory.partner_bank_payment_page is None:
            PageFactory.partner_bank_payment_page = PartnerBankPaymentPage(driver)
        return PageFactory.partner_bank_payment_page

    @staticmethod
    def get_telegraphic_transfer_page_instance(driver):
        """telegraphic transfer的page实例"""
        if PageFactory.telegraphic_transfer_page is None:
            PageFactory.telegraphic_transfer_page = TelegraphicTransferPage(driver)
        return PageFactory.telegraphic_transfer_page

    @staticmethod
    def get_cross_border_page_instance(driver):
        """cross border ach的page实例"""
        if PageFactory.cross_border_page is None:
            PageFactory.cross_border_page = CrossBorderACHPage(driver)
        return PageFactory.cross_border_page

    @staticmethod
    def get_bill_payment_page_instance(driver):
        """bill payment的page实例"""
        if PageFactory.bill_payment_page is None:
            PageFactory.bill_payment_page = BillPaymentPage(driver)
        return PageFactory.bill_payment_page

    @staticmethod
    def get_account_transfer_page_instance(driver):
        """account transfer的page实例"""
        if PageFactory.account_transfer_page is None:
            PageFactory.account_transfer_page = AccountTransferPage(driver)
        return PageFactory.account_transfer_page

    @staticmethod
    def get_upload_file_page_instance(driver):
        """account transfer的page实例"""
        if PageFactory.upload_file_page is None:
            PageFactory.upload_file_page = UploadFilePage(driver)
        return PageFactory.upload_file_page

    @staticmethod
    def clean_page_instance():
        """一个实例只能在一个用例中运行，所以在用例结尾调这个函数，将变量重置为None,供下一次使用"""
        if PageFactory.fast_payment_page is not None:
            PageFactory.fast_payment_page = None
        if PageFactory.giro_payment_page is not None:
            PageFactory.giro_payment_page = None
        if PageFactory.make_a_payment_page is not None:
            PageFactory.make_a_payment_page = None
        if PageFactory.partner_bank_payment_page is not None:
            PageFactory.partner_bank_payment_page = None
        if PageFactory.telegraphic_transfer_page is not None:
            PageFactory.telegraphic_transfer_page = None
        if PageFactory.cross_border_page is not None:
            PageFactory.cross_border_page = None
        if PageFactory.bill_payment_page is not None:
            PageFactory.bill_payment_page = None
        if PageFactory.account_transfer_page is not None:
            PageFactory.account_transfer_page = None
        if PageFactory.upload_file_page is not None:
            PageFactory.upload_file_page = None
