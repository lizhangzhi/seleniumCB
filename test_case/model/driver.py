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
	return driver
