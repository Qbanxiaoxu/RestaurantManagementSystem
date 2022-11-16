# -*- coding: utf-8 -*-
# author：xxp time:2022/11/15

import tkinter
from tkinter import ttk
import tkinter.messagebox

from sample.dao.connect import ConnectDatabase
from sample.entity.Entity import Order, ShoppingCart
from sample.gui.listview import ListViewUI
import datetime


class RestaurantUI:

    def __init__(self, frame):
        self.frame = frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.cols_count = 0
        self.rows_count = 0
        self.head_tags = ['index']
        self.head_widths = [50]
        self.head_texts = ['']
        self.tree = ttk.Treeview(frame, columns=self.head_tags, show='headings')
        self.__created = False  # 控制表格创建后，停用部分方法
        self.__check_boxes = True  # 标识是否有复选框功能
        self.__show_index = True  # 标识是否显示行号
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
        restaurant_id = 0
        for row_num in range(1, self.listview.rows_count + 1):
            if self.listview.get_check_bl(row_num):
                restaurant_id = row_num
                # print(row_num)
        self.listview.destroy_result()
        menu = MenuUI(self.frame, restaurant_id)


class MenuUI:
    def __init__(self, frame, restaurant_id):
        self.restaurant_id = restaurant_id
        self.frame = frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.shopping_cart = []
        self.listview = ListViewUI(self.frame)

        self.listview.add_column('restaurant_id')
        self.listview.add_column('dish_id')
        self.listview.add_column('dish_name')
        self.listview.add_column('dish_price')
        self.listview.add_column('dish_description')
        self.listview.set_rows_height_fontsize()
        self.listview.set_head_font()
        self.listview.create_listview()

        self.menu = ConnectDatabase().query_menu()
        for m in self.menu:
            dish = [self.restaurant_id, m['dish_id'], m['dish_name'], m['dish_price'], m['dish_description']]
            self.listview.add_row(False, dish)
        btn_modify = tkinter.Button(self.frame, text="Add to shopping cart", command=self.add_shopping_cart)
        btn_modify.place(x=300, y=480, width=200, height=50)

    def add_shopping_cart(self):
        shop_info = "Shopping Cart:\n"
        for row_num in range(1, self.listview.rows_count + 1):
            if self.listview.get_check_bl(row_num):
                dish = self.listview.get_row_values_by_item(self.listview.get_row(row_num))
                self.shopping_cart.append(dish)
                shop_info += ",".join(dish)
                shop_info += "\n"

        is_add = tkinter.messagebox.askyesno('Are you sure to add?',
                                             shop_info)
        if is_add:
            # shopping_cart_temp = []
            shopping_cart_add = []
            for dish in self.shopping_cart:
                # if dish not in shopping_cart_temp:
                #     shopping_cart_temp.append(dish)
                s = ShoppingCart(dish_id=int(dish[2]),
                                 dish_num=1, dish_sum_price=float(dish[4]), restaurant_id=self.restaurant_id)
                shopping_cart_add.append(s)
            # for d in self.shopping_cart:
            #     for a in shopping_cart_add:
            #         if a.dish_id == int(d[1]):
            #             a.dish_num += 1
            #             a.dish_sum_price += float(d[3])
            for dish_add in shopping_cart_add:
                # print(dish_add)
                ConnectDatabase.add_shopping_cart(dish_add)


class ShoppingCartUI:
    def __init__(self, frame, customer_id):
        self.frame = frame
        self.customer_id = customer_id
        self.note_input = "nothing"

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.listview = ListViewUI(self.frame)

        self.listview.add_column('restaurant_id')
        self.listview.add_column('dish_id')
        self.listview.add_column('dish_num')
        self.listview.add_column('dish_sum_price')
        self.listview.set_rows_height_fontsize()
        self.listview.set_head_font()
        self.listview.create_listview()
        self.shopping_carts = ConnectDatabase().query_shopping_cart()
        for s in self.shopping_carts:
            shopping_cart = [s['restaurant_id'], s['dish_id'], s['dish_num'], s['dish_sum_price']]
            self.listview.add_row(False, shopping_cart)
        btn_modify = tkinter.Button(self.frame, text="place order", command=self.place_order)
        btn_modify.place(x=100, y=480, width=200, height=50)

        btn_delete = tkinter.Button(self.frame, text="delete shopping cart", command=self.delete_shopping_cart)
        btn_delete.place(x=500, y=480, width=200, height=50)

    def place_order(self):
        restaurant_id_all = []
        for dish in self.shopping_carts:
            if dish['restaurant_id'] not in restaurant_id_all:
                restaurant_id_all.append(dish['restaurant_id'])

        for r_id in restaurant_id_all:
            customer_id = self.customer_id
            employee_id = 0
            restaurant_id = r_id
            table_id = 0
            order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            total_price = 0

            note = self.note_input
            pay_state = 'no'
            tables = ConnectDatabase.query_table()
            for t in tables:
                if t['table_state'] == 'idle':
                    table_id = t['table_id']
                    break
            employee = ConnectDatabase.query_employee()
            for e in employee:
                if e['work_state'] == "idle":
                    employee_id = e['employee_id']
                    break
            for d in self.shopping_carts:
                if d['restaurant_id'] == r_id:
                    total_price += d['dish_sum_price']
            if table_id == 0 or employee_id == 0:
                tkinter.messagebox.showerror(title='empty order',
                                             message="No orders need to be added!")
            else:
                order = Order(None, customer_id=customer_id, restaurant_id=restaurant_id, employee_id=employee_id,
                              table_id=table_id, order_time=order_time, total_price=total_price, note=note,
                              pay_state=pay_state)
                ConnectDatabase.add_order(order)
        tkinter.messagebox.showinfo("place order", "Order successful but not paid!")
        ConnectDatabase().delete_shopping_cart()

    @staticmethod
    def delete_shopping_cart():

        is_delete = tkinter.messagebox.askyesno('Are you sure to delete?',
                                                "The items in the cart will be deleted")
        if is_delete:
            ConnectDatabase.delete_shopping_cart()


class OrderUI:
    def __init__(self, frame, user_id):
        self.user_id = user_id
        self.frame = frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.selected_orders = []
        self.order_selected_info = []

        self.listview = ListViewUI(self.frame)

        self.listview.add_column('order_id')
        self.listview.add_column('customer_id')
        self.listview.add_column('restaurant_id')
        self.listview.add_column('employee_id')
        self.listview.add_column('table_id')
        self.listview.add_column('order_time')
        self.listview.add_column('total_price')
        self.listview.add_column('note')
        self.listview.add_column('pay_state')
        self.listview.set_rows_height_fontsize()
        self.listview.set_head_font()
        self.listview.create_listview()

        self.orders = ConnectDatabase().query_orders()
        for o in self.orders:
            if o['customer_id'] == self.user_id:
                order = [o['order_id'], o['customer_id'], o['restaurant_id'],
                         o['employee_id'], o['table_id'], o['order_time'],
                         o['total_price'], o['note'], o['pay_state']]
                self.listview.add_row(False, order)
        btn_modify = tkinter.Button(self.frame, text="wechat pay", command=self.pay_by_wechat)
        btn_modify.place(x=100, y=480, width=200, height=50)

        btn_delete = tkinter.Button(self.frame, text="delete the selected order", command=self.delete_selected_order)
        btn_delete.place(x=500, y=480, width=200, height=50)

    def pay_by_wechat(self):
        selected_orders, order_selected_info = self.get_selected_orders()
        is_pay = tkinter.messagebox.askyesno('Fixed payment?',
                                             order_selected_info)
        if is_pay:
            for order in selected_orders:
                if order[9] == 'no':
                    order_pay = Order(order_id=int(order[1]), customer_id=int(order[2]), restaurant_id=int(order[3]),
                                      employee_id=int(order[4]), table_id=int(order[5]), order_time=order[6],
                                      total_price=float(order[7]), note=order[8], pay_state='yes')
                    ConnectDatabase.modify_order(order_pay)
        tkinter.messagebox.showinfo('welcome next time', 'Successful payment!')

    def get_selected_orders(self):
        selected_orders = []
        order_selected_info = "Selected orders:\n"
        for row_num in range(1, self.listview.rows_count + 1):
            if self.listview.get_check_bl(row_num):
                # print(self.listview.get_row_values_by_item(self.listview.get_row(row_num)))
                order = self.listview.get_row_values_by_item(self.listview.get_row(row_num))
                selected_orders.append(order)
                order_selected_info += ",".join(order)
                order_selected_info += "\n"

        return selected_orders, order_selected_info

    def delete_selected_order(self):
        selected_orders, order_selected_info = self.get_selected_orders()
        is_delete = tkinter.messagebox.askyesno('Are you sure to add?',
                                                order_selected_info)
        if is_delete:
            for order in selected_orders:
                ConnectDatabase.delete_order(int(order[1]))
        tkinter.messagebox.showinfo('the result of the deletion operation', 'Deleting the selected order succeeded!')
