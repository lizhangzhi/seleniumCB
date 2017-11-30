import os
import inspect
# import sys
import yaml
# -*- coding: utf-8 -*-
__author__ = 'lizhangzhi'
'''
@file: configUtil.py
@time: 2017/11/29 17:16
定义了获取配置文件里信息的方法
'''


def get_path(module_now=None):
    """获取当前模块所在路径"""
    if not module_now:
        module_now = get_path  # 这个时候的module就是GetPath函数的命名空间 也就是当前脚本的命名空间吗
    cur_module = inspect.getmodule(module_now)  # inspect.getmodule()方法用来获得定义对象所在的模块
    path = os.path.dirname(cur_module.__file__)  # 获取文件所在路径
    return path


# ROOT = os.path.abspath(os.path.join(get_path(sys.modules['yaml']), os.pardir))  # os.pardir 获取当前目录的父目录名
ROOT = ''


class ConfigUtil(object):
    @classmethod  # @classmethod是类方法，可以通过类直接调用
    def get_all(cls, path='../config/cb.yml'):
        """获取配置文件中的配置，返回string"""
        file_path = ROOT + path
        return yaml.load(open(file_path, 'r'))

    @classmethod
    def get(cls, section, option='', path='../config/cb.yml'):
        """获取配置文件中的配置，返回string"""
        file_path = ROOT + path
        config = yaml.load(open(file_path, 'r'))
        if option:
            result = config[section][option]
        else:
            result = config[section]

        return str(result) if isinstance(result, (str, int)) else result

    @classmethod
    def getint(cls, section, option='', path='../config/cb.yml'):
        """获取配置文件中的配置，返回int"""
        file_path = ROOT + path
        config = yaml.load(open(file_path, 'r'))
        if option:
            return int(config[section][option])
        else:
            return int(config[section])
