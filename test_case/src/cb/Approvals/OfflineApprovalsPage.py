from Util import *
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: MyApprovalsPage.py
@time: 2018/4/11 16:44
'''


class OfflineApprovalsPage(BasePage):
    """Offline Approvals List页面的page object"""
    # Offline Approval List 页面by transaction tab的定位
    list_per_transaction_tab_loc = (By.XPATH, "//a[@tabid='pendingTab']")
    # Offline Approval List页面search section里reference的定位
    reference_loc = (By.XPATH, "//div[@id='tab-2fileOfflineApprovalCentre_Tabs']"
                               "/form/div[2]/div[2]/div/div/div[2]/div/div[8]/input")
    # Offline Approval List页面go button的定位
    offline_approval_go_button_loc = (By.ID, 'submitpending_Link')
    # Approver 下拉框的定位
    approver_dropdown_loc = (By.ID, "offapproverId")
    # Offline Approval List页面title的定位
    title_loc = (By.XPATH, "//span[@slid='pageHeadlineDisplay']")
