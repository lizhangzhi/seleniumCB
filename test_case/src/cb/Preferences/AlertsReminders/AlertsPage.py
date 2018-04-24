from Util import *
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: AlertsPage.py
@time: 2018/4/10 9:35
'''


class AlertsPage(BasePage):
    """Alerts 的page object"""
    # 页面标题的定位
    page_head_line_loc = (By.XPATH, "//td[@class='sectionBoxTitle']/span[1]")

    def get_page_head_line(self):
        return self.find_element(self.page_head_line_loc).text
