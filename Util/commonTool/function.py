import os

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: function.py
@time: 2017/8/17 14:42
'''


def take_screenshot(driver, file_name):
    # 截图方法
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_path = base_dir + "/report/image/" + file_name
    driver.get_screenshot_as_file(file_path)
