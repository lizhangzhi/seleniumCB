import logging
from Util import *
from test_case.src.PageFactory import PageFactory
from .CrossBorderACHPage import CrossBorderACHPage
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: CrossBorderACH_sta.py
@time: 2018/3/29 15:16
'''


class CrossBorderACHTest(MyUnittest):

    def create_CBA(self):
        """创建Cross Border ACH"""
        cross_border_ach = PageFactory.get_cross_border_page_instance(self.driver)
        cross_border_ach.login_cb(self.url, self.login_id, self.company_id)
        cross_border_ach.open_menu("Payments", "Cross Border ACH")
        cross_border_ach.switch_to_frame()
        cross_border_ach.select_account_ux(CrossBorderACHPage.account_ux_loc,
                                           CrossBorderACHPage.account_value_ux_loc,
                                           "124124124")
        cross_border_ach.select_country_ux(CrossBorderACHPage.country_ux_loc,
                                           CrossBorderACHPage.country_value_ux_loc,
                                           "HONG KONG")
        cross_border_ach.select_debit_type_ux(CrossBorderACHPage.debit_type_ux_loc,
                                              CrossBorderACHPage.debit_type_value_ux_loc,
                                              "Consolidated Debit")
        cross_border_ach.select_beneficiary_bulk_ux(CrossBorderACHPage.beneficiary_ux_loc)
        cross_border_ach.enter_amount_ux(CrossBorderACHPage.amount_ux_loc, '9')
        cross_border_ach.scroll_up_and_down(0, 1500)
        cross_border_ach.click_next_button_ux(CrossBorderACHPage.next_button_ux_loc)
        cross_border_ach.wait_ux_page_load(CrossBorderACHPage.edit_icon_loc)
        cross_border_ach.scroll_up_and_down(0, 2000)
        cross_border_ach.click_submit_button_ux(CrossBorderACHPage.submit_button_ux_loc)
        self.success_message = cross_border_ach.get_success_message_ux()
        self.instruction_id = cross_border_ach.get_success_message_ux().split()[3]
        cross_border_ach.switch_to_frame(out=True)

    @log(logger=logging.getLogger(__name__))
    def test_1_create_CBA(self):
        """测试能成功创建一条Cross Border ACH"""
        self.create_CBA()
        function.take_screenshot(self.driver, '18_cross_border_ach_create.jpg')
        self.assertIn('has been created successfully', self.success_message)
        PageFactory.clean_page_instance()
