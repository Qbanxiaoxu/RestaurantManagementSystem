# -*- coding: utf-8 -*-
# author：xxp time:2022/11/9
# -*- coding: utf-8 -*-
# author：xxp time:2022/11/9
# Login and Registration window

import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import sample.dao.connect as connection
import sample.gui.signup as new_signup
import os

from sample.gui.cashier import CashierUI
from sample.gui.chef import ChefUI
from sample.gui.cleaner import CleanerUI
from sample.gui.customer import CustomerUI
from sample.gui.manager import ManagerUI
from sample.gui.waiter import WaiterUI


class LoginUI:
    def __init__(self):
        # 登录窗口
        self.window_login = tkinter.Tk()
        # 标题
        self.window_login.title('Welcome to the fast food restaurant management system')
        # 设置窗口不可变
        self.window_login.resizable(False, False)
        # 屏幕宽和高
        screen_width_login = self.window_login.winfo_screenwidth()
        screen_height_login = self.window_login.winfo_screenheight()
        # 屏幕大小和位置
        self.window_login.geometry(
            '%dx%d+%d+%d' % (690, 500, (screen_width_login - 690) / 2, (screen_height_login - 500) / 2))
        # 画布用来放置图片
        canvas = tkinter.Canvas(self.window_login, width=690, height=300)
        # 打开图像
        img = Image.open(os.path.realpath("../resources/Login.jpg"))
        # 使图像兼容
        image_file = ImageTk.PhotoImage(img)
        # 在画布上放置图片
        canvas.create_image(0, 0, anchor="nw", image=image_file)
        # 画布在登录窗口的位置
        canvas.pack(side='top')
        # 标签 用户名和密码
        tkinter.Label(self.window_login, text="username:").place(x=200, y=320)
        tkinter.Label(self.window_login, text="password:").place(x=200, y=360)
        # 用户名输入框
        self.username_input_login = tkinter.StringVar()
        entry_username = tkinter.Entry(self.window_login, textvariable=self.username_input_login)
        entry_username.place(x=270, y=320)
        # 密码输入框
        self.password_input_login = tkinter.StringVar()
        entry_password = tkinter.Entry(self.window_login, textvariable=self.password_input_login)
        entry_password.place(x=270, y=360)

        # 登录 注册按钮
        button_signin = tkinter.Button(self.window_login, text="sign in", command=self.signin)
        button_signin.place(x=270, y=400)
        button_signup = tkinter.Button(self.window_login, text="sign up", command=self.signup)
        button_signup.place(x=370, y=400)

        self.window_login.mainloop()

    # 登录操作
    def signin(self):
        # 输入框获取用户名密码
        username = self.username_input_login.get()
        password = self.password_input_login.get()

        # 判断用户名和密码是否匹配
        if username != '' and password != '':
            # 记录是顾客或雇员
            is_customer_signin, is_employee_signin = connection.ConnectDatabase().verify(username, password)
            if is_customer_signin:
                tkinter.messagebox.showinfo(title='welcome',
                                            message='Welcome!' + username)
                self.window_login.destroy()
                # TODO 打开顾客界面
                CustomerUI(username, password)
            if is_employee_signin:
                tkinter.messagebox.showinfo(title='welcome',
                                            message='Welcome!' + username)
                self.window_login.destroy()
                # TODO 打开雇员界面
                # TODO 判断雇员身份跳转不同界面
                position = connection.ConnectDatabase().get_employee_position(username, password)
                if position == 'manager':
                    ManagerUI(username, password, position)
                elif position == 'cashier':
                    CashierUI(username, password, position)
                elif position == 'waiter':
                    WaiterUI(username, password, position)
                elif position == 'chef':
                    ChefUI(username, password, position)
                elif position == 'cleaner':
                    CleanerUI(username, password, position)
                else:
                    tkinter.messagebox.showerror('wrong', 'mei zhao dao')

            if not is_customer_signin and not is_employee_signin:
                is_signup = tkinter.messagebox.askyesno('Sign up?',
                                                        'You have not registered yet, do you want to register now?')
                if is_signup:
                    # window_login.destroy()
                    self.signup()
        else:
            tkinter.messagebox.showerror(title='error', message='The user name or password is empty!')

    def signup(self):
        self.window_login.destroy()
        new_signup.SignupUI()
