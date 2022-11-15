# -*- coding: utf-8 -*-
# author：xxp time:2022/11/15

import tkinter
from tkinter import ttk
import tkinter.messagebox

from sample.dao.connect import ConnectDatabase
from sample.entity.Entity import Order, ShoppingCart
from sample.gui.listview import ListViewUI


class SelectionInformation:
    restaurant_id = 0
    shopping_cart = []

    def print_info(self):
        print(self.restaurant_id)
        print(self.shopping_cart)


class RestaurantUI:
    def __init__(self, frame):
        self.frame = frame
        self.cols_count = 0
        self.rows_count = 0
        self.head_tags = ['index']
        self.head_widths = [50]
        self.head_texts = ['']
        self.tree = ttk.Treeview(frame, columns=self.head_tags, show='headings')
        self.__created = False  # 控制表格创建后，停用部分方法
        self.__check_boxes = True  # 标识是否有复选框功能
        self.__show_index = True  # 标识是否显示行号
        self.restaurant_id = 0
        self.listview = ListViewUI(self.frame)
        self.restaurants = ConnectDatabase().query_restaurant()

        self.listview.add_column('restaurant_id')
        self.listview.add_column('restaurant_name')
        self.listview.add_column('restaurant_address')
        self.listview.set_rows_height_fontsize()
        self.listview.set_head_font()
        self.listview.create_listview()

        for r in self.restaurants:
            restaurant = [r['restaurant_id'], r['restaurant_name'], r['restaurant_address']]
            self.listview.add_row(False, restaurant)
        btn_modify = tkinter.Button(self.frame, text="Enter the restaurant", command=self.enter_restaurant)
        btn_modify.place(x=300, y=480, width=200, height=50)

    def enter_restaurant(self):
        for row_num in range(1, self.rows_count + 1):
            if self.listview.get_check_bl(row_num):
                self.restaurant_id = row_num
                self.restaurant_id = row_num
        self.listview.destroy_result()
        menu = MenuUI(self.frame)


class MenuUI:
    def __init__(self, frame):
        self.frame = frame
        self.shopping_cart = []
        self.listview = ListViewUI(self.frame)

        self.listview.add_column('dish_id')
        self.listview.add_column('dish_name')
        self.listview.add_column('dish_price')
        self.listview.add_column('dish_description')
        self.listview.set_rows_height_fontsize()
        self.listview.set_head_font()
        self.listview.create_listview()

        self.menu = ConnectDatabase().query_menu()
        for m in self.menu:
            dish = [m['dish_id'], m['dish_name'], m['dish_price'], m['dish_description']]
            self.listview.add_row(False, dish)
        btn_modify = tkinter.Button(self.frame, text="Add to shopping cart", command=self.add_shopping_cart)
        btn_modify.place(x=300, y=480, width=200, height=50)

    def add_shopping_cart(self):
        shop_info = "Shopping Cart:\n"
        for row_num in range(1, self.listview.rows_count + 1):
            if self.listview.get_check_bl(row_num):
                print(self.listview.get_row_values_by_item(self.listview.get_row(row_num)))
                dish = self.listview.get_row_values_by_item(self.listview.get_row(row_num))
                self.shopping_cart.append(dish)
                shop_info += ",".join(dish)
                shop_info += "\n"

        is_add = tkinter.messagebox.askyesno('Are you sure to add?',
                                             shop_info)
        if is_add:
            shopping_cart_temp = []
            shopping_cart_add = []
            for dish in self.shopping_cart:
                if dish not in shopping_cart_temp:
                    shopping_cart_temp.append(dish)
                    s = ShoppingCart(shopping_cart_id=None, dish_id=int(dish[1]), dish_num=0, dish_sum_price=0)
                    shopping_cart_add.append(s)
            for d in self.shopping_cart:
                for a in shopping_cart_add:
                    if a.dish_id == int(d[1]):
                        a.dish_num += 1
                        a.dish_sum_price += float(d[3])
            for dish in shopping_cart_add:
                ConnectDatabase.add_shopping_cart(dish)


class ShoppingCartUI:
    def __init__(self, frame):
        self.frame = frame
        self.shopping_cart = []
        self.listview = ListViewUI(self.frame)

        self.listview.add_column('shopping_cart_id')
        self.listview.add_column('dish_id')
        self.listview.add_column('dish_num')
        self.listview.add_column('dish_sum_price')
        self.listview.set_rows_height_fontsize()
        self.listview.set_head_font()
        self.listview.create_listview()
        self.shopping_carts = ConnectDatabase().query_shopping_cart()
        for s in self.shopping_carts:
            shopping_cart = [s['shopping_cart_id'], s['dish_id'], s['dish_num'], s['dish_sum_price']]
            self.listview.add_row(False, shopping_cart)
        btn_modify = tkinter.Button(self.frame, text="place order", command=self.place_order)
        btn_modify.place(x=100, y=480, width=200, height=50)
        btn_delete = tkinter.Button(self.frame, text="delete shopping cart", command=self.delete_shopping_cart)
        btn_delete.place(x=500, y=480, width=200, height=50)

    def place_order(self):
        self.shopping_cart = []
        order = Order(order_id=8, customer_id=8, restaurant_id=9, employee_id=9, table_id=9, order_time="",
                      total_price=0, note="", pay_state="")
        ConnectDatabase().add_order(order)

    @staticmethod
    def delete_shopping_cart():

        shopping_cart = ConnectDatabase.query_shopping_cart()
        is_delete = tkinter.messagebox.askyesno('Are you sure to delete?',
                                                "The items in the cart will be deleted")
        if is_delete:
            shopping_cart_all_id = []
            for sc in shopping_cart:
                shopping_cart_all_id.append(sc["shopping_cart_id"])
            ConnectDatabase.delete_shopping_cart(shopping_cart_all_id)
