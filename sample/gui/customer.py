# -*- coding: utf-8 -*-
# author：xxp time:2022/11/9

import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import sample.dao.connect as connection
import os


class CustomerUI:
    def __init__(self, username, password):
        # 顾客信息
        self.username = username
        self.password = password
        self.window_customer = tkinter.Tk()
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
        # 个人信息容器
        self.frame_personal_info = tkinter.Frame(self.window_customer, bg="#F8F8FF",
                                                 highlightthickness=2, width=1000, height=150)
        self.frame_personal_info.grid(columnspan=100, rowspan=15)

        canvas = tkinter.Canvas(self.frame_personal_info, width=150, height=150)
        img = Image.open(r"E:\Python\RestaurantManagementSystem\resources\customer.jpg")
        img.resize((150, 150))
        image_file = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor="nw", image=image_file)
        canvas.place(x=0, y=0, width=150, height=150)
        # 操作容器
        self.frame_operation = tkinter.Frame(self.window_customer, bg="#DCDCDC",
                                             width=150, height=550)
        self.frame_operation.grid(columnspan=15, rowspan=55)
        # 逛店铺，查看购物车，修改个人信息，下单，查看订单
        btn_choose = tkinter.Button(self.frame_operation, text="choose restaurant")
        btn_choose.place(x=0, y=10, width=150, height=90)
        btn_shopping_cart = tkinter.Button(self.frame_operation, text="shopping cart")
        btn_shopping_cart.place(x=0, y=120, width=150, height=90)
        btn_modify_personal_info = tkinter.Button(self.frame_operation, text="modify personal info")
        btn_modify_personal_info.place(x=0, y=230, width=150, height=90)
        btn_place_order = tkinter.Button(self.frame_operation, text='place order')
        btn_place_order.place(x=0, y=340, width=150, height=90)
        btn_check_order = tkinter.Button(self.frame_operation, text='check order')
        btn_check_order.place(x=0, y=450, width=150, height=90)
        # 操作结果容器
        self.frame_result = tkinter.Frame(self.window_customer, bg='#F0F8FF', width=850, height=550)
        self.frame_result.grid(column=15, row=15, columnspan=85, rowspan=55)
        self.window_customer.mainloop()


CustomerUI("xx", "xxx")
