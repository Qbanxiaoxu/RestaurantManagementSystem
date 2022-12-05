# -*- coding: utf-8 -*-
# author：xxp time:2022/11/16
# Add, delete, check and change
import tkinter
from tkinter import messagebox
from sample.dao.connect import ConnectDatabase
from sample.entity.Entity import Restaurant, Menu, Employee, Customer, Order
from sample.gui.listview import ListViewUI


class ManagerOperation:
    def __init__(self, frame, form_type):
        self.frame = frame
        self.form_type = form_type
        self.destroy_frame()
        self.check_id = None
        self.listview = ListViewUI(self.frame)
        if form_type == 'restaurant':
            self.restaurant_name = None
            self.restaurant_address = None
            self.listview.add_column('restaurant_id')
            self.listview.add_column('restaurant_name')
            self.listview.add_column('restaurant_address')
            self.listview.set_rows_height_fontsize()
            self.listview.set_head_font()
            self.listview.create_listview()
            self.restaurants = ConnectDatabase('admin').query_restaurant()
            for r in self.restaurants:
                restaurant = [r['restaurant_id'], r['restaurant_name'], r['restaurant_address']]
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
        if form_type == 'employee':
            self.employee_name = None
            self.employee_password = None
            self.gender = None
            self.id_number = None
            self.employee_contact_info = None
            self.position = None
            self.word_state = None
            self.basic_salary = None

            self.listview.add_column('employee_id')
            self.listview.add_column('employee_name')
            self.listview.add_column('gender')
            self.listview.add_column('id_number')
            self.listview.add_column('contact_info')
            self.listview.add_column('position')
            self.listview.add_column('work_state')
            self.listview.add_column('basic_salary')
            self.listview.add_column('employee_password')
            self.listview.set_rows_height_fontsize()
            self.listview.set_head_font()
            self.listview.create_listview()

            self.employees = ConnectDatabase('admin').query_employee()
            for e in self.employees:
                employee = [e['employee_id'], e['employee_name'], e['gender'],
                            e['id_number'], e['contact_info'], e['position'],
                            e['work_state'], e['basic_salary'], e['employee_password']]
                self.listview.add_row(False, employee)
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

        btn_modify = tkinter.Button(self.frame, text="add", command=self.add)
        btn_modify.place(x=100, y=480, width=100, height=50)

        btn_delete = tkinter.Button(self.frame, text="delete", command=self.delete)
        btn_delete.place(x=250, y=480, width=100, height=50)

        btn_modify = tkinter.Button(self.frame, text="check", command=self.check)
        btn_modify.place(x=400, y=480, width=100, height=50)

        btn_delete = tkinter.Button(self.frame, text="change", command=self.change)
        btn_delete.place(x=550, y=480, width=100, height=50)

    def add(self):
        self.destroy_frame()
        if self.form_type == 'restaurant':
            self.destroy_frame()
            self.restaurant_name = tkinter.StringVar()
            tkinter.Label(self.frame, text='restaurant_name:').place(x=220, y=160)
            tkinter.Entry(self.frame, textvariable=self.restaurant_name).place(x=400, y=160)

            self.restaurant_address = tkinter.StringVar()
            tkinter.Label(self.frame, text='restaurant_address:').place(x=220, y=210)
            tkinter.Entry(self.frame, textvariable=self.restaurant_address).place(x=400, y=210)

            btn_modify = tkinter.Button(self.frame, text="add", command=self.commit_add)
            btn_modify.place(x=300, y=480, width=200, height=50)
        if self.form_type == 'menu':
            self.dish_name = tkinter.StringVar()
            tkinter.Label(self.frame, text='dish_name:').place(x=220, y=160)
            tkinter.Entry(self.frame, textvariable=self.dish_name).place(x=400, y=160)

            self.dish_price = tkinter.DoubleVar()
            tkinter.Label(self.frame, text='dish_price:').place(x=220, y=210)
            tkinter.Entry(self.frame, textvariable=self.dish_price).place(x=400, y=210)

            self.dish_description = tkinter.StringVar()
            tkinter.Label(self.frame, text='dish_description:').place(x=220, y=260)
            tkinter.Entry(self.frame, textvariable=self.dish_description).place(x=400, y=260)

            btn_modify = tkinter.Button(self.frame, text="add", command=self.commit_add)
            btn_modify.place(x=300, y=480, width=200, height=50)
        if self.form_type == 'employee':
            self.employee_name = tkinter.StringVar()
            tkinter.Label(self.frame, text='employee_name:').place(x=220, y=15)
            tkinter.Entry(self.frame, textvariable=self.employee_name).place(x=400, y=15)

            self.employee_password = tkinter.StringVar()
            tkinter.Label(self.frame, text='employee_password:').place(x=220, y=75)
            tkinter.Entry(self.frame, textvariable=self.employee_password).place(x=400, y=75)

            self.employee_contact_info = tkinter.StringVar()
            tkinter.Label(self.frame, text='employee_contact_info:').place(x=220, y=135)
            tkinter.Entry(self.frame, textvariable=self.employee_contact_info).place(x=400, y=135)

            self.gender = tkinter.StringVar()
            tkinter.Label(self.frame, text='gender:').place(x=220, y=195)
            tkinter.Entry(self.frame, textvariable=self.gender).place(x=400, y=195)

            self.id_number = tkinter.StringVar()
            tkinter.Label(self.frame, text='id_number:').place(x=220, y=255)
            tkinter.Entry(self.frame, textvariable=self.id_number).place(x=400, y=255)

            self.position = tkinter.StringVar()
            tkinter.Label(self.frame, text='position:').place(x=220, y=315)
            tkinter.Entry(self.frame, textvariable=self.position).place(x=400, y=315)

            self.word_state = tkinter.StringVar()
            tkinter.Label(self.frame, text='word_state:').place(x=220, y=375)
            tkinter.Entry(self.frame, textvariable=self.word_state).place(x=400, y=375)

            self.basic_salary = tkinter.DoubleVar()
            tkinter.Label(self.frame, text='basic_salary:').place(x=220, y=430)
            tkinter.Entry(self.frame, textvariable=self.basic_salary).place(x=400, y=430)

            btn_modify = tkinter.Button(self.frame, text="add", command=self.commit_add)
            btn_modify.place(x=300, y=480, width=200, height=50)
        if self.form_type == 'customer':
            self.customer_name = tkinter.StringVar()
            tkinter.Label(self.frame, text='customer_name:').place(x=220, y=160)
            tkinter.Entry(self.frame, textvariable=self.customer_name).place(x=400, y=160)

            self.customer_password = tkinter.StringVar()
            tkinter.Label(self.frame, text='customer_password:').place(x=220, y=210)
            tkinter.Entry(self.frame, textvariable=self.customer_password).place(x=400, y=210)

            self.customer_contact_info = tkinter.StringVar()
            tkinter.Label(self.frame, text='customer_contact_info:').place(x=220, y=260)
            tkinter.Entry(self.frame, textvariable=self.customer_contact_info).place(x=400, y=260)

            btn_modify = tkinter.Button(self.frame, text="add", command=self.commit_add)
            btn_modify.place(x=300, y=480, width=200, height=50)
        if self.form_type == 'order':
            tkinter.messagebox.showerror("Wrong operation", "Adding orders is not supported!")

    def commit_add(self):
        if self.form_type == 'restaurant':
            restaurant_name = self.restaurant_name.get()
            restaurant_address = self.restaurant_address.get()
            restaurant = Restaurant(restaurant_id=None, restaurant_address=restaurant_address,
                                    restaurant_name=restaurant_name)
            ConnectDatabase('admin').add_restaurant(restaurant)
            tkinter.messagebox.showinfo('add', "Restaurant added successfully!")
        if self.form_type == 'menu':
            dish_name = self.dish_name.get()
            dish_price = self.dish_price.get()
            dish_description = self.dish_description.get()
            dish = Menu(dish_id=None, dish_name=dish_name, dish_price=float(dish_price),
                        dish_description=dish_description)
            ConnectDatabase('admin').add_menu(dish)
            tkinter.messagebox.showinfo('add', "Dish added successfully!")
        if self.form_type == 'employee':
            employee_name = self.employee_name.get()
            employee_password = self.employee_password.get()
            employee_contact_info = self.employee_contact_info.get()
            gender = self.gender.get()
            id_number = self.id_number.get()
            position = self.position.get()
            word_state = self.word_state.get()
            basic_salary = self.basic_salary.get()
            employee = Employee(employee_id=None, employee_password=employee_password,
                                employee_name=employee_name, contact_info=employee_contact_info,
                                gender=gender, work_state=word_state, basic_salary=basic_salary,
                                id_number=id_number, position=position)
            ConnectDatabase('admin').add_employee(employee)
            tkinter.messagebox.showinfo('add', "Employee added successfully!")
        if self.form_type == 'customer':
            customer_name = self.customer_name.get()
            customer_password = self.customer_password.get()
            customer_contact_info = self.customer_contact_info.get()
            customer = Customer(customer_id=None, customer_name=customer_name,
                                customer_password=customer_password, contact_info=customer_contact_info)
            ConnectDatabase('admin').add_customer(customer)
            tkinter.messagebox.showinfo('add', "Customer added successfully!")

    def delete(self):
        selected, selected_info = self.get_selected()
        is_delete = tkinter.messagebox.askyesno('Confirm delete?',
                                                selected_info)
        if is_delete:
            if self.form_type == 'restaurant':
                for select in selected:
                    ConnectDatabase('admin').delete_restaurant(select[1])
            if self.form_type == 'menu':
                for select in selected:
                    ConnectDatabase('admin').delete_menu(select[1])
            if self.form_type == 'order':
                for select in selected:
                    ConnectDatabase('admin').delete_order(select[1])
            if self.form_type == 'employee':
                for select in selected:
                    ConnectDatabase('admin').delete_employee(select[1])
            if self.form_type == 'customer':
                for select in selected:
                    ConnectDatabase('admin').delete_customer(select[1])
            tkinter.messagebox.showinfo('delete', 'Successfully deleted!')

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

    @staticmethod
    def change():
        tkinter.messagebox.showinfo('change', "This function model is not developed!")

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
