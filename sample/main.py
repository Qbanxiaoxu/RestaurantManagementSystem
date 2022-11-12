# -*- coding: utf-8 -*-
# author：xxp time:2022/11/5
from sample.dao.connect import ConnectDatabase
from sample.gui.customer import CustomerUI
from sample.gui.login import LoginUI

if __name__ == '__main__':
    # LoginUI()
    CustomerUI("11", "11")
    # print(ConnectDatabase().query_restaurant())
    # db=connection.ConnectDatabase()
    # # print(type(db.query_customer()[0]))
    # my_database = connection.ConnectDatabase()
    #
    # # 获取数据库中的用户信息，顾客、雇员
    # customers_info = my_database.query_customer()
    # employees_info = my_database.query_employee()
    # print(customers_info)
