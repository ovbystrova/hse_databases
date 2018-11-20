# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for
import pymysql as pm

USER = 'kesha'
PASSWORD = 'trustno1'
DB_NAME = 'fur_shop'

connection = pm.connect(user = USER,
                        password = PASSWORD,
                        db = DB_NAME,
                        charset = 'utf8mb4')
cursor = connection.cursor()

def insert_item(name, description, price):
    cursor.execute('INSERT INTO items (id, name, description, price) VALUES(null, "%s", "%s", "%d")' % (name, description, price))
    connection.commit()

def insert_customer(name, phone, email):
    cursor.execute('INSERT INTO customers (id, name, phone, email) VALUES(null, "%s", "%d", "%s")' % (name, phone, email))
    connection.commit()

def insert_purchase(item_id, customer_id, date):
    cursor.execute('INSERT INTO purchases (id, item_id, customer_id, date) VALUES(null, "%d", "%d", "%s")' % (item_id, customer_id, date))
    connection.commit()

def insert_complaint(text, item_id, purchase_id):
    cursor.execute('INSERT INTO complaints (id, text, item_id, purchase_id) VALUES(null, "%s", "%d", "%d")' % (text, item_id, purchase_id))
    connection.commit()

#Запрос на все предметы, стоимость которых больше чего-то.
def complex_cost(money):
    try:
        cursor.execute('SELECT * FROM items WHERE price > "%d"' %(money))
        res = cursor.fetchall()
    except:
        print('Nothing like that')
    connection.commit()
    return res

#Запрос на все отзывы по такому-то товару (по названию)
def complex_search(item_name):
    cursor.execute('SELECT * FROM items INNER JOIN complaints ON (items.name = "%s" and complaints.item_id = items.id)' % (item_name))
    res = cursor.fetchall()
    connection.commit()
    return res

#Просмотр БД (отдельной таблицы)
def show(request):
    if request =='items':
        cursor.execute('SELECT * FROM items')
    elif request =='customers':
        cursor.execute('SELECT * FROM customers')
    elif request =='purchases':
        cursor.execute('SELECT * FROM purchases')
    elif request =='complaints':
        cursor.execute('SELECT * FROM complaints')
    res = cursor.fetchall()
    connection.commit()
    return res

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.args:
        function = request.args['function']
        parametrs = request.args['parametrs']
        parametrs = parametrs.split(';')
        if function == 'insert_item':
            name = parametrs[0]
            description = parametrs[1]
            price = int(parametrs[2])
            insert_item(name, description, price)
        elif function =='insert_customer':
            name = parametrs[0]
            phone = int(parametrs[1])
            email = parametrs[2]
            insert_customer(name, phone, email)
        elif function =='insert_purchase':
            item_id = int(parametrs[0])
            customer_id = int(parametrs[1])
            date = parametrs[2]
            insert_purchase(item_id, customer_id, date)
        elif function =='insert_complaint':
            text = parametrs[0]
            item_id = int(parametrs[1])
            purchase_id = int(parametrs[2])
            insert_complaint(text, item_id, purchase_id)
        return redirect(url_for('index'))
    return render_template('insert.html')


@app.route('/search_join', methods=['GET', 'POST'])
def search_join():
    if request.args:
        item_name = request.args['item_name']
        res = complex_search(item_name)
        return render_template('response.html',res = res)
    return render_template('search_join.html')

@app.route('/filter_items', methods=['GET', 'POST'])
def filter_items():
    if request.args:
        money = request.args['money']
        res = complex_cost(int(money))
        return render_template('filter_items_response.html', res = res )
    return render_template('filter_items.html')

@app.route('/show', methods=['GET', 'POST'])
def show_bd():
    if request.args:
        req = request.args['req']
        res = show(req)
        return render_template('show_response.html', res=res)
    return render_template('show.html')

if __name__ == '__main__':
    app.run(debug=True)
