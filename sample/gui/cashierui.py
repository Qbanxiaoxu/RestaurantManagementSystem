# -*- coding: utf-8 -*-
# author：xxp time:2022/11/17

import tkinter
from tkinter import messagebox
from sample.dao.connect import ConnectDatabase
from sample.entity.Entity import Restaurant, Menu, Employee, Customer, Order
from sample.gui.listview import ListViewUI


class CashierOperation:
    def __init__(self, frame, form_type):
        self.frame = frame
        self.form_type = form_type
        self.destroy_frame()
        self.check_id = None
        self.listview = ListViewUI(self.frame)
        if form_type == 'restaurant_table':
            self.listview.add_column('table_id')
            self.listview.add_column('table_state')
            self.listview.set_rows_height_fontsize()
            self.listview.set_head_font()
            self.listview.create_listview()
            self.tables = ConnectDatabase('admin').query_table()
            for t in self.tables:
                restaurant = [t['table_id'], t['table_state']]
                self.listview.add_row(False, restaurant)

        if form_type == 'menu':
            self.dish_name = None
            self.dish_price = None
            self.dish_description = None
            self.listview.add_column('dish_id')
            self.listview.add_column('dish_name')
            self.listview.add_column('dish_price')
            self.listview.add_column('dish_description')
            self.listview.set_rows_height_fontsize()
            self.listview.set_head_font()
            self.listview.create_listview()

            self.menu = ConnectDatabase('admin').query_menu()
            for m in self.menu:
                dish = [m['dish_id'], m['dish_name'], m['dish_price'], m['dish_description']]
                self.listview.add_row(False, dish)
        if form_type == 'customer':
            self.customer_name = None
            self.customer_password = None
            self.customer_contact_info = None

            self.listview.add_column('customer_id')
            self.listview.add_column('customer_name')
            self.listview.add_column('customer_password')
            self.listview.add_column('contact_info')
            self.listview.set_rows_height_fontsize()
            self.listview.set_head_font()
            self.listview.create_listview()

            self.customers = ConnectDatabase('admin').query_customer()
            for c in self.customers:
                customer = [c['customer_id'], c['customer_name'], c['customer_password'], c['contact_info']]
                self.listview.add_row(False, customer)
        if form_type == 'order':
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

            self.orders = ConnectDatabase('admin').query_orders()
            for o in self.orders:
                order = [o['order_id'], o['customer_id'], o['restaurant_id'],
                         o['employee_id'], o['table_id'], o['order_time'],
                         o['total_price'], o['note'], o['pay_state']]
                self.listview.add_row(False, order)

        btn_modify = tkinter.Button(self.frame, text="check", command=self.check)
        btn_modify.place(x=400, y=480, width=100, height=50)

    def check(self):
        self.destroy_frame()
        self.check_id = tkinter.IntVar()
        tkinter.Label(self.frame, text='check id:').place(x=220, y=160)
        tkinter.Entry(self.frame, textvariable=self.check_id).place(x=400, y=160)

        btn_modify = tkinter.Button(self.frame, text="check", command=self.commit_check)
        btn_modify.place(x=300, y=480, width=200, height=50)

    def commit_check(self):
        check_id = self.check_id.get()
        restaurant = ConnectDatabase('admin').check(check_id=check_id, form_type=self.form_type)
        tkinter.messagebox.showinfo('check', str(restaurant))

    def destroy_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def get_selected(self):
        selected = []
        selected_info = "Selected:\n"
        for row_num in range(1, self.listview.rows_count + 1):
            if self.listview.get_check_bl(row_num):
                select = self.listview.get_row_values_by_item(self.listview.get_row(row_num))
                selected.append(select)
                selected_info += ",".join(select)
                selected_info += "\n"

        return selected, selected_info
