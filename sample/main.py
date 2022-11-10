# -*- coding: utf-8 -*-
# author：xxp time:2022/11/5
import sample.entity.Entity as Entity
import sample.dao.connect as connection
import sample.gui.login as test
if __name__ == '__main__':
    test.Login()
    # db=connection.ConnectDatabase()
    # # print(type(db.query_customer()[0]))
    # my_database = connection.ConnectDatabase()
    #
    # # 获取数据库中的用户信息，顾客、雇员
    # customers_info = my_database.query_customer()
    # employees_info = my_database.query_employee()
    # print(customers_info)
