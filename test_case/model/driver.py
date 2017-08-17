from selenium import webdriver

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: driver.py
@time: 2017/8/17 11:00
'''


def browser():
	driver = webdriver.Firefox(executable_path='./../drivers/geckodriver')
	return driver

if __name__ == '__main__':
	dr = browser()
	dr.get("http://www.baidu.com/")
	dr.quit()
