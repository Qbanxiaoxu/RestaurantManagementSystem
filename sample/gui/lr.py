# -*- coding: utf-8 -*-
# author：xxp time:2022/11/9
# Login and Registration window

import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import sample.dao.connect as connection


class Login:
    # 登录窗口
    window_login = tkinter.Tk()
    # 标题
    window_login.title('Welcome to the fast food restaurant management system')
    # 设置窗口不可变
    window_login.resizable(False, False)
    # 屏幕宽和高
    screen_width = window_login.winfo_width()
    screen_height = window_login.winfo_height()
    # 屏幕大小和位置
    window_login.geometry('%dx%d+%d+%d' % (690, 500, (screen_width - 690) / 2, (screen_height - 500) / 2))
    # 画布用来放置图片
    canvas = tkinter.Canvas(window_login, width=500, height=300)
    # 打开图像
    img = Image.open("Login.jpg")
    # 使图像兼容
    image_file = ImageTk.PhotoImage(img)
    # 在画布上放置图片
    image = canvas.create_image(0, 0, anchor="nw", image=image_file)
    # 画布在登录窗口的位置
    canvas.pack(side='top')
    # 标签 用户名和密码
    tkinter.Label(window_login, text="username:").place(x=200, y=320)
    tkinter.Label(window_login, text="password:").place(x=200, y=360)
    # 用户名输入框
    username = tkinter.StringVar()
    entry_username = tkinter.Entry(window_login, textvariable=username)
    entry_username.place(x=250, y=320)
    # 密码输入框
    password = tkinter.StringVar()
    entry_password = tkinter.Entry(window_login, textvariable=password)
    entry_password.place(x=250, y=360)
    # 登录 注册按钮
    button_signin = tkinter.Button(window_login, text="sign in", compound=self.signin)
    button_signin.place(x=280, y=400)
    button_signup = tkinter.Button(window_login, text="sign up", compound="")
    button_signup.place(x=350, y=400)

    # 初始化对象，创建登录窗口
    def __init__(self):

        self.window_login.mainloop()

    # 登录操作
    def signin(self):
        # 输入框获取用户名密码
        name = self.username.get()
        password = self.password.get()
        my_database = connection.ConnectDatabase()

        # 获取数据库中的用户信息，顾客、雇员
        customers_info = my_database.query_customer()
        employees_info = my_database.query_employee()

        # 判断用户名和密码是否匹配
        if name != '' and password != '':
            # 记录是顾客或雇员
            is_customer = False
            is_employee = False
            for customer in customers_info:
                if name == customer["customer_name"] and password == customer["customer_password"]:
                    is_customer = True
                    break
            for employee in employees_info:
                if name == employee["employee_name"] and password == employee["employee_password"]:
                    is_employee = True
                    break
            if is_customer:
                tkinter.messagebox.showinfo(title='welcome',
                                            message='Welcome!' + name)
                self.window_login.destroy()
                # TO DO 打开顾客界面
            if is_employee:
                tkinter.messagebox.showinfo(title='welcome',
                                            message='Welcome!' + name)
                self.window_login.destroy()
                # TO DO 打开雇员界面
            if not is_employee and not is_customer:
                is_signup = tkinter.messagebox.askyesno('Sign up?',
                                                        'You have not registered yet, do you want to register now?')
                if is_signup:
                    self.window_login.destroy()
                    # TO DO 打开注册页面


class Signup:
    # 注册界面
    window_signup = tkinter.Tk()
    # 界面标题
    window_signup.title("signup")
    # 屏幕宽和高
    screen_width = window_signup.winfo_width()
    screen_height = window_signup.winfo_height()
    # 界面大小位置
    window_signup.geometry('%dx%d+%d+%d' % (400, 200, (screen_width - 400) / 2, (screen_height - 200) / 2))
    # 用户名输入
    username = tkinter.StringVar()
    tkinter.Label(window_signup, text='username:').place(x=10, y=10)
    tkinter.Entry(window_signup, textvariable=username).place(x=150, y=10)
    # 密码输入
    password = tkinter.StringVar()
    tkinter.Label(window_signup, text='password:').place(x=10, y=50)
    tkinter.Entry(window_signup, textvariable=password, show='*').place(x=150, y=50)
    # 重复密码输入
    confirm_password = tkinter.StringVar()
    tkinter.Label(window_signup, text='confirm password:').place(x=10, y=90)
    tkinter.Entry(window_signup, textvariable=confirm_password, show='*').place(x=150, y=90)
    # 提交
    button_submit = tkinter.Button(window_signup, text="submit", compound="")
    button_submit.place(x=150, y=130)

    # 初始化对象，创建窗口
    def __int__(self):
        self.window_signup.mainloop()
    def signup(self):
