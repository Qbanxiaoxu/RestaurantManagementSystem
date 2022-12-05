# -*- coding: utf-8 -*-
# author：xxp time:2022/11/9
import tkinter
from tkinter import messagebox
from sample.dao.connect import ConnectDatabase
from sample.entity.Entity import Menu
from sample.gui.listview import ListViewUI


class ChefForm:
    def __init__(self, frame):
        self.frame = frame
        self.destroy_frame()
        self.check_id = None
        self.listview = ListViewUI(self.frame)

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

        btn_modify = tkinter.Button(self.frame, text="add", command=self.add)
        btn_modify.place(x=100, y=480, width=100, height=50)

        btn_delete = tkinter.Button(self.frame, text="delete", command=self.delete)
        btn_delete.place(x=250, y=480, width=100, height=50)

        btn_modify = tkinter.Button(self.frame, text="check", command=self.check)
        btn_modify.place(x=400, y=480, width=100, height=50)

        btn_delete = tkinter.Button(self.frame, text="change", command=self.change)
        btn_delete.place(x=550, y=480, width=100, height=50)

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

    def add(self):
        self.destroy_frame()

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

    def commit_add(self):
        dish_name = self.dish_name
        dish_price = self.dish_price
        dish_description = self.dish_description
        dish = Menu(dish_id=None, dish_name=dish_name, dish_price=dish_price, dish_description=dish_description)
        ConnectDatabase('admin').add_menu(dish)
        tkinter.messagebox.showinfo('add', "Dish added successfully!")

    def delete(self):
        selected, selected_info = self.get_selected()
        is_delete = tkinter.messagebox.askyesno('Confirm delete?',
                                                selected_info)
        if is_delete:
            for select in selected:
                ConnectDatabase('admin').delete_menu(select[1])
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
        restaurant = ConnectDatabase('admin').check(check_id=check_id, form_type='menu')
        tkinter.messagebox.showinfo('check', str(restaurant))

    @staticmethod
    def change():
        tkinter.messagebox.showinfo('change', "This function model is not developed!")
