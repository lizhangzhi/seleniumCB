from Util import *
from time import sleep

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: paymentsPage.py
@time: 2017/8/17 15:46
编写payment菜单下页面的通用操作方法
'''


class PaymentPage(BasePage):
    """Payment Create/Preview/Edit/View/Copy等页面基本操作的page object"""

    def switch_to_frame(self, out=False):
        """切换frame

        out：为True时代表切换出frame
        """
        frame_loc = (By.ID, 'iframe1')
        self.switch_frame(frame_loc, out)

    def select_from_account(self, from_account_loc='', account_number='', ux_flag=False,
                            account_ux_loc='', account_value_ux_loc=''):
        """选择from account

        account_number：所要选择的account number
        ux_flag:为True时，这个方法适用于UX页面
        account_ux_loc：UX页面account下拉框的定位
        account_value_ux_loc： UX页面输入account number后，查询到的值的定位
        """
        if from_account_loc:
            from_account_loc = from_account_loc
        else:
            from_account_loc = (By.ID, 'fromParty')

        if ux_flag:
            self.find_element(account_ux_loc, clickable=True).click()
            self.find_element(account_ux_loc, clickable=True).send_keys(account_number)
            self.find_element(account_value_ux_loc, clickable=True).click()
        else:
            self.select_dropdown(from_account_loc).select_by_visible_text(account_number)

    def select_payment_currency(self, payment_currency_loc='', currency='', ux_flag=False,
                                currency_ux_loc='', currency_textbox_ux_loc='', currency_value_ux_loc=''):
        """选择payment currency

        currency：要选择的currency
        ux_flag：为True时，这个方法适用于UX页面
        currency_ux_loc  currency_textbox_ux_loc：UX页面payment currency下拉框的定位
        currency_value_ux_loc：UX页面输入currency后，查询到的值的定位
        """
        if payment_currency_loc:
            payment_currency_loc = payment_currency_loc
        else:
            payment_currency_loc = (By.ID, 'paymentCurrency_currencyCode')

        if ux_flag:
            self.find_element(currency_ux_loc, clickable=True).click()
            self.find_element(currency_textbox_ux_loc, clickable=True).send_keys(currency)
            self.double_click(loc=currency_value_ux_loc)
        else:
            self.select_dropdown(payment_currency_loc).select_by_value(currency)

    def select_country(self, country_ux_loc, country_value_ux_loc, value):
        """选择国家"""
        self.find_element(country_ux_loc, clickable=True).click()
        self.find_element(country_ux_loc, clickable=True).send_keys(value)
        self.find_element(country_value_ux_loc, clickable=True).click()

    def select_beneficiary(self, beneficiary_loc='', value='', ux_single=False, ux_bulk=False,
                           beneficiary_ux_loc='', beneficiary_value_ux_loc=''):
        """选择beneficiary

        number：旧页面beneficiary下拉框下所要选择值的顺序
        ux_single：为True时，这个方法适用于UX页面single类型的payment
        ux_bulk：为True时，这个方法适用于UX页面bulk类型的payment
        beneficiary_ux_loc：UX页面beneficiary下拉框的定位
        beneficiary_value_ux_loc：UX页面输入beneficiary后，查询到的值的定位
        """
        if beneficiary_loc:
            beneficiary_loc = beneficiary_loc
        else:
            beneficiary_loc = (By.ID, 'toParty')

        if ux_single:
            self.find_element(beneficiary_ux_loc, clickable=True).click()
            self.find_element(beneficiary_ux_loc, clickable=True).send_keys(value)
            self.double_click(loc=beneficiary_value_ux_loc)
        elif ux_bulk:
            self.find_element(beneficiary_ux_loc, clickable=True).click()
        else:
            self.select_dropdown(beneficiary_loc).select_by_index(value)

    def enter_amount(self, amount_loc='', value='', ux_flag=False):
        """输入amount
        ux_flag：为True时，这个方法适用于UX页面
        amount_ux_loc：UX页面amount文本框的定位
        """

        if ux_flag:
            self.find_element(amount_loc).clear()
            self.find_element(amount_loc).send_keys(value)
        else:
            if amount_loc:
                amount_loc = amount_loc
            else:
                amount_loc = (By.ID, 'amount_value_control')
            self.find_element(amount_loc).send_keys(value)

    def enter_payment_details(self, payment_details_loc='', value='', ux_flag=False):
        """输入payment details
        ux_flag：为True时，这个方法适用于UX页面
        payment_details_ux_loc：UX页面payment details文本框的定位
        """

        if ux_flag:
            self.find_element(payment_details_loc, clickable=True).send_keys(value)
        else:
            if payment_details_loc:
                payment_details_loc = payment_details_loc
            else:
                payment_details_loc = (By.ID, 'details')
            self.find_element(payment_details_loc).send_keys(value)

    def select_purpose_code(self, ux_flag=False,
                            purpose_code_loc='', purpose_code_filter_loc='', purpose_code_value_loc=''):
        """选择purpose code

        ux_flag：为True时，这个方法适用于UX页面
        purpose_code_ux_loc：UX页面purpose code下拉框的定位
        purpose_code_value_ux_loc：UX页面输入purpose code后，查询到的值的定位
        """
        if ux_flag:
            self.find_element(purpose_code_loc, clickable=True).click()
            self.find_element(purpose_code_value_loc).click()
        else:
            self.find_element(purpose_code_loc, clickable=True).click()
            self.find_element(purpose_code_filter_loc).send_keys('ALLW')
            sleep(1)
            self.find_element(purpose_code_value_loc, clickable=True).click()

    def select_bank_charges(self, ux_flag=False, bank_charges_loc=''):
        """选择bank charges

        ux_flag：为True时，这个方法适用于UX页面
        bank_charges_ux_loc：UX页面bank charge checkbox的定位
        """
        if ux_flag:
            self.find_element(bank_charges_loc, clickable=True).click()
        else:
            print("Don't have old ui part yet.Please modify the method")

    def get_success_message(self, success_message_loc='', ux_flag=False, success_message_ux_loc=''):
        """获取成功的message

        ux_flag：为True时，这个方法适用于UX页面
        """
        if success_message_loc or success_message_ux_loc:
            success_message_loc = success_message_loc
            success_message_ux_loc = success_message_ux_loc
        else:
            success_message_loc = (By.ID, 'my_list')
            success_message_ux_loc = (By.XPATH, "//div[@class='alert alert-info']/ul/li/label")

        if ux_flag:
            return self.find_element(success_message_ux_loc).text
        else:
            return self.find_element(success_message_loc).text

    def click_preview_button(self, preview_button_loc='', ux_flag=False):
        """在create/edit payment页面点击preview按钮

        ux_flag：为True时，这个方法适用于UX页面
        next_button_ux_loc：UX create/edit页面的next按钮的定位
        """
        if ux_flag and preview_button_loc:
            self.find_element(preview_button_loc, clickable=True).click()
        else:
            if preview_button_loc:
                preview_button_loc = preview_button_loc
            else:
                preview_button_loc = (By.ID, 'previewButton_Link')
            self.find_element(preview_button_loc, clickable=True).click()

    def wait_page_load(self, loc):
        """等待页面加载"""
        self.find_element(loc)

    def click_submit_button(self, submit_button_loc='', ux_flag=False):
        """在preview页面点击submit按钮

        ux_flag：为True时，这个方法适用于UX页面
        submit_button_ux_loc：UX preview页面的submit按钮的定位
        """
        if ux_flag and submit_button_loc:
            self.find_element(submit_button_loc, clickable=True).click()
        else:
            if submit_button_loc:
                submit_button_loc = submit_button_loc
            else:
                submit_button_loc = (By.ID, 'submitButton_Link')
            self.find_element(submit_button_loc, clickable=True).click()

    def click_save_as_template_checkbox(self, value):
        """执行save as template操作"""
        save_as_template_checkbox_loc = (By.ID, 'saveAsTemplate')
        template_name_loc = (By.ID, 'templateName')

        self.find_element(save_as_template_checkbox_loc, clickable=True).click()
        self.find_element(template_name_loc).send_keys(value)

    def click_delete_button_loc(self, delete_button_loc=''):
        """view页面执行delete操作"""
        if delete_button_loc:
            delete_button_loc = delete_button_loc
        else:
            delete_button_loc = (By.ID, 'deleteButton_Link')
        self.find_element(delete_button_loc, clickable=True).click()

    def click_reject_button(self, reject_button_loc=''):
        """view页面执行reject操作"""
        if reject_button_loc:
            reject_button_loc = reject_button_loc
        else:
            reject_button_loc = (By.ID, 'rejectButton_Link')
        self.find_element(reject_button_loc, clickable=True).click()

    def click_approve_button(self, approve_button_loc):
        """执行approve操作

        approve_button_loc：approve 按钮的定位
        """
        self.find_element(approve_button_loc, clickable=True).click()

    def enter_approve_response(self, value, approve_response_loc=''):
        """输入response的值"""
        if approve_response_loc:
            approve_response_loc = approve_response_loc
        else:
            approve_response_loc = (By.ID, 'signature')

        self.find_element(approve_response_loc).send_keys(value)

    def click_approve_now_checkbox(self, approve_now_checkbox_loc=''):
        """勾选approve now的checkbox"""
        if approve_now_checkbox_loc:
            approve_now_checkbox_loc = approve_now_checkbox_loc
        else:
            approve_now_checkbox_loc = (By.ID, 'approvalChoice_B')
        self.find_element(approve_now_checkbox_loc, clickable=True).click()

    def click_copy_button(self):
        """点击copy按钮"""
        copy_button_loc = (By.ID, 'copyButton_Link')
        self.find_element(copy_button_loc, clickable=True).click()

    def click_edit_button(self, ux_flag=False, edit_button_loc=''):
        """点击edit按钮

        ux_flag：为True时，这个方法适用于UX页面
        approve_button_loc：approve 按钮的定位
        """

        if ux_flag and edit_button_loc:
            self.find_element(edit_button_loc, clickable=True).click()
        else:
            if edit_button_loc:
                edit_button_loc = edit_button_loc
            else:
                edit_button_loc = (By.XPATH, "//*[@id='modifyButton_Link']")
            self.find_element(edit_button_loc, clickable=True).click()

    def login_cb(self, url, login_id, company_id):
        """登陆CB端的方法 （嗯...以前为啥要写在这里...，好奇怪，懒得改了，算了）"""
        login = LoginPage(self.driver)
        login.logincb(url, login_id, company_id)

# Center/List 页面一些通用操作
    def click_filter_button(self, filter_button_loc=''):
        """点击filter按钮，打开filter模块"""
        if filter_button_loc:
            filter_button_loc = filter_button_loc
        else:
            filter_button_loc = (By.ID, 'pendingA')
        self.find_element(filter_button_loc, clickable=True).click()

    def enter_reference(self, reference_loc='', value=''):
        """在filter模块输入reference值"""
        if reference_loc:
            reference_loc = reference_loc
        else:
            reference_loc = (By.ID, 'filterReference')
        self.find_element(reference_loc).send_keys(value)

    def click_go_button(self, go_button_loc=''):
        """在filter部分点击go按钮"""
        if go_button_loc:
            go_button_loc = go_button_loc
        else:
            go_button_loc = (By.ID, 'ButtonCtrl_Link')
        self.find_element(go_button_loc, clickable=True).click()

    def click_reference_link(self, reference):
        """点击reference链接跳转"""
        reference_loc = (By.LINK_TEXT, reference)
        self.find_element(reference_loc, clickable=True).click()

    def enter_file_name(self, file_name_loc, filename):
        """在filter部分输入file name"""
        self.find_element(file_name_loc).send_keys(filename)

    def click_file_name_link(self, filename):
        """点击搜索出来的file name的链接"""
        self.find_element((By.LINK_TEXT, filename)).click()

# To View Page
    def get_to_view_payment_page(self, instruction_id):
        """Transfer Center点击reference link到指定payment的view页面"""
        payment_page = PaymentPage(self.driver)
        payment_page.open_menu("Payments", "Transfer Center")
        payment_page.click_filter_button()
        payment_page.enter_reference(value=instruction_id)
        payment_page.click_go_button()
        payment_page.click_reference_link(instruction_id)

# choose a tab in list page
    def click_tab(self, tab_loc):
        self.find_element(tab_loc).click()
