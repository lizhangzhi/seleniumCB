import logging
from Util import *
from .FileUploadEnquiryPage import FileUploadEnquiryPage
# -*- coding: utf-8 -*-
__author__ = 'janet'
'''
@file: FileUploadEnquiry_sta.py
@time: 2018/4/10 14:09
'''


class FileUploadEnquiryTest(MyUnittest):

    def file_upload_enquiry(self):
        login_page = LoginPage(self.driver)
        login_page.logincb(self.url, self.sam_login_id, "", login_sam=True)
        file_upload_enquiry_page = FileUploadEnquiryPage(self.driver)
        file_upload_enquiry_page.open_menu("OPERATIONS", "FILE UPLOAD ENQUIRY")
        file_upload_enquiry_page.enter_start_date("01-Apr-2018")
        file_upload_enquiry_page.click_search_button()
        file_upload_enquiry_page.click_filename_link()
        file_upload_enquiry_page.click_reference_link()
        file_upload_enquiry_page.click_print_button()
        self.success_message = file_upload_enquiry_page.get_session_text()

    @log(logger=logging.getLogger(__name__))
    def test_file_upload_enquiry(self):
        """在SAM>OPERATIONS>FILE UPLOAD ENQUIRY页面查看数据是否正常显示"""
        self.file_upload_enquiry()
        function.take_screenshot(self.driver, '34_file_upload_enquiry.jpg')
        self.assertIn('Transaction Information', self.success_message)
