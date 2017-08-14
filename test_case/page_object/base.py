# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: try.py
@time: 2017/8/14 15:41
'''


class Page(object):
    cb_url = 'https://192.168.0.245:9444/s1gcb/logon/loginSSO'

    def __init__(self, selenium_driver, base_url=cb_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        self.url = self.base_url + url
        self.driver.get(url)

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, script):
        return self.driver.execute_script(script)
