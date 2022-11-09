# -*- coding: utf-8 -*-
# author：xxp time:2022/11/9

import tkinter
import tkinter.messagebox
import pickle
from PIL import Image, ImageTk

# 窗口
window = tkinter.Tk()
window.title('Welcome to the fast food restaurant management system')
# window.geometry('690x500')
window.resizable(False, False)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry('%dx%d+%d+%d' % (690, 500, (screenwidth - 690) / 2, (screenheight - 500) / 2))
# 画布放置图片
canvas = tkinter.Canvas(window, height=300, width=800)
img = Image.open('Login.jpg')
image_file = ImageTk.PhotoImage(img)
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')


# 登录函数
def usr_log_in():
    # 输入框获取用户名密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    # 判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tkinter.messagebox.showinfo(title='welcome',
                                        message='Welcome!' + usr_name)
            window.destroy()
            # Image_sys()       #打开主界面

        else:
            tkinter.messagebox.showerror(message='密码错误')
    # 用户名密码不能为空
    elif usr_name == '' or usr_pwd == '':
        tkinter.messagebox.showerror(message='用户名或密码为空', )
    # 不在数据库中弹出是否注册的框
    else:
        is_signup = tkinter.messagebox.askyesno('Sign up?', 'You have not registered yet, do you want to register now?')
        if is_signup:
            usr_signup()  # 打开注册界面


# 标签 用户名密码
tkinter.Label(window, text='用户名:').place(x=200, y=320)
tkinter.Label(window, text='密码:').place(x=200, y=360)
# 用户名输入框
var_usr_name = tkinter.StringVar()

entry_usr_name = tkinter.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=250, y=320)
# 密码输入框
var_usr_pwd = tkinter.StringVar()
entry_usr_pwd = tkinter.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=260, y=360)


# 注册函数
def usr_signup():
    # 确认注册时的相应函数

    def signtowcg():
        # 获取输入框内的内容
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

            # 检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tkinter.messagebox.showerror('错误', '用户名已存在')
        elif np == '' or nn == '':
            tkinter.messagebox.showerror('错误', '用户名或密码为空')
        elif np != npf:
            tkinter.messagebox.showerror('错误', '密码前后不一致')
        # 注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tkinter.messagebox.showinfo('欢迎', '注册成功')
            # 注册成功关闭注册框
            window_signup.destroy()

    # 新建注册界面
    # window_signup = tkinter.Toplevel(window)
    window_signup = tkinter.Tk()
    window_signup.geometry('%dx%d+%d+%d' % (400, 200, (screenwidth - 400) / 2, (screenheight - 200) / 2))
    # window_signup.geometry('350x200')
    window_signup.title('注册')
    # 用户名变量及标签、输入框
    new_name = tkinter.StringVar()
    tkinter.Label(window_signup, text='用户名：').place(x=10, y=10)
    tkinter.Entry(window_signup, textvariable=new_name).place(x=150, y=10)
    # 密码变量及标签、输入框
    new_pwd = tkinter.StringVar()
    tkinter.Label(window_signup, text='请输入密码：').place(x=10, y=50)
    tkinter.Entry(window_signup, textvariable=new_pwd, show='*').place(x=150, y=50)
    # 重复密码变量及标签、输入框
    new_pwd_confirm = tkinter.StringVar()
    tkinter.Label(window_signup, text='请再次输入密码：').place(x=10, y=90)
    tkinter.Entry(window_signup, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    # 确认注册按钮及位置
    bt_confirm_signup = tkinter.Button(window_signup, text='确认注册',
                                        command=signtowcg)
    bt_confirm_signup.place(x=150, y=130)
    window.destroy()


# 登录 注册按钮
bt_login = tkinter.Button(window, text='登录', command=usr_log_in)
bt_login.place(x=280, y=400)
bt_logup = tkinter.Button(window, text='注册', command=usr_signup)
bt_logup.place(x=350, y=400)
window.mainloop()
