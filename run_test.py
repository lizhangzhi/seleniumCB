import unittest
import time
from HTMLTestRunner import HTMLTestRunner

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: run_test.py
@time: 2017/8/22 11:35
'''

if __name__ == '__main__':

	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = '../report/' + now + 'result.html'
	fp = open(filename, 'wb')

	runner = HTMLTestRunner(stream=fp, title='IDEAL3 automated test report', description='case result')
	discover = unittest.defaultTestLoader.discover('../test_case/', pattern='*_sta.py', top_level_dir=None)
	runner.run(discover)
