import unittest
from .driver import browser
from .configUtil import ConfigUtil

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: myunit.py
@time: 2017/8/17 10:15
'''


class MyUnittest(unittest.TestCase):
    # 定义自己的unittest类
    @classmethod
    def setUp(cls):
        site = ConfigUtil.get(section='site')
        cls.driver = browser()
        cls.url = site['url']
        cls.login_id = site['login_id']
        cls.company_id = site['company_id']

    def tearDown(self):
        self.driver.quit()
