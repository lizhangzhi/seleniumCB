from time import sleep
from Util import *
from .AlertsPage import AlertsPage
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: Alerts_sta.py
@time: 2018/4/10 9:35
'''


class AlertsTest(MyUnittest):

    def test_1_alerts_page_working(self):
        """判断Alerts/Reminders页面能正常显示"""
        login_page = LoginPage(self.driver)
        login_page.logincb(self.url, self.login_id, self.company_id)
        alerts_page = AlertsPage(self.driver)
        alerts_page.open_menu("Preferences", "Alerts/Reminders")
        sleep(3)
        self.page_head = alerts_page.get_page_head_line()
        function.take_screenshot(self.driver, "28_alerts.jpg")
        self.assertIn("Preferences - Alerts and Reminders", self.page_head)
