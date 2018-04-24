from Util import *

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: paymentsPage.py
@time: 2017/8/17 15:46
编写payment菜单下页面的通用操作方法
'''


class PaymentPage(BasePage):

    # Old UI
    from_account_loc = (By.ID, 'fromParty')
    payment_currency_loc = (By.ID, 'paymentCurrency_currencyCode')
    amount_loc = (By.ID, 'amount_value_control')
    beneficiary_loc = (By.ID, 'toParty')
    payment_details_loc = (By.ID, 'details')
    success_message_loc = (By.ID, 'my_list')
    list_per_transaction_tab_loc = (By.XPATH, "//a[@tabid='pendingTab']")

# UX
    frame_loc = (By.ID, 'iframe1')
    success_message_ux_loc = (By.XPATH, "//div[@class='alert alert-info']/ul/li/label")

# Preview
    # old ui
    preview_button_loc = (By.ID, 'previewButton_Link')
    # ux

# Submit
    # old ui
    submit_button_loc = (By.ID, 'submitButton_Link')
    # ux

# Save as Template
    # old ui
    save_as_template_checkbox_loc = (By.ID, 'saveAsTemplate')
    template_name_loc = (By.ID, 'templateName')

# Delete
    # old ui
    delete_button_loc = (By.ID, 'deleteButton_Link')

# Reject
    # old ui
    reject_button_loc = (By.ID, 'rejectButton_Link')

# Approve
    # old ui
    approve_payment_button_loc = (By.ID, 'approveButton_Link')
    # ux
    challenge_button_ux_loc = (By.XPATH, "//*[@class='challenge-button-get']/button")

# Approve Now
    # old ui
    approve_now_checkbox_loc = (By.ID, 'approvalChoice_B')
    approve_response_loc = (By.ID, 'signature')

# Edit
    # old ui
    edit_button_loc = (By.XPATH, "//*[@id='modifyButton_Link']")
    preview_button_edit_page_loc = (By.XPATH, "//*[@class='ctrlBtnGrp']/a[3]")
    # ux

# Copy
    # old UI
    copy_button_loc = (By.ID, 'copyButton_Link')

# Transfer Center
    filter_button_loc = (By.ID, 'pendingA')
    reference_loc = (By.ID, 'filterReference')
    go_button_loc = (By.ID, 'ButtonCtrl_Link')

# Offline Approval List
    offline_approval_go_button_loc = (By.ID, 'submitpending_Link')
    approver_dropdown_loc = (By.ID, "offapproverId")

# Old UI
    def select_from_account(self, account_text):
        self.select_dropdown(self.from_account_loc).select_by_visible_text(account_text)

    def select_payment_currency(self, currency):
        self.select_dropdown(self.payment_currency_loc).select_by_value(currency)

    def enter_amount(self, value):
        self.find_element(self.amount_loc).send_keys(value)

    def select_beneficiary(self, number):
        self.select_dropdown(self.beneficiary_loc).select_by_index(number)

    def enter_payment_details(self, value):
        self.find_element(self.payment_details_loc).send_keys(value)

    def get_success_message(self):
        return self.find_element(self.success_message_loc).text

# UX
    def switch_to_frame(self, out=False):
        self.switch_frame(self.frame_loc, out)

    def select_account_ux(self, account_ux_loc, account_value_ux_loc, account_number):
        self.find_element(account_ux_loc, clickable=True).click()
        self.find_element(account_ux_loc, clickable=True).send_keys(account_number)
        self.find_element(account_value_ux_loc, clickable=True).click()

    def select_country_ux(self, country_ux_loc, country_value_ux_loc, value):
        self.find_element(country_ux_loc, clickable=True).click()
        self.find_element(country_ux_loc, clickable=True).send_keys(value)
        self.find_element(country_value_ux_loc, clickable=True).click()

    def select_payment_currency_ux(self, currency_ux_loc, currency_textbox_ux_loc, currency_value_ux_loc, currency):
        self.find_element(currency_ux_loc, clickable=True).click()
        self.find_element(currency_textbox_ux_loc, clickable=True).send_keys(currency)
        self.double_click(loc=currency_value_ux_loc)

    def select_beneficiary_bulk_ux(self, beneficiary_ux_loc):
        self.find_element(beneficiary_ux_loc, clickable=True).click()

    def select_beneficiary_single_ux(self, beneficiary_ux_loc, beneficiary_value_ux_loc, value):
        self.find_element(beneficiary_ux_loc, clickable=True).click()
        self.find_element(beneficiary_ux_loc, clickable=True).send_keys(value)
        self.double_click(loc=beneficiary_value_ux_loc)
        # self.find_element(self.beneficiary_value_ux_loc).click()

    def enter_amount_ux(self, amount_ux_loc, value):
        self.find_element(amount_ux_loc).clear()
        self.find_element(amount_ux_loc).send_keys(value)

    def select_purpose_code_ux(self, purpose_code_ux_loc, purpose_code_value_ux_loc):
        self.find_element(purpose_code_ux_loc, clickable=True).click()
        self.find_element(purpose_code_value_ux_loc).click()

    def select_bank_charges_ux(self, bank_charges_ux_loc):
        self.find_element(bank_charges_ux_loc, clickable=True).click()

    def enter_payment_details_ux(self, payment_details_ux_loc, value):
        self.find_element(payment_details_ux_loc, clickable=True).send_keys(value)

    def get_success_message_ux(self):
        return self.find_element(self.success_message_ux_loc).text

# Preview
    # old ui
    def click_preview_button(self):
        self.find_element(self.preview_button_loc, clickable=True).click()

    def wait_page_load(self, loc):
        self.find_element(loc)

    # ux
    def wait_ux_page_load(self, loc):
        self.find_element(loc)

    def click_next_button_ux(self, next_button_ux_loc):
        self.find_element(next_button_ux_loc, clickable=True).click()

# Submit
    # old ui
    def click_submit_button(self):
        self.find_element(self.submit_button_loc, clickable=True).click()

    # ux
    def click_submit_button_ux(self, submit_button_ux_loc):
        self.find_element(submit_button_ux_loc, clickable=True).click()

# Save as Template
    def click_save_as_template_checkbox(self, value):
        self.find_element(self.save_as_template_checkbox_loc, clickable=True).click()
        self.find_element(self.template_name_loc).send_keys(value)

# Delete
    # old ui
    def click_delete_button_loc(self):
        self.find_element(self.delete_button_loc, clickable=True).click()

# Reject
    # old ui
    def click_reject_button(self):
        self.find_element(self.reject_button_loc, clickable=True).click()

# Approve
    # old ui
    def click_approve_payment_button(self, approve_payment_button_loc):
        self.find_element(approve_payment_button_loc, clickable=True).click()

    def click_approve_button(self, approve_button_loc):
        self.find_element(approve_button_loc, clickable=True).click()

    # ux
    def click_approve_button_ux(self, approve_button_ux_loc):
        self.find_element(approve_button_ux_loc, clickable=True).click()

    def click_challenge_button_ux(self):
        self.find_element(self.challenge_button_ux_loc, clickable=True).click()

    def enter_response_ux(self, response_ux_loc, value):
        self.find_element(response_ux_loc).send_keys(value)

    def get_approve_success_message_ux(self, approve_success_message_ux_loc):
        return self.find_element(approve_success_message_ux_loc).text

# Approve Now
    # old ui
    def click_approve_now_checkbox(self):
        self.find_element(self.approve_now_checkbox_loc, clickable=True).click()

    def enter_approve_response(self, approve_response_loc, value):
        self.find_element(approve_response_loc).send_keys(value)

# Copy
    # old ui
    def click_copy_button(self):
        self.find_element(self.copy_button_loc, clickable=True).click()

# Edit
    # old ui
    def click_edit_button(self):
        self.find_element(self.edit_button_loc, clickable=True).click()

    def click_preview_on_edit_page(self):
        self.find_element(self.preview_button_edit_page_loc, clickable=True).click()

    # ux
    def click_edit_icon_ux(self, edit_icon_ux_loc):
        self.find_element(edit_icon_ux_loc, clickable=True).click()

# Login
    def login_cb(self, url, login_id, company_id):
        login = LoginPage(self.driver)
        login.logincb(url, login_id, company_id)

# Center
    def click_filter_button(self):
        self.find_element(self.filter_button_loc, clickable=True).click()

    def enter_reference(self, reference_loc, value):
        self.find_element(reference_loc).send_keys(value)

    def click_go_button(self, go_button_loc):
        self.find_element(go_button_loc, clickable=True).click()

    def click_reference_link(self, reference):
        reference_loc = (By.LINK_TEXT, reference)
        self.find_element(reference_loc, clickable=True).click()

    def enter_file_name(self, file_name_loc, filename):
        self.find_element(file_name_loc).send_keys(filename)

    def click_file_name_link(self, filename):
        """点击搜索出来的file name的链接"""
        self.find_element((By.LINK_TEXT, filename)).click()

# To View Page
    def get_to_view_payment_page(self, instruction_id):
        payment_page = PaymentPage(self.driver)
        payment_page.open_menu("Payments", "Transfer Center")
        payment_page.click_filter_button()
        payment_page.enter_reference(PaymentPage.reference_loc, instruction_id)
        payment_page.click_go_button(self.go_button_loc)
        payment_page.click_reference_link(instruction_id)

# choose a tab in list page
    def click_tab(self, tab_loc):
        self.find_element(tab_loc).click()
