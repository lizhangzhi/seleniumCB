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

# UX
    frame_loc = (By.ID, 'iframe1')
    account_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='payer']")
    account_value_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='payer']/div/div[2]/div[2]/span")
    beneficiary_ux_loc = (By.XPATH, "//div[@class='payee-list']/filter-item-component[1]/section/div/div/div/button")
    amount_ux_loc = (By.XPATH, "//dbs-input[@formcontrolname='payeeAmount']/span/div/input")
    success_message_ux_loc = (By.XPATH, "//div[@class='alert alert-info']/ul/li/label")

# Preview
    # old ui
    preview_button_loc = (By.ID, 'previewButton_Link')
    # ux
    next_button_ux_loc = (By.XPATH, "//button[@translate = 'labelPreviewTransfer']")

# Submit
    # old ui
    submit_button_loc = (By.ID, 'submitButton_Link')
    # ux
    submit_button_ux_loc = (By.XPATH, "//button[@translate = 'labelSubmit']")

# Approve
    # old ui
    approve_payment_button_loc = (By.ID, 'approveButton_Link')
    # ux
    approve_button_ux_loc = (By.XPATH, "//div[@class='form-group no-print']/div/button[5]")
    challenge_button_ux_loc = (By.XPATH, "//*[@class='challenge-button-get']/button")
    response_ux_loc = (By.XPATH, "//dbs-input[@name='responseCode']/span/div/input")
    approve_success_message_ux_loc = (By.XPATH, "//md-dialog-container[@class='mat-dialog-container']")
# Approve Now
    # old ui
    approve_now_checkbox_loc = (By.ID, 'approvalChoice_B')
    approve_now_response_loc = (By.ID, 'signature')

# Edit
    # old ui
    edit_button_loc = (By.ID, "modifyButton_Link")
    # ux
    edit_icon_ux_loc = (By.XPATH, "//label[@translate='labelEdit']")

# Copy
    # old UI
    copy_button_loc = (By.ID, 'copyButton_Link')

# Transfer Center
    filter_button_loc = (By.ID, 'pendingA')
    reference_loc = (By.ID, 'filterReference')
    go_button_loc = (By.ID, 'ButtonCtrl_Link')

# Old UI
    def select_from_account(self, account_text):
        self.select_dropdown(self.from_account_loc).select_by_visible_text(account_text)

    def select_payment_currency(self, currency):
        self.select_dropdown(self.payment_currency_loc).select_by_value(currency)

    def enter_amount(self, value):
        self.find_element(self.amount_loc).send_keys(value)

    def select_beneficiary(self):
        self.select_dropdown(self.beneficiary_loc).select_by_index(2)

    def enter_payment_details(self, value):
        self.find_element(self.payment_details_loc).send_keys(value)

    def get_success_message(self):
        return self.find_element(self.success_message_loc).text

# UX
    def switch_to_frame(self, out=False):
        self.switch_frame(self.frame_loc, out)

    def select_account_ux(self):
        self.find_element(self.account_ux_loc).click()
        self.find_element(self.account_value_ux_loc).click()

    def select_beneficiary_ux(self):
        self.find_element(self.beneficiary_ux_loc).click()

    def enter_amount_ux(self, value):
        self.find_element(self.amount_ux_loc).clear()
        self.find_element(self.amount_ux_loc).send_keys(value)

    def get_success_message_ux(self):
        return self.find_element(self.success_message_ux_loc).text

# Preview
    # old ui
    def click_preview_button(self):
        self.find_element(self.preview_button_loc).click()

    # ux
    def click_next_button_ux(self):
        self.find_element(self.next_button_ux_loc).click()

# Submit
    # old ui
    def click_submit_button(self):
        self.find_element(self.submit_button_loc).click()

    # ux
    def click_submit_button_ux(self):
        self.find_element(self.submit_button_ux_loc).click()

# Approve
    # old ui
    def click_approve_payment_button(self):
        self.find_element(self.approve_payment_button_loc).click()

    # ux
    def click_approve_button_ux(self):
        self.find_element(self.approve_button_ux_loc).click()

    def click_challenge_button_ux(self):
        self.find_element(self.challenge_button_ux_loc).click()

    def enter_response_ux(self, value):
        self.find_element(self.response_ux_loc).send_keys(value)

    def get_approve_success_message_ux(self):
        return self.find_element(self.approve_success_message_ux_loc).text

# Approve Now
    # old ui
    def click_approve_now_checkbox(self):
        self.find_element(self.approve_now_checkbox_loc).click()

    def enter_approve_now_response(self, value):
        self.find_element(self.approve_now_response_loc).send_keys(value)

# Copy
    # old ui
    def click_copy_button(self):
        self.find_element(self.copy_button_loc).click()

# Edit
    # old ui
    def click_edit_button(self):
        self.find_element(self.edit_button_loc).click()

    # ux
    def click_edit_icon_ux(self):
        self.find_element(self.edit_icon_ux_loc).click()

# Login
    def login_cb(self, url, login_id, company_id):
        login = LoginPage(self.driver)
        login.logincb(url, login_id, company_id)

# Center
    def click_filter_button(self):
        self.find_element(self.filter_button_loc).click()

    def enter_reference(self, value):
        self.find_element(self.reference_loc).send_keys(value)

    def click_go_button(self):
        self.find_element(self.go_button_loc).click()

    def click_reference_link(self, reference):
        reference_loc = (By.LINK_TEXT, reference)
        self.find_element(reference_loc).click()

# To View Page
    def get_to_view_payment_page(self, instruction_id):
        payment_page = PaymentPage(self.driver)
        payment_page.open_menu("Payments", "Transfer Center")
        payment_page.click_filter_button()
        payment_page.enter_reference(instruction_id)
        payment_page.click_go_button()
        payment_page.click_reference_link(instruction_id)
