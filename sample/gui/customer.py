# -*- coding: utf-8 -*-
# author：xxp time:2022/11/9

import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import VERTICAL, HORIZONTAL
import os

from sample.dao.connect import ConnectDatabase
from sample.entity.Entity import Customer
from sample.gui.formui import RestaurantUI, ShoppingCartUI


class CustomerUI:
    def __init__(self, username, password):
        self.window_customer = tkinter.Tk()

        self.shopping_cart_all_id = []
        # 标题
        self.window_customer.title('Welcome to "Freedom Restaurant"')
        # 设置窗口不可变
        self.window_customer.resizable(False, False)
        # 屏幕宽和高
        screen_width_login = self.window_customer.winfo_screenwidth()
        screen_height_login = self.window_customer.winfo_screenheight()
        # 屏幕大小和位置
        self.window_customer.geometry(
            '%dx%d+%d+%d' % (1000, 700, (screen_width_login - 1000) / 2, (screen_height_login - 700) / 2 - 30))
        """
        show personal information
        """
        self.frame_personal_info = tkinter.Frame(self.window_customer, bg="#F8F8FF",
                                                 highlightthickness=2, width=1000, height=150)
        self.frame_personal_info.grid(columnspan=100, rowspan=15)

        canvas = tkinter.Canvas(self.frame_personal_info, width=150, height=150)
        img = Image.open(os.path.realpath("../resources/customer.jpg"))
        img.resize((150, 150))
        image_file = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor="nw", image=image_file)
        canvas.place(x=0, y=0, width=150, height=150)

        me = ConnectDatabase.find_customer(username, password)
        # 顾客信息
        self.password_modify = None
        self.contact_info_modify = None
        self.username_modify = None
        self.username = me.customer_name
        self.password = me.customer_password
        self.id = me.customer_id
        self.contact_info = me.contact_info

        tkinter.Label(self.frame_personal_info, text="ID:", font=("宋体", 16)).place(x=225, y=25, height=30)
        tkinter.Message(self.frame_personal_info, text=self.id,
                        font=("宋体", 16), width=200).place(x=325, y=25, height=30)

        tkinter.Label(self.frame_personal_info, text="name:", font=("宋体", 16)).place(x=225, y=55, height=30)
        tkinter.Message(self.frame_personal_info, text=self.username,
                        font=("宋体", 16), width=200).place(x=325, y=55, height=30)

        tkinter.Label(self.frame_personal_info, text="contact information:", font=("宋体", 16)).place(x=550, y=25,
                                                                                                    height=30)
        tkinter.Message(self.frame_personal_info, text=self.contact_info,
                        font=("宋体", 16), width=200).place(x=800, y=25, height=30)

        """
        操作容器
        """
        self.frame_operation = tkinter.Frame(self.window_customer, bg="#DCDCDC",
                                             width=150, height=550)
        self.frame_operation.grid(columnspan=15, rowspan=55)
        # 逛店铺，查看购物车，修改个人信息，下单，查看订单
        btn_choose = tkinter.Button(self.frame_operation, text="choose restaurant", command=self.choose)
        btn_choose.place(x=0, y=10, width=150, height=90)

        btn_shopping_cart = tkinter.Button(self.frame_operation, text="shopping cart", command=self.shopping_cart)
        btn_shopping_cart.place(x=0, y=120, width=150, height=90)

        btn_modify_personal_info = tkinter.Button(self.frame_operation, text="modify personal info",
                                                  command=self.modify_own_information
                                                  )
        btn_modify_personal_info.place(x=0, y=230, width=150, height=90)

        btn_place_order = tkinter.Button(self.frame_operation, text='display order form')
        btn_place_order.place(x=0, y=340, width=150, height=90)

        btn_check_order = tkinter.Button(self.frame_operation, text='null')
        btn_check_order.place(x=0, y=450, width=150, height=90)
        # 操作结果容器
        self.frame_result = tkinter.Frame(self.window_customer, bg='#F0F8FF', width=850, height=550)
        self.frame_result.grid(column=15, row=15, columnspan=85, rowspan=55)

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=("黑体", 15))
        self.style.configure('Treeview', rowheight=30, font=(None, 15))

        self.window_customer.mainloop()

    def choose(self):
        self.destroy_result()
        restaurant = RestaurantUI(self.frame_result)

    def shopping_cart(self):
        self.destroy_result()
        shoppingcart = ShoppingCartUI(self.frame_result)

    def modify_own_information(self):
        self.destroy_result()
        # 用户名输入
        self.username_modify = tkinter.StringVar()
        tkinter.Label(self.frame_result, text='new username:').place(x=220, y=160)
        tkinter.Entry(self.frame_result, textvariable=self.username_modify).place(x=400, y=160)
        # 联系方式
        self.contact_info_modify = tkinter.StringVar()
        tkinter.Label(self.frame_result, text='new contact information:').place(x=220, y=210)
        tkinter.Entry(self.frame_result, textvariable=self.contact_info_modify).place(x=400, y=210)
        # 密码输入
        self.password_modify = tkinter.StringVar()
        tkinter.Label(self.frame_result, text='new password:').place(x=220, y=260)
        tkinter.Entry(self.frame_result, textvariable=self.password_modify).place(x=400, y=260)

        btn_modify = tkinter.Button(self.frame_result, text="commit changes", command=self.commit_changes)
        btn_modify.place(x=300, y=480, width=200, height=50)

    def commit_changes(self):
        host = Customer(self.id, self.username_modify, self.password_modify, self.contact_info_modify)
        ConnectDatabase().modify_customer(host)
        self.window_customer.update()

    def destroy_result(self):
        for widget in self.frame_result.winfo_children():
            widget.destroy()
