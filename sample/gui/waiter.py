# -*- coding: utf-8 -*-
# author：xxp time:2022/11/9

import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import os

from sample.dao.connect import ConnectDatabase
from sample.entity.Entity import Employee
from sample.gui.waiterui import WaiterOperation


class WaiterUI:
    def __init__(self, username, password, position):
        self.username = username
        self.password = password
        self.position = position
        self.id = 0
        self.contact_info = None
        self.password_modify = None
        self.contact_info_modify = None
        self.username_modify = None
        self.gender = None
        self.id_number = None
        self.work_state = None
        self.basic_salary = None

        self.window_waiter = tkinter.Tk()
        # 标题
        self.window_waiter.title('Welcome to "Freedom Restaurant"')
        # 设置窗口不可变
        self.window_waiter.resizable(False, False)
        # 屏幕宽和高
        screen_width_waiter = self.window_waiter.winfo_screenwidth()
        screen_height_waiter = self.window_waiter.winfo_screenheight()
        # 屏幕大小和位置
        self.window_waiter.geometry(
            '%dx%d+%d+%d' % (1000, 700, (screen_width_waiter - 1000) / 2, (screen_height_waiter - 700) / 2 - 30))
        """
        show personal information
        """
        self.frame_personal_info = tkinter.Frame(self.window_waiter, bg="#F8F8FF",
                                                 highlightthickness=2, width=1000, height=150)
        self.frame_personal_info.grid(columnspan=100, rowspan=15)

        canvas = tkinter.Canvas(self.frame_personal_info, width=150, height=150)
        img = Image.open(os.path.realpath("../resources/waiter.png"))
        img.resize((150, 150))
        image_file = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor="nw", image=image_file)
        canvas.place(x=0, y=0, width=150, height=150)

        self.frame_detail = tkinter.Frame(self.frame_personal_info, bg="#F8F8FF",
                                          highlightthickness=2, width=850, height=150)
        self.frame_detail.place(x=150, y=0)
        self.personal_information()

        """
        操作容器
        """
        self.frame_operation = tkinter.Frame(self.window_waiter, bg="#DCDCDC",
                                             width=150, height=550)
        self.frame_operation.grid(columnspan=15, rowspan=55)

        btn_r = tkinter.Button(self.frame_operation, text="restaurant table information",
                               command=self.restaurant_table_info)
        btn_r.place(x=0, y=5, width=150, height=70)

        btn_m = tkinter.Button(self.frame_operation, text="menu information", command=self.menu_info)
        btn_m.place(x=0, y=95, width=150, height=70)

        # btn_e = tkinter.Button(self.frame_operation, text="employees information", command=self.employee_info)
        #
        # btn_e.place(x=0, y=185, width=150, height=70)

        btn_c = tkinter.Button(self.frame_operation, text="customers information", command=self.customer_info
                               )
        btn_c.place(x=0, y=275, width=150, height=70)

        btn_o = tkinter.Button(self.frame_operation, text='orders information', command=self.order_info)
        btn_o.place(x=0, y=365, width=150, height=70)

        btn_modify = tkinter.Button(self.frame_operation, text='modify personal info',
                                    command=self.modify_own_information)
        btn_modify.place(x=0, y=455, width=150, height=70)
        # 操作结果容器
        self.frame_result = tkinter.Frame(self.window_waiter, bg='#F0F8FF', width=850, height=550)
        self.frame_result.grid(column=15, row=15, columnspan=85, rowspan=55)

        self.window_waiter.mainloop()

    def menu_info(self):
        WaiterOperation(self.frame_result, 'menu')

    def restaurant_table_info(self):
        WaiterOperation(self.frame_result, 'restaurant_table')

    def employee_info(self):
        WaiterOperation(self.frame_result, 'employee')

    def customer_info(self):
        WaiterOperation(self.frame_result, 'customer')

    def order_info(self):
        WaiterOperation(self.frame_result, 'order')

    def personal_information(self):
        me = ConnectDatabase('admin').find_employ(self.username, self.password, self.position)
        self.username = me.employee_name
        self.password = me.employee_password
        self.id = me.employee_id
        self.contact_info = me.contact_info
        self.position = me.position
        self.gender = me.gender
        self.id_number = me.id_number
        self.basic_salary = me.basic_salary
        self.work_state = me.work_state

        tkinter.Label(self.frame_detail, text="ID:", font=("宋体", 14)).place(x=30, y=16, height=20)
        tkinter.Message(self.frame_detail, text=self.id,
                        font=("宋体", 14), width=200).place(x=240, y=16, height=20)

        tkinter.Label(self.frame_detail, text="name:", font=("宋体", 14)).place(x=30, y=47, height=20)
        tkinter.Message(self.frame_detail, text=self.username,
                        font=("宋体", 16), width=200).place(x=240, y=47, height=20)

        tkinter.Label(self.frame_detail, text="contact information:", font=("宋体", 14)).place(x=30, y=78,
                                                                                             height=20)
        tkinter.Message(self.frame_detail, text=self.contact_info,
                        font=("宋体", 14), width=200).place(x=240, y=78, height=20)

        tkinter.Label(self.frame_detail, text="gender:", font=("宋体", 14)).place(x=30, y=109, height=20)
        tkinter.Message(self.frame_detail, text=self.gender,
                        font=("宋体", 14), width=200).place(x=240, y=109, height=20)
        # di er lie
        tkinter.Label(self.frame_detail, text="id_number:", font=("宋体", 14)).place(x=450, y=14, height=20)
        tkinter.Message(self.frame_detail, text=self.id_number,
                        font=("宋体", 14), width=200).place(x=650, y=16, height=20)

        tkinter.Label(self.frame_detail, text="position:", font=("宋体", 14)).place(x=450, y=47,
                                                                                  height=20)
        tkinter.Message(self.frame_detail, text=self.position,
                        font=("宋体", 14), width=200).place(x=650, y=47, height=20)

        tkinter.Label(self.frame_detail, text="work_state:", font=("宋体", 14)).place(x=450, y=78, height=20)
        tkinter.Message(self.frame_detail, text=self.work_state,
                        font=("宋体", 14), width=200).place(x=650, y=78, height=20)

        tkinter.Label(self.frame_detail, text="basic salary:", font=("宋体", 14)).place(x=450, y=109,
                                                                                      height=20)
        tkinter.Message(self.frame_detail, text=self.basic_salary,
                        font=("宋体", 14), width=200).place(x=650, y=109, height=20)

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
        self.username = self.username_modify.get()
        self.password = self.password_modify.get()
        self.contact_info = self.contact_info_modify.get()
        host = Employee(employee_id=self.id, employee_name=self.username, employee_password=self.password,
                        contact_info=self.contact_info, gender='', position='', work_state='',
                        basic_salary=0, id_number='')
        personal_info = "id:" + str(
            self.id) + "\nname:" + self.username + "\npassword:" + self.password + "\ncontact_info:" + self.contact_info
        tkinter.messagebox.showinfo('modifying the result', personal_info)
        ConnectDatabase('admin').modify_employee(host)
        for widget in self.frame_detail.winfo_children():
            widget.destroy()
        tkinter.messagebox.showerror('Please log out and log in again', personal_info)
        self.window_waiter.destroy()

    def destroy_result(self):
        for widget in self.frame_result.winfo_children():
            widget.destroy()
