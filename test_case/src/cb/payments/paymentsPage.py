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
    fromaccount_loc = (By.ID, 'fromParty')
    paymentcurrency_loc = (By.ID, 'paymentCurrency_currencyCode')
    amount_loc = (By.ID, 'amount_value_control')
    beneficiary_loc = (By.ID, 'toParty')
    preview_button_loc = (By.ID, 'previewButton_Link')
    instruction_to_DBS_Bank_loc = (By.ID, 'messageToBank')
    submit_button_loc = (By.ID, 'submitButton_Link')
    success_message_loc = (By.ID, 'my_list')

    # Transfer Center
    filter_button_loc = (By.ID, 'pendingA')
    reference_loc = (By.ID, 'filterReference')
    go_button_loc = (By.ID, 'ButtonCtrl_Link')

    # UX
    frame_loc = (By.ID, 'iframe1')
    country_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname= 'countrySelected']")
    country_value_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname= 'countrySelected']/div/div[2]/div[1]/span")
    account_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='payer']")
    account_value_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='payer']/div/div[2]/div[2]/span")
    type_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='ptnbnkPmtSelect']")
    type_value_ux_loc = (By.XPATH, "//auto-complete[@formcontrolname='ptnbnkPmtSelect']/div/div[2]/div[4]/span")
    beneficiary_ux_loc = (By.XPATH, "//div[@class='payee-list']/filter-item-component[1]/section/div/div/div/button")
    amount_ux_loc = (By.XPATH, "//dbs-input[@formcontrolname='payeeAmount']/span/div/input")
    next_button_ux_loc = (By.XPATH, "//button[@translate = 'labelPreviewTransfer']")
    submit_button_ux_loc = (By.XPATH, "//button[@translate = 'labelSubmit']")
    success_message_ux_loc = (By.XPATH, "//div[@class='alert alert-info']/ul/li/label")
    edit_icon_ux_loc = (By.XPATH, "//label[@translate='labelEdit']")

    # Approve UX
    approve_button_ux_loc = (By.XPATH, "//div[@class='form-group no-print']/div/button[5]")
    challenge_button_ux_loc = (By.XPATH, "//*[@class='challenge-button-get']/button")
    response_ux_loc = (By.XPATH, "//dbs-input[@name='responseCode']/span/div/input")
    approve_success_message_ux_loc = (By.XPATH, "//md-dialog-container[@class='mat-dialog-container']")

    # Old UI
    def select_from_account(self, account_text):
        self.select_dropdown(self.fromaccount_loc).select_by_visible_text(account_text)

    def select_payment_currency(self, currency):
        self.select_dropdown(self.paymentcurrency_loc).select_by_value(currency)

    def enter_amount(self, value):
        self.find_element(self.amount_loc).send_keys(value)

    def select_beneficiary(self):
        self.select_dropdown(self.beneficiary_loc).select_by_index(2)

    def enter_instruction(self, value):
        self.find_element(self.instruction_to_DBS_Bank_loc).send_keys(value)

    def click_preview_button(self):
        self.find_element(self.preview_button_loc).click()

    def click_submit_button(self):
        self.find_element(self.submit_button_loc).click()

    def get_success_message(self):
        return self.find_element(self.success_message_loc).text

    # UX
    def switch_to_frame(self, out=False):
        self.switch_frame(self.frame_loc, out)

    def select_country_ux(self):
        self.find_element(self.country_ux_loc).click()
        # sleep(1)
        self.find_element(self.country_value_ux_loc).click()

    def select_account_ux(self):
        self.find_element(self.account_ux_loc).click()
        # sleep(1)
        self.find_element(self.account_value_ux_loc).click()

    def select_type_ux(self):
        self.find_element(self.type_ux_loc).click()
        self.find_element(self.type_value_ux_loc).click()

    def select_beneficiary_ux(self):
        self.find_element(self.beneficiary_ux_loc).click()

    def enter_amount_ux(self, value):
        self.find_element(self.amount_ux_loc).clear()
        self.find_element(self.amount_ux_loc).send_keys(value)

    def click_next_button_ux(self):
        self.find_element(self.next_button_ux_loc).click()

    def click_submit_button_ux(self):
        self.find_element(self.submit_button_ux_loc).click()

    def get_success_message_ux(self):
        return self.find_element(self.success_message_ux_loc).text

    # transfer center
    def click_filter_button(self):
        self.find_element(self.filter_button_loc).click()

    def enter_reference(self, value):
        self.find_element(self.reference_loc).send_keys(value)

    def click_go_button(self):
        self.find_element(self.go_button_loc).click()

    def click_reference_link(self, reference):
        reference_loc = (By.LINK_TEXT, reference)
        self.find_element(reference_loc).click()

    # approve
    def click_approve_button_ux(self):
        self.find_element(self.approve_button_ux_loc).click()

    def click_challenge_button_ux(self):
        self.find_element(self.challenge_button_ux_loc).click()

    def enter_response_ux(self, value):
        self.find_element(self.response_ux_loc).send_keys(value)

    def get_approve_success_message_ux(self):
        return self.find_element(self.approve_success_message_ux_loc).text

    # edit
    def click_edit_icon_ux(self):
        self.find_element(self.edit_icon_ux_loc).click()

    payee_ux_loc = (By.XPATH, "//div[@class='payee-list']/div[3]/p")

    def get_payee_confidential_ux(self):
        return self.find_element(self.payee_ux_loc).text

    item_ux_loc = (By.XPATH, "//div[@class='payee-list']/filter-item-component/section")

    def get_payee_list_ux(self):
        return self.find_element(self.item_ux_loc)
