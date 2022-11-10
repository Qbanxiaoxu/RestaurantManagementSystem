# -*- coding: utf-8 -*-
# author：xxp time:2022/11/9
# -*- coding: utf-8 -*-
# author：xxp time:2022/11/9
# Login and Registration window

import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import sample.dao.connect as connection
import sample.entity.Entity as Entity

# 登录窗口
window_login = tkinter.Tk()
# 标题
window_login.title('Welcome to the fast food restaurant management system')
# 设置窗口不可变
window_login.resizable(False, False)
# 屏幕宽和高
screen_width = window_login.winfo_screenwidth()
screen_height = window_login.winfo_screenheight()
# 屏幕大小和位置
window_login.geometry('%dx%d+%d+%d' % (690, 500, (screen_width - 690) / 2, (screen_height - 500) / 2))
# 画布用来放置图片
canvas = tkinter.Canvas(window_login, width=690, height=300)
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
username_input = tkinter.StringVar()
entry_username = tkinter.Entry(window_login, textvariable=username_input)
entry_username.place(x=270, y=320)
# 密码输入框
password_input = tkinter.StringVar()
entry_password = tkinter.Entry(window_login, textvariable=password_input)
entry_password.place(x=270, y=360)


# 登录操作
def signin():
    # 输入框获取用户名密码
    name = username_input.get()
    password = password_input.get()
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
            window_login.destroy()
            # TO DO 打开顾客界面
        if is_employee:
            tkinter.messagebox.showinfo(title='welcome',
                                        message='Welcome!' + name)
            window_login.destroy()
            # TO DO 打开雇员界面
        if not is_employee and not is_customer:
            is_signup = tkinter.messagebox.askyesno('Sign up?',
                                                    'You have not registered yet, do you want to register now?')
            if is_signup:
                window_login.destroy()
                signup()
    else:
        tkinter.messagebox.showerror(title='error', message='The user name or password is empty!')


def signup():
    def submit():
        username = username_signup.get()
        contact_info = contact_info_input.get()
        password = password_signup.get()
        password_confirm = confirm_password.get()
        if password == password_confirm:
            if username == '' or password == '' or contact_info == '':
                tkinter.messagebox.showerror(title='error',
                                             message='The user name or password or contact information is empty')
            else:
                my_database = connection.ConnectDatabase()

                # 获取数据库中的用户信息，顾客、雇员
                customers_info = my_database.query_customer()
                employees_info = my_database.query_employee()
                # 记录是顾客或雇员
                is_customer = False
                is_employee = False
                for customer in customers_info:
                    if username == customer["customer_name"] and password == customer["customer_password"]:
                        is_customer = True
                        break
                for employee in employees_info:
                    if username == employee["employee_name"] and password == employee["employee_password"]:
                        is_employee = True
                        break
                if is_customer or is_employee:
                    tkinter.messagebox.showerror(title='error', message='The user name is already in use!')
                else:
                    customer = Entity.Customer(None, username, password, contact_info)
                    my_database.add_customer(customer)
                    tkinter.messagebox.showinfo(title='signup result', message='Successful!')
                    window_signup.destroy()
        else:
            tkinter.messagebox.showerror(title='error', message='The password is inconsistent!')

    # 注册界面
    window_signup = tkinter.Tk()
    # 界面标题
    window_signup.title("signup")
    # 屏幕宽和高
    screen_width = window_signup.winfo_screenwidth()
    screen_height = window_signup.winfo_screenheight()
    # 界面大小位置
    window_signup.geometry('%dx%d+%d+%d' % (400, 250, (screen_width - 400) / 2, (screen_height - 200) / 2))
    window_signup.resizable(False, False)
    # 用户名输入
    username_signup = tkinter.StringVar()
    tkinter.Label(window_signup, text='username:').place(x=10, y=10)
    tkinter.Entry(window_signup, textvariable=username_signup).place(x=150, y=10)
    # 联系方式
    contact_info_input = tkinter.StringVar()
    tkinter.Label(window_signup, text='contact information:').place(x=10, y=50)
    tkinter.Entry(window_signup, textvariable=contact_info_input).place(x=150, y=50)
    # 密码输入
    password_signup = tkinter.StringVar()
    tkinter.Label(window_signup, text='password:').place(x=10, y=90)
    tkinter.Entry(window_signup, textvariable=password_signup, show='*').place(x=150, y=90)
    # 重复密码输入
    confirm_password = tkinter.StringVar()
    tkinter.Label(window_signup, text='confirm password:').place(x=10, y=130)
    tkinter.Entry(window_signup, textvariable=confirm_password, show='*').place(x=150, y=130)
    # 提交
    button_submit = tkinter.Button(window_signup, text="submit", command=submit)
    button_submit.place(x=200, y=170)


# 登录 注册按钮
button_signin = tkinter.Button(window_login, text="sign in", command=signin)
button_signin.place(x=270, y=400)
button_signup = tkinter.Button(window_login, text="sign up", command=signup)
button_signup.place(x=370, y=400)

window_login.mainloop()