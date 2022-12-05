# -*- coding: utf-8 -*-
# author：xxp time:2022/11/10

import tkinter
import tkinter.messagebox
import sample.dao.connect as connection
import sample.entity.Entity as Entity


class SignupUI:
    def __init__(self):
        # 注册界面
        self.window_signup = tkinter.Tk()
        # 界面标题
        self.window_signup.title("signup")
        # 屏幕宽和高
        screen_width_signup = self.window_signup.winfo_screenwidth()
        screen_height_signup = self.window_signup.winfo_screenheight()
        # 界面大小位置
        self.window_signup.geometry(
            '%dx%d+%d+%d' % (400, 250, (screen_width_signup - 400) / 2, (screen_height_signup - 200) / 2))
        self.window_signup.resizable(False, False)
        # 用户名输入
        self.username_input_signup = tkinter.StringVar()
        tkinter.Label(self.window_signup, text='username:').place(x=10, y=10)
        tkinter.Entry(self.window_signup, textvariable=self.username_input_signup).place(x=150, y=10)
        # 联系方式
        self.contact_info_input = tkinter.StringVar()
        tkinter.Label(self.window_signup, text='contact information:').place(x=10, y=50)
        tkinter.Entry(self.window_signup, textvariable=self.contact_info_input).place(x=150, y=50)
        # 密码输入
        self.password_input_signup = tkinter.StringVar()
        tkinter.Label(self.window_signup, text='password:').place(x=10, y=90)
        tkinter.Entry(self.window_signup, textvariable=self.password_input_signup, show='*').place(x=150, y=90)
        # 重复密码输入
        self.confirm_password = tkinter.StringVar()
        tkinter.Label(self.window_signup, text='confirm password:').place(x=10, y=130)
        tkinter.Entry(self.window_signup, textvariable=self.confirm_password, show='*').place(x=150, y=130)
        # 提交
        button_submit = tkinter.Button(self.window_signup, text="submit", command=self.submit)
        button_submit.place(x=200, y=170)

        self.window_signup.mainloop()

    def submit(self):
        username = self.username_input_signup.get()
        contact_info = self.contact_info_input.get()
        password = self.password_input_signup.get()
        password_confirm = self.confirm_password.get()
        if password == password_confirm:
            if username == '' or password == '' or contact_info == '':
                tkinter.messagebox.showerror(title='error',
                                             message='The user name or password or contact information is empty')
            else:
                # 记录是顾客或雇员
                is_customer_signup, is_employee_signup = connection.ConnectDatabase('admin').verify(username, password)
                if is_customer_signup or is_employee_signup:
                    tkinter.messagebox.showerror(title='error', message='The user name is already in use!')
                else:
                    customer = Entity.Customer(None, username, password, contact_info)
                    connection.ConnectDatabase('admin').add_customer(customer)
                    tkinter.messagebox.showinfo(title='signup result', message='Successful!')
                    self.window_signup.destroy()
        else:
            tkinter.messagebox.showerror(title='error', message='The password is inconsistent!')
