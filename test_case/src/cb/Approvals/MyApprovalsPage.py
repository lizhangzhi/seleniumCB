from Util import *
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: MyApprovalsPage.py
@time: 2018/4/11 16:44
'''


class MyApprovalsPage(BasePage):
    """My Approvals List页面的page object"""
    # My Approval List-By Transaction页面search section里reference的定位
    reference_loc = (By.XPATH, "//div[@id='tab-2fileApprovalCentre_Tabs']"
                               "/form/div[2]/div[2]/div/div/div[2]/div/div[6]/input")
    # My Approval List 页面by transaction tab的定位
    list_per_transaction_tab_loc = (By.XPATH, "//a[@tabid='pendingTab']")
    # My Approval List 页面by file tab的定位
    list_per_file_tab_loc = (By.XPATH, "//a[@tabid='processedTab']")
    # My Approval List-By File页面search section里file name的定位
    filter_file_name_loc = (By.ID, "filterFileName")
    # My Approval List-By File页面search section里go 按钮的定位
    pert_transaction_go_button_loc = (By.ID, "submitprocessed_Link")
    # My Approval List - By File -View File页面的approve file按钮的定位
    approve_file_button_loc = (By.ID, "approveButton_Link")
    # My Approval List - By File -View File页面的File Information标题栏的定位
    page_load_loc = (By.XPATH, "//span[@id='RejectFileContentsectionLeft']")
