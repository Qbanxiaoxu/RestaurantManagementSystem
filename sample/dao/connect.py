# -*- coding: utf-8 -*-
# author：xxp time:2022/11/8
import docs.conf as configure
import pymysql.cursors

from sample.entity.Entity import Customer, Employee


class ConnectDatabase:
    __customer_number = 0
    __employee_number = 0
    __menu_number = 0
    __orders_number = 0
    __restaurant_number = 0
    __table_number = 0
    __restaurant_table_number = 0

    # __shopping_cart_number=0

    def __init__(self, user):
        if user == "customer":
            self.user = configure.mysql_database_user_customer
            self.password = configure.mysql_database_password_customer
        if user == "admin":
            self.user = configure.mysql_database_user_administrator
            self.password = configure.mysql_database_password_administrator
        if user == "employee":
            self.user = configure.mysql_database_user_employee
            self.password = configure.mysql_database_password_employee

    # Query operation

    def query_customer(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select * from customer"
                cursor.execute(sql)
                result = cursor.fetchall()
        return result

    def query_employee(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select * from employee"
                cursor.execute(sql)
                result = cursor.fetchall()
        return result

    def query_menu(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select * from menu"
                cursor.execute(sql)
                result = cursor.fetchall()
        return result

    def query_orders(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select * from orders"
                cursor.execute(sql)
                result = cursor.fetchall()
        return result

    def query_restaurant(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select * from restaurant"
                cursor.execute(sql)
                result = cursor.fetchall()
        return result

    def query_table(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select * from restaurant_table"
                cursor.execute(sql)
                result = cursor.fetchall()
        return result

    def query_shopping_cart(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select * from shopping_cart"
                cursor.execute(sql)
                result = cursor.fetchall()
        return result

    # Get number operation
    def get_customer_number(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select count(*) from customer"
                cursor.execute(sql)
                result = cursor.fetchone()["count(*)"]
                self.__customer_number = result
        return self.__customer_number

    def get_menu_number(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select count(*) from menu"
                cursor.execute(sql)
                result = cursor.fetchone()
                self.__menu_number = result["count(*)"]
        return self.__menu_number

    def get_employee_number(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select count(*) from employee"
                cursor.execute(sql)
                result = cursor.fetchone()
                self.__employee_number = result["count(*)"]
        return self.__employee_number

    def get_orders_number(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select count(*) from orders"
                cursor.execute(sql)
                result = cursor.fetchone()
                self.__orders_number = result["count(*)"]
        return self.__orders_number

    def get_restaurant_number(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select count(*) from restaurant"
                cursor.execute(sql)
                result = cursor.fetchone()
                self.__restaurant_number = result["count(*)"]
        return self.__restaurant_number

    def get_table_number(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection.cursor() as cursor:
            sql = "select count(*) from restaurant_table"
            cursor.execute(sql)
            result = cursor.fetchone()
            self.__table_number = result["count(*)"]
        return self.__table_number

    # def get_shopping_cart_number(self):
    #
    #     return self.__shopping_cart_number
    def get_dish_price(self, dish_id):
        menu = self.query_menu()
        for dish in menu:
            if dish['dish_id'] == dish_id:
                return dish['dish_price']
        return 0

    # Add operation

    def add_customer(self, customer):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO customer (customer_id, customer_name,customer_password,contact_info) " \
                      "VALUES (%s, %s, %s, %s)"
                values = (
                    customer.customer_id, customer.customer_name, customer.customer_password, customer.contact_info)
                cursor.execute(sql, values)
                connection.commit()

    def add_employee(self, employee):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO employee " \
                      "(employee_id, employee_name,gender,id_number,contact_info,position," \
                      "work_state,basic_salary,employee_password) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (
                    employee.employee_id, employee.employee_name, employee.gender,
                    employee.id_number, employee.contact_info, employee.position,
                    employee.work_state, employee.basic_salary, employee.employee_password)
                cursor.execute(sql, values)
                connection.commit()

    def add_menu(self, menu):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO menu " \
                      "(dish_id, dish_name, dish_price, dish_description) " \
                      "VALUES (%s, %s, %s, %s)"
                values = (menu.dish_id, menu.dish_name, menu.dish_price, menu.dish_description)
                cursor.execute(sql, values)
                connection.commit()

    def add_order(self, order):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO orders " \
                      "(order_id,customer_id, restaurant_id, employee_id, table_id, " \
                      "order_time, total_price, note, pay_state) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (order.order_id, order.customer_id, order.employee_id, order.restaurant_id,
                          order.table_id, order.order_time, order.total_price, order.note, order.pay_state)
                cursor.execute(sql, values)
                connection.commit()

    def add_restaurant(self, restaurant):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO restaurant (restaurant_id, restaurant_name, restaurant_address) " \
                      "VALUES (%s,%s,%s)"
                values = (restaurant.restaurant_id, restaurant.restaurant_name, restaurant.restaurant_address)
                cursor.execute(sql, values)
                connection.commit()

    def add_restaurant_table(self, restaurant_table):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO restaurant_table (table_id, table_state) " \
                      "VALUES (%s,%s)"
                values = (restaurant_table.teble_id, restaurant_table.table_state)
                cursor.execute(sql, values)
                connection.commit()

    def add_shopping_cart(self, shopping_cart):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO shopping_cart (dish_id, dish_num, dish_sum_price,restaurant_id) " \
                      "VALUES (%s,%s,%s,%s)"
                values = (shopping_cart.dish_id, shopping_cart.dish_num,
                          shopping_cart.dish_sum_price, shopping_cart.restaurant_id)
                cursor.execute(sql, values)
                connection.commit()

    # Delete operation

    def delete_customer(self, customer_id):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM customer WHERE customer_id=%s"
                value = customer_id
                cursor.execute(sql, value)
                connection.commit()

    def delete_employee(self, employee_id):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM employee WHERE employee_id=%s"
                value = employee_id
                cursor.execute(sql, value)
                connection.commit()

    def delete_menu(self, dish_id):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM menu WHERE dish_id=%s"
                value = dish_id
                cursor.execute(sql, value)
                connection.commit()

    def delete_order(self, order_id):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM orders WHERE order_id=%s"
                value = order_id
                cursor.execute(sql, value)
                connection.commit()

    def delete_restaurant(self, restaurant_id):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM restaurant WHERE restaurant_id=%s"
                value = restaurant_id
                cursor.execute(sql, value)
                connection.commit()

    def delete_restaurant_table(self, table_id):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM restaurant_table WHERE table_id=%s"
                value = table_id
                cursor.execute(sql, value)
                connection.commit()

    def delete_shopping_cart(self):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "TRUNCATE shopping_cart"
                cursor.execute(sql)
                connection.commit()

    # Modify operation

    def modify_customer(self, customer):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                if customer.customer_name:
                    sql = "UPDATE customer SET customer_name = %s WHERE customer_id = %s"
                    values = (customer.customer_name, customer.customer_id)
                    cursor.execute(sql, values)
                    connection.commit()
                if customer.customer_password:
                    sql = "UPDATE customer SET customer_password = %s WHERE customer_id = %s"
                    values = (customer.customer_password, customer.customer_id)
                    cursor.execute(sql, values)
                    connection.commit()
                if customer.contact_info:
                    sql = "UPDATE customer SET contact_info = %s WHERE customer_id = %s"
                    values = (customer.contact_info, customer.customer_id)
                    cursor.execute(sql, values)
                    connection.commit()

    def modify_employee(self, employee):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                if employee.employee_name:
                    sql = "UPDATE employee SET employee_name = %s WHERE employee_id = %s"
                    values = (employee.employee_name, employee.employee_id)
                    cursor.execute(sql, values)
                    connection.commit()
                if employee.employee_password:
                    sql = "UPDATE employee SET employee_password = %s WHERE employee_id = %s"
                    values = (employee.employee_password, employee.employee_id)
                    cursor.execute(sql, values)
                    connection.commit()
                if employee.contact_info:
                    sql = "UPDATE employee SET contact_info = %s WHERE employee_id = %s"
                    values = (employee.contact_info, employee.employee_id)
                    cursor.execute(sql, values)
                    connection.commit()
                if employee.gender:
                    sql = "UPDATE employee SET gender = %s WHERE employee_id = %s"
                    values = (employee.gender, employee.employee_id)
                    cursor.execute(sql, values)
                    connection.commit()
                if employee.position:
                    sql = "UPDATE employee SET position = %s WHERE employee_id = %s"
                    values = (employee.position, employee.employee_id)
                    cursor.execute(sql, values)
                    connection.commit()
                if employee.work_state:
                    sql = "UPDATE employee SET work_state = %s WHERE employee_id = %s"
                    values = (employee.work_state, employee.employee_id)
                    cursor.execute(sql, values)
                    connection.commit()
                if employee.basic_salary:
                    sql = "UPDATE employee SET basic_salary = %s WHERE employee_id = %s"
                    values = (employee.basic_salary, employee.employee_id)
                    cursor.execute(sql, values)
                    connection.commit()

    def modify_order(self, order):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                if order.note:
                    sql = "UPDATE orders SET note = %s WHERE order_id = %s"
                    values = (order.note, order.order_id)
                    cursor.execute(sql, values)
                    connection.commit()
                if order.pay_state:
                    sql = "UPDATE orders SET pay_state = %s WHERE order_id = %s"
                    values = (order.pay_state, order.order_id)
                    cursor.execute(sql, values)
                    connection.commit()

    def modify_menu(self, menu):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                if menu.dish_name:
                    sql = "UPDATE menu SET dish_name = %s WHERE dish_id = %s"
                    values = (menu.dish_name, menu.dish_id)
                    cursor.execute(sql, values)
                    connection.commit()
                if menu.dish_price:
                    sql = "UPDATE menu SET dish_price = %s WHERE dish_id = %s"
                    values = (menu.dish_price, menu.dish_id)
                    cursor.execute(sql, values)
                    connection.commit()
                if menu.dish_description:
                    sql = "UPDATE menu SET dish_description = %s WHERE dish_id = %s"
                    values = (menu.dish_description, menu.dish_id)
                    cursor.execute(sql, values)
                    connection.commit()

    def modify_restaurant(self, restaurant):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                if restaurant.restaurant_name:
                    sql = "UPDATE restaurant SET restaurant_name = %s WHERE restaurant_id = %s"
                    values = (restaurant.restaurant_name, restaurant.restaurant_id)
                    cursor.execute(sql, values)
                    connection.commit()
                if restaurant.restaurant_address:
                    sql = "UPDATE restaurant SET restaurant_address = %s WHERE restaurant_id = %s"
                    values = (restaurant.restaurant_address, restaurant.restaurant_id)
                    cursor.execute(sql, values)
                    connection.commit()

    def modify_restaurant_table(self, restaurant_table):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                if restaurant_table.table_state:
                    sql = "UPDATE restaurant_table SET table_state = %s WHERE table_id = %s"
                    values = (restaurant_table.table_state, restaurant_table.table_id)
                    cursor.execute(sql, values)
                    connection.commit()

    def verify(self, username, password):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            # 获取数据库中的用户信息，顾客、雇员
            customers_info = self.query_customer()
            employees_info = self.query_employee()
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
        return is_customer, is_employee

    def get_employee_position(self, username, password):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            employees_info = self.query_employee()
            for employee in employees_info:
                if username == employee["employee_name"] and password == employee["employee_password"]:
                    return employee["position"]
        return "mei zhao dao"

    def find_customer(self, name, password):
        customer = Customer(0, '', '', '')
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select * from customer where customer_name=%s and customer_password=%s"
                values = (name, password)
                cursor.execute(sql, values)
                result = cursor.fetchone()
        if result:
            customer.customer_id = result["customer_id"]
            customer.customer_name = result["customer_name"]
            customer.customer_password = result["customer_password"]
            customer.contact_info = result["contact_info"]
        return customer

    def find_employ(self, name, password, position):
        employee = Employee(0, '', '', '', '', '', '', '', 0.0)
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                sql = "select * from employee where employee_name=%s and employee_password=%s and position=%s"
                values = (name, password, position)
                cursor.execute(sql, values)
                result = cursor.fetchone()
        if result:
            employee.employee_id = result["employee_id"]
            employee.employee_name = result["employee_name"]
            employee.employee_password = result["employee_password"]
            employee.id_number = result["id_number"]
            employee.contact_info = result["contact_info"]
            employee.gender = result["gender"]
            employee.position = result["position"]
            employee.work_state = result["work_state"]
            employee.basic_salary = result["basic_salary"]
        return employee

    def check(self, check_id, form_type):
        connection = pymysql.connect(
            host=configure.mysql_database_host,
            user=self.user,
            password=self.password,
            database=configure.mysql_database_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset=configure.mysql_database_charset
        )
        with connection:
            with connection.cursor() as cursor:
                if form_type == 'restaurant_table':
                    sql = "select * from restaurant_table where table_id=%s"
                    value = check_id
                    cursor.execute(sql, value)
                    result = cursor.fetchone()
                if form_type == 'restaurant':
                    sql = "select * from restaurant where restaurant_id=%s"
                    value = check_id
                    cursor.execute(sql, value)
                    result = cursor.fetchone()
                if form_type == 'menu':
                    sql = "select * from menu where dish_id=%s"
                    value = check_id
                    cursor.execute(sql, value)
                    result = cursor.fetchone()
                if form_type == 'employee':
                    sql = "select * from employee where employee_id=%s"
                    value = check_id
                    cursor.execute(sql, value)
                    result = cursor.fetchone()
                if form_type == 'customer':
                    sql = "select * from customer where customer_id=%s"
                    value = check_id
                    cursor.execute(sql, value)
                    result = cursor.fetchone()
                if form_type == 'order':
                    sql = "select * from orders where order_id=%s"
                    value = check_id
                    cursor.execute(sql, value)
                    result = cursor.fetchone()
        return result
