import os
from functools import wraps
# from test_case.src.PageFactory import PageFactory


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


def search_file(path, word):
    """在指定路径下递归查找文件名包含关键字的文件"""
    for filename in os.listdir(path):  # 列出目录下的所以文件及目录
        fp = os.path.join(path, filename)  # 通过os.path.join()函数，把两个路径合成一个
        if os.path.isfile(fp) and word in filename:  # 判断是否是文件且文件名包含关键字
            return fp, filename
        elif os.path.isdir(fp):  # 如果是目录，则递归继续往下查找
            search_file(fp, word)


def change_name(path, separator, word, suffix):
    """
    修改文件名
    separator:通过传入的分隔符分割文件
    word:要加到文件名中的字符
    suffix:将文件转换为其它格式的后缀
    """
    if os.path.isfile(path):
        file_path = os.path.split(path)  # 分割目录和文件名
        file_name_list = file_path[1].split(separator)  # 通过-分割文件
        file_name_new = os.path.join(file_path[0], "".join([file_name_list[0], separator, word, suffix]))
        os.rename(path, file_name_new)
    else:
        print("传入的path非文件")


def log(logger):
    """打印log的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info("Start running %s" % func.__name__)
            try:
                func(*args, **kwargs)
            except Exception:
                raise logger.exception("Run %s fail.Please check log and fix" % func.__name__)
            finally:
                logger.info("End running %s" % func.__name__)
                # PageFactory.clean_page_instance()
        return wrapper
    return decorator
