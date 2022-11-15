# -*- coding: utf-8 -*-
# author：xxp time:2022/11/5
from sample.dao.connect import ConnectDatabase
from sample.entity.Entity import ShoppingCart
from sample.gui.customer import CustomerUI
from sample.gui.login import LoginUI

if __name__ == '__main__':
    # LoginUI()
    CustomerUI("11", "11")
    # shopping_cart_add = []
    # shopping_cart = [('☑1', '1', 'Rachel Phillips', '665.81', '5x4Chr59yw'),
    #                  ('☑2', '2', 'Qin Shihan', '848.69', 'MjzToZsanr'),
    #                  ('☑3', '3', 'Tong Cho Yee', '349.78', '2pgvaixRGA'),
    #                  ('☑4', '4', 'Lee Tin Lok', '184.78', 'HJ7VwzZEG7'),
    #                  ('☑5', '5', 'Tong Chi Ming', '629.17', 'thecmS6Wvu'),
    #                  ('☑6', '6', 'Gao Lu', '598.80', 'NwyxyaIVGo'),
    #                  ('☑7', '7', 'Vincent Perez', '334.62', 'fVdDsKpqky'),
    #                  ('☑7', '7', 'Vincent Perez', '334.62', 'fVdDsKpqky'),
    #                  ('☑7', '7', 'Vincent Perez', '334.62', 'fVdDsKpqky'),
    #                  ('☑7', '7', 'Vincent Perez', '334.62', 'fVdDsKpqky'),
    #                  ('☑8', '8', 'Shawn Reynolds', '680.77', 'SGwCIEKtt9'),
    #                  ('☑8', '8', 'Shawn Reynolds', '680.77', 'SGwCIEKtt9'),]
    #
    # shopping_cart_temp = []
    # sh = []
    # for dish in shopping_cart:
    #     if dish not in shopping_cart_temp:
    #         shopping_cart_temp.append(dish)
    #         s = ShoppingCart(shopping_cart_id=None, dish_id=int(dish[1]), dish_num=0, dish_sum_price=0)
    #         sh.append(s)
            # dict_temp = {"dish_id": int(dish[1]), "dish_num": 0, "dish_sum_price": 0}


    # print(len(sh))
    # # for a in shopping_cart_add:
    # #     for d in shopping_cart:
    # #         if a["dish_id"] == d[1]:
    # #             a["dish_num"] += 1
    # #             a["dish_sum_price"] += d[3]
    #
    # for d in shopping_cart:
    #     for a in sh:
    #         if a.dish_id == int(d[1]):
    #             a.dish_num += 1
    #             a.dish_sum_price += float(d[3])
    # print(sh)
    # print(len(sh))
    # print(ConnectDatabase.query_menu())
    # print(shopping_cart_add)
    # s=' '.join(t)
    # print(s)
    # print(ConnectDatabase().query_restaurant())
    # db=connection.ConnectDatabase()
    # # print(type(db.query_customer()[0]))
    # my_database = connection.ConnectDatabase()
    #
    # # 获取数据库中的用户信息，顾客、雇员
    # customers_info = my_database.query_customer()
    # employees_info = my_database.query_employee()
    # print(customers_info)
