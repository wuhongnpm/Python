# coding=utf-8

# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行



# 2.注释：包括记录创建时间，创建人，项目名称。

'''

Created on 2019-9-29

@author: 北京-宏哥   QQ交流群：707699217

Project:手把手教你搭建Pytest+Allure2.X环境详细教程，生成让你一见钟情的测试报告（非常详细，非常实用）

'''

# 3.导入模块

import allure





# @allure.MASTER_HELPER.feature("测试Dome")

@allure.feature("测试Demo")

class TestDome(object):



    #@@allure.MASTER_HELPER.step("定义被测函数")

    @allure.step("定义被测函数")

    def func(self, x):

        return x+1



    #@allure.MASTER_HELPER.story("被测场景")

    @allure.story("被测场景")

    #@allure.MASTER_HELPER.severity("blocker")

    @allure.severity("blocker")

    #@allure.MASTER_HELPER.step("断言结果")

    @allure.step("断言结果")

    def test_func(self):

        # with allure.MASTER_HELPER.step("断言结果"):

        #allure.MASTER_HELPER.attach("预期结果", "{}".format(self.func(3)))

        allure.attach("预期结果", "{}".format(self.func(3)))

        #allure.MASTER_HELPER.attach("实际结果", "{}".format(5))

        allure.attach("实际结果", "{}".format(5))

        assert self.func(3) == 5