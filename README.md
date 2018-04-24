# seleniumCB

seleniumCB is a UI Automation Project based on Python 3.6.1 + Selenium 3.4.3 + unittest

# 项目结构
1) config 配置文件
2) drivers 各浏览器的driver目录
3) package  selenium server的jar包
4) report 测试报告和log存放路径
5) test_case 测试用例
6) uploadfile 上传文件存放路径
7) Util 工具类
    - commonTool 通用方法目录
        - configUtil 配置文件读取
        - driver webdriver配置
        - function 通用方法存放
        - myunit 继承unittest.TestCase,重写setup和teardown
     - page_object
        - basePage 封装selenium通用方法
        - loginPage 登陆页面的page对象