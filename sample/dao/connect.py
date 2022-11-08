# -*- coding: utf-8 -*-
# author：xxp time:2022/11/8
import docs.conf as configure
import pymysql.cursors


class ConnectDatabase:
    connection = pymysql.connect(
        host=configure.mysql_database_host,
        user=configure.mysql_database_user,
        password=configure.mysql_database_password,
        database=configure.mysql_database_name,
        cursorclass=pymysql.cursors.DictCursor,
        charset=configure.mysql_database_charset
    )
    __customer_number = 0
    __employee_number = 0
    __menu_number = 0
    __orders_number = 0
    __restaurant_number = 0
    __table_number = 0
    __restaurant_table_number = 0

    # __shopping_cart_number=0
    def __del__(self):
        self.connection.close()

    # Query operation
    def query_customer(self):
        with self.connection.cursor() as cursor:
            sql = "select * from customer"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def query_employee(self):
        with self.connection.cursor() as cursor:
            sql = "select * from employee"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def query_menu(self):
        with self.connection.cursor() as cursor:
            sql = "select * from menu"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def query_orders(self):
        with self.connection.cursor() as cursor:
            sql = "select * from orders"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def query_restaurant(self):
        with self.connection.cursor() as cursor:
            sql = "select * from restaurant"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def query_table(self):
        with self.connection.cursor() as cursor:
            sql = "select * from restaurant_table"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def query_shopping_cart(self):
        with self.connection.cursor() as cursor:
            sql = "select * from shopping_cart"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    # Get number operation
    def get_customer_number(self):
        with self.connection.cursor() as cursor:
            sql = "select count(*) from customer"
            cursor.execute(sql)
            result = cursor.fetchone()["count(*)"]
            self.__customer_number = result
        return self.__customer_number

    def get_menu_number(self):
        with self.connection.cursor() as cursor:
            sql = "select count(*) from menu"
            cursor.execute(sql)
            result = cursor.fetchone()
            self.__menu_number = result["count(*)"]
        return self.__menu_number

    def get_employee_number(self):
        with self.connection.cursor() as cursor:
            sql = "select count(*) from employee"
            cursor.execute(sql)
            result = cursor.fetchone()
            self.__employee_number = result["count(*)"]
        return self.__employee_number

    def get_orders_number(self):
        with self.connection.cursor() as cursor:
            sql = "select count(*) from orders"
            cursor.execute(sql)
            result = cursor.fetchone()
            self.__orders_number = result["count(*)"]
        return self.__orders_number

    def get_restaurant_number(self):
        with self.connection.cursor() as cursor:
            sql = "select * from restaurant"
            cursor.execute(sql)
            result = cursor.fetchone()
            self.__restaurant_table_number = result["count(*)"]
        return self.__restaurant_number

    def get_table_number(self):
        with self.connection.cursor() as cursor:
            sql = "select count(*) from restaurant_table"
            cursor.execute(sql)
            result = cursor.fetchone()
            self.__table_number = result["count(*)"]
        return self.__table_number

    # def get_shopping_cart_number(self):
    #
    #     return self.__shopping_cart_number

    # Add operation
    def add_customer(self, customer):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO customer (customer_id, customer_name,customer_password,contact_info) " \
                  "VALUES (%s, %s, %s, %s)"
            values = (
                customer.customer_id, customer.customer_name, customer.customer_password, customer.contact_info)
            cursor.execute(sql, values)
            self.connection.commit()

    def add_employee(self, employee):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO employee " \
                  "(employee_id, employee_name,gender,id_number,contact_info,position," \
                  "work_state,basic_salary,employee_password) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                employee.employee_id, employee.employee_name, employee.gender,
                employee.id_number, employee.contact_info, employee.position,
                employee.work_state, employee.basic_salary, employee.employee_password)
            cursor.execute(sql, values)
            self.connection.commit()

    def add_menu(self, menu):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO menu " \
                  "(dish_id, dish_name, dish_price, dish_description) " \
                  "VALUES (%s, %s, %s, %s)"
            values = (menu.dish_id, menu.dish_name, menu.dish_price, menu.dish_description)
            cursor.execute(sql, values)
            self.connection.commit()

    def add_order(self, order):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO orders " \
                  "(order_id,customer_id, restaurant_id, employee_id, table_id, " \
                  "order_time, total_price, note, pay_state) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (order.order_id, order.customer_id, order.employee_id, order.restaurant_id,
                      order.table_id, order.order_time, order.total_price, order.note, order.pay_state)
            cursor.execute(sql, values)
            self.connection.commit()

    def add_restaurant(self, restaurant):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO restaurant (restaurant_id, restaurant_name, restaurant_address) " \
                  "VALUES (%s,%s,%s)"
            values = (restaurant.restaurant_id, restaurant.restaurant_name, restaurant.restaurant_address)
            cursor.execute(sql, values)
            self.connection.commit()

    def add_restaurant_table(self, restaurant_table):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO restaurant_table (table_id, table_state) " \
                  "VALUES (%s,%s)"
            values = (restaurant_table.teble_id, restaurant_table.table_state)
            cursor.execute(sql, values)
            self.connection.commit()

    def add_shopping_cart(self, shopping_cart):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO shopping_cart (dish_id, dish_num, dish_sum_price) " \
                  "VALUES (%s,%s,%s)"
            values = (shopping_cart.dish_id, shopping_cart.dish_num, shopping_cart.dish_sum_price)
            cursor.execute(sql, values)
            self.connection.commit()

    # Delete operation
    def delete_customer(self, customer):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM customer WHERE customer_id=%s"
            value = customer.customer_id
            cursor.execute(sql, value)
            self.connection.commit()

    def delete_employee(self, employee):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM employee WHERE employee_id=%s"
            value = employee.employee_id
            cursor.execute(sql, value)
            self.connection.commit()

    def delete_menu(self, menu):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM menu WHERE dish_id=%s"
            value = menu.dish_id
            cursor.execute(sql, value)
            self.connection.commit()

    def delete_order(self, order):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM orders WHERE order_id=%s"
            value = order.order_id
            cursor.execute(sql, value)
            self.connection.commit()

    def delete_restaurant(self, restaurant):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM restaurant WHERE restaurant_id=%s"
            value = restaurant.restaurant_id
            cursor.execute(sql, value)
            self.connection.commit()

    def delete_restaurant_table(self, restaurant_table):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM restaurant_table WHERE table_id=%s"
            value = restaurant_table.teble_id
            cursor.execute(sql, value)
            self.connection.commit()

    # def delete_shopping_cart(self, shopping_cart):
    #     with self.connection.cursor() as cursor:
    #         sql = ""
    #         value = ()
    #         cursor.execute(sql, value)
    #     self.connection.commit()

    # Modify operation

    def modify_customer(self, customer):
        with self.connection.cursor() as cursor:
            if customer.customer_name:
                sql = "UPDATE customer SET customer_name = %s WHERE customer_id = %s"
                values = (customer.customer_name, customer.customer_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if customer.customer_password:
                sql = "UPDATE customer SET customer_password = %s WHERE customer_id = %s"
                values = (customer.customer_password, customer.customer_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if customer.contact_info:
                sql = "UPDATE customer SET contact_info = %s WHERE customer_id = %s"
                values = (customer.contact_info, customer.customer_id)
                cursor.execute(sql, values)
                self.connection.commit()

    def modify_employee(self, employee):
        with self.connection.cursor() as cursor:
            if employee.customer_name:
                sql = "UPDATE employee SET employee_name = %s WHERE employee_id = %s"
                values = (employee.employee_name, employee.employee_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if employee.employee_password:
                sql = "UPDATE employee SET employee_password = %s WHERE employee_id = %s"
                values = (employee.employee_password, employee.employee_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if employee.contact_info:
                sql = "UPDATE employee SET contact_info = %s WHERE employee_id = %s"
                values = (employee.contact_info, employee.employee_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if employee.gender:
                sql = "UPDATE employee SET gender = %s WHERE employee_id = %s"
                values = (employee.gender, employee.employee_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if employee.id_number:
                sql = "UPDATE employee SET id_number = %s WHERE employee_id = %s"
                values = (employee.id_number, employee.employee_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if employee.position:
                sql = "UPDATE employee SET position = %s WHERE employee_id = %s"
                values = (employee.position, employee.employee_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if employee.work_state:
                sql = "UPDATE employee SET work_state = %s WHERE employee_id = %s"
                values = (employee.work_state, employee.employee_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if employee.basic_salary:
                sql = "UPDATE employee SET basic_salary = %s WHERE employee_id = %s"
                values = (employee.basic_salary, employee.employee_id)
                cursor.execute(sql, values)
                self.connection.commit()

    def modify_order(self, order):
        with self.connection.cursor() as cursor:
            if order.note:
                sql = "UPDATE orders SET note = %s WHERE order_id = %s"
                values = (order.note, order.order_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if order.pay_state:
                sql = "UPDATE orders SET pay_state = %s WHERE order_id = %s"
                values = (order.pay_state, order.order_id)
                cursor.execute(sql, values)
                self.connection.commit()

    def modify_menu(self, menu):
        with self.connection.cursor() as cursor:
            if menu.dish_name:
                sql = "UPDATE menu SET dish_name = %s WHERE dish_id = %s"
                values = (menu.dish_name, menu.dish_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if menu.dish_price:
                sql = "UPDATE menu SET dish_price = %s WHERE dish_id = %s"
                values = (menu.dish_price, menu.dish_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if menu.dish_description:
                sql = "UPDATE menu SET dish_description = %s WHERE dish_id = %s"
                values = (menu.dish_description, menu.dish_id)
                cursor.execute(sql, values)
                self.connection.commit()

    def modify_restaurant(self, restaurant):
        with self.connection.cursor() as cursor:
            if restaurant.restaurant_name:
                sql = "UPDATE restaurant SET restaurant_name = %s WHERE restaurant_id = %s"
                values = (restaurant.restaurant_name, restaurant.restaurant_id)
                cursor.execute(sql, values)
                self.connection.commit()
            if restaurant.restaurant_address:
                sql = "UPDATE restaurant SET restaurant_address = %s WHERE restaurant_id = %s"
                values = (restaurant.restaurant_address, restaurant.restaurant_id)
                cursor.execute(sql, values)
                self.connection.commit()

    def modify_restaurant_table(self, restaurant_table):
        with self.connection.cursor() as cursor:
            if restaurant_table.table_state:
                sql = "UPDATE restaurant_table SET table_state = %s WHERE table_id = %s"
                values = (restaurant_table.table_state, restaurant_table.table_id)
                cursor.execute(sql, values)
                self.connection.commit()