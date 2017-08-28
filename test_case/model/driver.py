from selenium import webdriver

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: driver.py
@time: 2017/8/17 11:00
'''


def browser():
	# 定义 webdriver
	driver = webdriver.Firefox(executable_path='./../drivers/geckodriver')
	# driver = webdriver.Remote(
	# 	command_executor='http://127.0.0.1:4444/wd/hub',
	# 	desired_capabilities={"browserName": "chrome"})
	return driver
