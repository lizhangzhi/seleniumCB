import unittest
import time
import smtplib
import os
import yaml
import logging.config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from HTMLTestRunner import HTMLTestRunner

# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: run_test.py
@time: 2017/8/22 11:35
'''


def new_report():
    # 找到最新的测试报告文件
    result_dir = '../report/'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
    file = os.path.join(result_dir, lists[-1])
    return file


def send_mail(file):
    # 定义发送文件，并把测试报告文件作为附件发送
    sender = 'autobuildemail@163.com'
    password = 'lx7262696'  # zaq1234
    receiver = 'zhangzhi.li@pactera.com'
    smtp_sever = 'smtp.163.com'
    subject = 'IDEAL3 Automation Test Report'

    f = open(file, 'rb')
    mail_body = f.read()
    f.close()
    # 创建一个MIMEMultipart对象，用来组合邮件多个部分
    msg = MIMEMultipart()
    # 构造邮件正文
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    # 构造邮件附件
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="Result.html"'
    msg.attach(att)
    # 发送邮件
    server = smtplib.SMTP(smtp_sever, 25)
    # server.set_debuglevel(1)
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()


def setup_logging(default_path="../config/logging.yml", default_level=logging.INFO, env_key="LOG_CFG"):
    """配置logging功能"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

if __name__ == '__main__':

    setup_logging()
    # 生成HTML报告
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = '../report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='IDEAL3 automated test report', description='Windows10    Firefox')
    # runner = unittest.TextTestRunner()
    # 用discover通过标准加载测试用例
    discover = unittest.defaultTestLoader.discover('../test_case/', pattern='*_sta.py', top_level_dir=None)
    runner.run(discover)
    fp.close()
    # new_file = new_report()
    # send_mail(new_file)
