import time
import sys
import logging
from Util import *
from .UploadFilePage import UploadFilePage
from test_case.src.PageFactory import PageFactory
from test_case.src.cb.Approvals.MyApprovalsPage import MyApprovalsPage
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: UploadFile_sta.py
@time: 2018/4/10 14:09
'''


class UploadFileTest(MyUnittest):

    def upload_file(self, file_type, file_format, file_path, approval_option, approval_currency, filename):
        upload_file_page = PageFactory.get_upload_file_page_instance(self.driver)
        login_page = LoginPage(self.driver)
        login_page.logincb(self.url, self.login_id, self.company_id)
        upload_file_page.open_menu("File Services", "Upload File")
        upload_file_page.select_type(file_type)
        upload_file_page.select_file_format(file_format)
        time.sleep(1)
        upload_file_page.choose_file_name_to_upload(file_path)
        upload_file_page.select_approval_option(approval_option)
        upload_file_page.select_approval_currency(approval_currency)
        upload_file_page.click_upload_file_button()
        upload_file_page.click_refresh_button()
        time.sleep(1)
        self.href_attr = upload_file_page.get_uploaded_file_link_attr(filename)

    @log(logger=logging.getLogger(__name__))
    def test_1_upload_file(self):
        """测试能在File Service下成功上传文件"""
        try:
            file_path = sys.path[1].replace("/", "\\") + "\\" + "uploadfile"
            self.file_path, filename = search_file(file_path, "SGUploadFile-")
            self.upload_file("ALL", "UFF", self.file_path, "0", "SGD,2203003,5", filename)
            take_screenshot(self.driver, '35_file_service_upload_file.jpg')
            self.assertIsNotNone(self.href_attr)
        finally:
            change_name(self.file_path, separator="-", word=str(time.time()), suffix=".txt")
            PageFactory.clean_page_instance()

    @log(logger=logging.getLogger(__name__))
    def test_2_approve_file(self):
        """测试能在My Aprpoval List-By File 下进入view file页面进行approve"""
        try:
            file_path = sys.path[1].replace("/", "\\") + "\\" + "uploadfile"
            self.file_path, filename = search_file(file_path, "SGUploadFile-")
            self.upload_file("ALL", "UFF", self.file_path, "0", "SGD,2203003,5", filename)
            upload_file_page = PageFactory.get_upload_file_page_instance(self.driver)
            upload_file_page.open_menu("Payments", "My Approvals")
            upload_file_page.click_tab(MyApprovalsPage.list_per_file_tab_loc)
            upload_file_page.enter_file_name(MyApprovalsPage.filter_file_name_loc, filename)
            upload_file_page.click_go_button(MyApprovalsPage.pert_transaction_go_button_loc)
            upload_file_page.click_file_name_link(filename)
            upload_file_page.wait_page_load(MyApprovalsPage.page_load_loc)
            upload_file_page.scroll_up_and_down(0, 1000)
            upload_file_page.click_approve_button(MyApprovalsPage.approve_file_button_loc)
            upload_file_page.enter_approve_response(UploadFilePage.approve_response_loc, "approve")
            upload_file_page.click_approve_button(UploadFilePage.submit_button_loc)
            self.success_message = upload_file_page.get_success_message()
            take_screenshot(self.driver, '26_file_service_approve_file.jpg')
            self.assertIn('has been approved successfully', self.success_message)
        finally:
            change_name(self.file_path, separator="-", word=str(time.time()), suffix=".txt")
            PageFactory.clean_page_instance()
