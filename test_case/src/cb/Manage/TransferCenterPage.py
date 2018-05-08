from Util import *


# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: TransferCenterPage.py
@time: 2018/5/4 18:58
'''


class TransferCenterPage(BasePage):
    """Transfer Center页面的page object"""
    # filter模块Reference/Group Name输入框的定位
    reference_loc = (By.ID, 'filterReference')
    # filter模块go按钮的定位
    go_button_loc = (By.ID, 'ButtonCtrl_Link')
