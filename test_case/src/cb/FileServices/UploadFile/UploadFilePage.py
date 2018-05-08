from Util import *
from test_case.src.cb.payments.paymentsPage import PaymentPage
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: UploadFilePage.py
@time: 2018/4/10 14:09
'''


class UploadFilePage(PaymentPage):
    """Upload File页面的page object"""
    # Type 下拉框的定位
    type_loc = (By.NAME, "fileType")
    # File Format 下拉框的定位
    file_format_loc = (By.NAME, "fileFormat")
    # File Name选择文件按钮的定位
    file_name_loc = (By.ID, "theFile")
    # Approval Option下拉框的定位
    approval_option_loc = (By.NAME, "aprvlOptn")
    # Approval Currency下拉框的定位
    approval_currency_loc = (By.NAME, "aprvlCrny")
    # Upload File按钮的定位
    upload_file_button_loc = (By.ID, "text")
    # Manage File页面refresh按钮的定位
    refresh_button_loc = (By.ID, "refresh")
    # Approve File页面submit按钮的定位
    submit_button_loc = (By.ID, 'submitButton_Link')

    def select_type(self, file_type):
        """选择Type下拉框的值"""
        self.select_dropdown(self.type_loc).select_by_value(file_type)

    def select_file_format(self, file_format):
        """选择File Format下拉框的值"""
        self.select_dropdown(self.file_format_loc).select_by_value(file_format)

    def choose_file_name_to_upload(self, file_path):
        """点击浏览按钮，输入上传文件的路径"""
        self.find_element(self.file_name_loc).send_keys(file_path)

    def select_approval_option(self, approval_option):
        """选择Approval Option下拉框的值"""
        self.select_dropdown(self.approval_option_loc).select_by_value(approval_option)

    def select_approval_currency(self, currency):
        """选择Approval Currency下拉框的值"""
        self.select_dropdown(self.approval_currency_loc).select_by_value(currency)

    def click_upload_file_button(self):
        """点击Upload File按钮"""
        self.find_element(self.upload_file_button_loc).click()

    def click_refresh_button(self):
        """点击Manage File 页面 refresh按钮"""
        self.find_element(self.refresh_button_loc).click()

    def get_uploaded_file_link_attr(self, filename):
        """获取文件上传成功后，在manage file页面的link属性"""
        return self.find_element((By.LINK_TEXT, filename)).get_attribute("href")
