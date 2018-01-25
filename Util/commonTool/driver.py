from selenium import webdriver

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: driver.py
@time: 2017/8/17 11:00
'''


def browser():
    # 定义 webdriver

    # 给webdriver起的firefox加载现有的配置
    # profile = webdriver.FirefoxProfile(r"C:\Users\Lee\AppData\Roaming\Mozilla\Firefox\Profiles\7ixwjg9s.default")
    # driver = webdriver.Firefox(profile)

    driver = webdriver.Firefox(executable_path='./../drivers/geckodriver')
    # nodes = {
    #     'http://127.0.0.1:5555/wd/hub': 'firefox',
    #     # 'http://127.0.0.1:5556/wd/hub': 'chrome'
    # }
    # for host, browsers in nodes.items():
    #     print(host, browsers)
    #     driver = webdriver.Remote(
    #         command_executor=host,
    #         desired_capabilities={
    #             # "platform": 'ANY',
    #             "browserName": browsers,
    #             # 'version': '',
    #             # 'javascriptEnabled': True
    #         })
    return driver
