from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: basePage.py
@time: 2017/8/14 15:41
所有页面类的基础类，重定义了find_element,execute_script等方法
'''


class BasePage(object):
    # 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参

    def __init__(self, selenium_driver, base_url='https://116.12.252.152/s1gcb/logon/loginSSO'):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def _open(self, url):
        self.url = self.base_url + url
        self.driver.get(self.url)

    # 定义open方法，调用_open()进行打开链接
    def open(self, url):
        self._open(url)

    # 重写元素定位方法
    def find_element(self, loc):
        try:
            return WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located(loc))
        except Exception:
            print("page {0} can't find locator {1}".format(self.driver.current_url, loc))

    # 重写一组元素定位方法
    def find_elements(self, *loc):
        try:
            return WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located())
        except Exception as e:
            print("page {0} can't find elements for this locator {1}".format(self.driver.current_url, loc))

    # 重写下拉框定位方法
    def select_dropdown(self, loc):
        try:
            WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located(loc))
            return Select(self.find_element(loc))
        except Exception:
            print("page %s can't find dropdown %s" % (self.driver.current_url, loc))

    # 重写脚本执行方法
    def script(self, script):
        try:
            return self.driver.execute_script(script)
        except Exception:
            print("page {0} execute script {1} fail".format(self.driver.current_url, script))

    # 重写跳转到frame页面的方法
    def switch_frame(self, loc):
        try:
            return self.driver.switch_to_frame(self.find_element(loc))
        except Exception:
            print("page {0} can't switch to this frame page {1}".format(self.driver.current_url, loc))
    
    # 重写跳转到window的方法
    def switch_window(self, loc):
        try:
            return self.driver.switch_to_window(loc)
        except Exception:
            print("page {0} can't switch to window {1}".format(self.driver.current_url, loc))

    # 重写send_keys方法(在输入前能先执行click,clear等操作，可再扩展)
    def send_keys(self, loc, value, click_first = True, clear_first = True):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            return self.find_element(loc).send_keys(value)
        except Exception:
            print("page {0} can't find locator {1}".format(self.driver.current_url, loc))

    # 重写鼠标悬停方法
    def move_mouse_to_element(self, element='', loc=''):
        try:
            if loc:
                element = self.find_element(loc)
            elif element:
                element = element
            else:
                print("mouse actions need target element")
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception:
            print("page {0} can't find locator {1} or element {2}".format(self.driver.current_url, loc, element))
