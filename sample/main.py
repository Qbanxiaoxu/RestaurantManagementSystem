# -*- coding: utf-8 -*-
# author：xxp time:2022/11/5
import sample.entity.Entity as Entity
import sample.dao.connect as connection

if __name__ == '__main__':
    db=connection.ConnectDatabase()
    print(type(db.query_customer()[0]))
