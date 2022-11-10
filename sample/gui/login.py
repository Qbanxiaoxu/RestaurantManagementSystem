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


class Login:
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
        img = Image.open("Login.jpg")
        # 使图像兼容
        image_file = ImageTk.PhotoImage(img)
        # 在画布上放置图片
        image = canvas.create_image(0, 0, anchor="nw", image=image_file)
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
        name = self.username_input_login.get()
        password = self.password_input_login.get()
        my_database = connection.ConnectDatabase()

        # 获取数据库中的用户信息，顾客、雇员
        customers_info = my_database.query_customer()
        employees_info = my_database.query_employee()

        # 判断用户名和密码是否匹配
        if name != '' and password != '':
            # 记录是顾客或雇员
            is_customer_signin = False
            is_employee_signin = False
            for customer in customers_info:
                if name == customer["customer_name"] and password == customer["customer_password"]:
                    is_customer_signin = True
                    break
            for employee in employees_info:
                if name == employee["employee_name"] and password == employee["employee_password"]:
                    is_employee_signin = True
                    break
            if is_customer_signin:
                tkinter.messagebox.showinfo(title='welcome',
                                            message='Welcome!' + name)
                self.window_login.destroy()
                # TO DO 打开顾客界面
            if is_employee_signin:
                tkinter.messagebox.showinfo(title='welcome',
                                            message='Welcome!' + name)
                self.window_login.destroy()
                # TO DO 打开雇员界面
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
        new_signup.Signup()


test = Login()
