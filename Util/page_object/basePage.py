from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: basePage.py
@time: 2017/8/14 15:41
所有页面类的基础类，重定义了find_element,execute_script等方法
'''


class BasePage(object):
    # 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参

    def __init__(self, selenium_driver):
        self.driver = selenium_driver
        self.timeout = 60
        self.poll_frequency = 1

    def _open(self, url):
        self.driver.get(url)

    # 定义open方法，调用_open()进行打开链接
    def open(self, url):
        self._open(url)

    # 重写元素定位方法
    def find_element(self, loc, clickable=False, presence=False):
        try:
            if clickable:
                element = WebDriverWait(self.driver, self.timeout, self.poll_frequency) \
                    .until(EC.element_to_be_clickable(loc))
            elif presence:
                element = WebDriverWait(self.driver, self.timeout, self.poll_frequency) \
                    .until(EC.presence_of_element_located(loc))
            else:
                element = WebDriverWait(self.driver, self.timeout, self.poll_frequency) \
                    .until(EC.visibility_of_element_located(loc))
            if element:
                return element
            else:
                elements = WebDriverWait(self.driver, self.timeout, self.poll_frequency) \
                    .until(EC.visibility_of_all_elements_located(loc))
                return elements[0] if elements else False
        except Exception:
            print("page {0} can't find locator {1}".format(self.driver.current_url, loc))

    # 重写一组元素定位方法
    def find_elements(self, loc):
        try:
            elements = WebDriverWait(self.driver, self.timeout, self.poll_frequency) \
                .until(EC.visibility_of_all_elements_located(loc))
            return elements
        except Exception as e:
            print("page {0} can't find elements for this locator {1}".format(self.driver.current_url, loc))

    # 重写下拉框定位方法
    def select_dropdown(self, loc):
        try:
            WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(EC.visibility_of_element_located(loc))
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
    def switch_frame(self, loc, out):
        if out is True:
            self.driver.switch_to_default_content()
        else:
            try:
                return WebDriverWait(self.driver, 120, self.poll_frequency) \
                    .until(EC.frame_to_be_available_and_switch_to_it(loc))
                # return self.driver.switch_to_frame(self.find_element(loc))
            except Exception:
                print("page {0} can't switch to this frame page {1}".format(self.driver.current_url, loc))

    # 重写跳转到window的方法
    def switch_window(self, loc):
        try:
            return self.driver.switch_to_window(loc)
        except Exception:
            print("page {0} can't switch to window {1}".format(self.driver.current_url, loc))

    # 重写send_keys方法(在输入前能先执行click,clear等操作，可再扩展)
    def send_keys(self, loc, value, click_first=True, clear_first=True):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            return self.find_element(loc).send_keys(value)
        except Exception:
            print("page {0} can't find locator {1}".format(self.driver.current_url, loc))

    # 重写鼠标悬停方法
    def move_mouse_to_element(self, loc=()):
        try:
            if loc:
                element = self.find_element(loc)
            else:
                print("mouse actions need target element")
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception:
            print("page {0} can't find locator {1} or element {2}".format(self.driver.current_url, loc, element))

    # 重写鼠标双击方法
    def double_click(self, loc=''):
        try:
            if loc:
                element = self.find_element(loc)
            else:
                print("mouse actions need target element")
            ActionChains(self.driver).double_click(element).perform()
        except Exception:
            print("page {0} can't find locator {1} or element {2}".format(self.driver.current_url, loc, element))

    # 通过输入像素来控制页面左右移和上下移
    def scroll_up_and_down(self, up_distance, down_distance):
        self.script("window.scrollBy(%u, %u)" % (up_distance, down_distance))

    # 封装打开菜单的方法
    def open_menu(self, level1_menu, level2_menu):
        # File Service菜单下的Upload File部分使用else里的方法无法实现，解决不了，改成通过js打开菜单，直接通过id定位点击
        file_service_menu_dic = {"Manage Files": "level3nav_a_3_0_0",
                                 "Upload File": "level3nav_a_3_0_1",
                                 "Download File": "level3nav_a_3_0_2",
                                 "Manage Download Files": "level3nav_a_3_0_3",
                                 "Reports": "level3nav_a_3_0_4",
                                 }

        if level1_menu == "File Services":
            level2_loc = (By.ID, file_service_menu_dic[level2_menu])
            self.script("document.getElementById('filesrvc').parentElement.children[1]." +
                        "style='opacity:1; margin-left: 0; width:320px;'")
            self.find_element(level2_loc).click()
        elif level1_menu == "Payments":
            level2_loc = (By.LINK_TEXT, level2_menu)
            self.script("document.getElementById('pmt').parentElement.children[1]." +
                        "style='opacity:1; margin-left: 0; width:320px;'")
            self.find_element(level2_loc).click()
        else:
            level1_loc = (By.LINK_TEXT, level1_menu)
            level2_loc = (By.LINK_TEXT, level2_menu)
            while True:
                try:
                    self.move_mouse_to_element(level1_loc)
                    self.find_element(level1_loc, clickable=True).click()
                    self.find_element(level2_loc).click()
                    break
                except Exception:
                    pass
