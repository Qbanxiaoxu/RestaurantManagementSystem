# -*- coding: utf-8 -*-
# author：xxp time:2022/11/5
from dataclasses import dataclass


@dataclass()
class Customer:
    customer_id: int
    customer_name: str
    customer_password: str
    contact_info: str


@dataclass()
class Employee:
    employee_id: int
    employee_name: str
    employee_password: str
    gender: str
    id_number: str
    contact_info: str
    position: str
    work_state: str
    basic_salary: float


@dataclass()
class Menu:
    dish_id: int
    dish_name: str
    dish_price: float
    dish_description: str


@dataclass()
class Order:
    order_id: int
    customer_id: int
    restaurant_id: int
    employee_id: int
    table_id: int
    order_time: str
    total_price: float
    note: str
    pay_state: str


@dataclass()
class Restaurant:
    restaurant_id: int
    restaurant_name: str
    restaurant_address: str


@dataclass()
class RestaurantTable:
    table_id: int
    table_state: str


@dataclass()
class ShoppingCart:
    shopping_cart_id: int = 0
    dish_id: int = 0
    dish_num: int = 0
    dish_sum_price: float = 0

