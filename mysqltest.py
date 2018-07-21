import mysql.connector
import csv


def storedb(list_goods):
    list_id = 1
    db = mysql.connector.connect(
        host='localhost', user='root', password='123456', port=3306, database='spiders')
    cursor = db.cursor()
    # sql_createtable = 'create table goods (id varchar(20) primary key, name varchar(50), `desc` varchar(100), price varchar(20))'
    # cursor.execute(sql_createtable)
    sql_insert = 'insert into goods (id, name, `desc`, price) values (%s, %s, %s, %s)'
    for good in list_goods:
        in_good = good
        in_good.insert(0, str(list_id))
        list_id = list_id + 1
        cursor.execute(sql_insert, in_good)
        # cursor.rowcount()
        db.commit()

    # sql_delete = 'delete from goods'
    # cursor.execute(sql_delete)
    # db.commit()

    sql = 'select * from goods'
    cursor.execute(sql)
    values = cursor.fetchall()
    print(values)
    cursor.close()
    db.close()


def csv_read():
    list_goods = []
    with open('data2.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # print(row)
            list_goods.append(row)
    return list_goods


list_goods = []
list_goods = csv_read()
storedb(list_goods)
# print(list_goods)
