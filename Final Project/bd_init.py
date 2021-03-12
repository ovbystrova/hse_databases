# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for
import pymysql as pm

USER = 'root'
PASSWORD = 'toor'
DB_NAME = 'videos'

connection = pm.connect(user=USER,
                        password=PASSWORD,
                        db=DB_NAME,
                        charset='utf8mb4')
cursor = connection.cursor()


def insert_meta(id_video, name, date_of_recording, location, author, lang):
    """
    Insert line to meta table
    :param id_video: int
    :param name: str
    :param date_of_recording: str
    :param location: str
    :param author: str
    :param lang: str
    :return:
    """
    cursor.execute(
        'INSERT INTO meta (id_video, name, date_of_recording, location, author, lang) VALUES("%d", "%s", "%s", "%s", '
        '"%s", "%s") '
        % (id_video, name, date_of_recording, location, author, lang))
    connection.commit()


def insert_zhest(id_video, time, zhesticulation):
    """
    Insert line into zhest table
    :param id_video: int
    :param time: int
    :param zhesticulation: str
    :return:
    """
    cursor.execute('INSERT INTO zhest (id_video, time, zhesticulation) VALUES("%d", "%d", "%s")' % (
        id_video, time, zhesticulation))
    connection.commit()


def insert_mimic(id_video, time, text):
    """
    Insert line into mimic table
    :param id_video: int
    :param time: ind
    :param text: str
    :return:
    """
    cursor.execute('INSERT INTO mimic (id_video, time, text) VALUES("%d", "%d", "%s")' % (id_video, time, text))
    connection.commit()


def insert_text(id_video, time, text):
    """
    Insert line into text table
    :param id_video: int
    :param time: int
    :param text: str
    :return:
    """
    cursor.execute('INSERT INTO text (id_video, time, text) VALUES("%d", "%d", "%s")' % (id_video, time, text))
    connection.commit()


# Запрос на весь текст после такой-то секунды видео  (нужно id_video, time).
def complex_text(id_video, time):
    """
    Shows text from the specific video after specific time
    :param id_video: int
    :param time: int
    :return:
    """
    try:
        cursor.execute('SELECT * FROM text WHERE id_video = "%d" AND time > "%d"' % (id_video, time))
        res = cursor.fetchall()
    except:
        print('Nothing like that')
    connection.commit()
    return res


# Запрос на всю мимику по автору видео
def complex_search(author):
    """
    Shows all mimic by author
    :param author: str
    :return:
    """
    cursor.execute(
        'SELECT * FROM meta INNER JOIN mimic ON (meta.author = "%s" and mimic.id_video = meta.id_video)' % (author))
    res = cursor.fetchall()
    connection.commit()
    return res


def _inner_select(location):
    cursor.execute(
        'SELECT name, date_of_recording FROM (SELECT * FROM meta ) as T LEFT OUTER JOIN mimic ON T.id_video WHERE T.author="%s"' % (location)
    )
    res = cursor.fetchall()
    connection.commit()
    return res

# def select_from_three_tables():
#     cursor.execute(
#         ''
#     )
#     res = cursor.fetchall()
#     connection.commit()

# Просмотр БД (отдельной таблицы)
def show(request):
    """
    Show one of existed tables
    :param request: str
    :return:
    """
    if request == 'meta':
        cursor.execute('SELECT * FROM meta')
    elif request == 'zhest':
        cursor.execute('SELECT * FROM zhest')
    elif request == 'mimic':
        cursor.execute('SELECT * FROM mimic')
    elif request == 'text':
        cursor.execute('SELECT * FROM text')
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
        if function == 'insert_meta':
            id_video = int(parametrs[0])
            name = parametrs[1]
            date_of_recording = parametrs[2]
            location = parametrs[3]
            author = parametrs[4]
            lang = parametrs[5]
            insert_meta(id_video, name, date_of_recording, location, author, lang)
        elif function == 'insert_zhest':
            id_video = int(parametrs[0])
            time = int(parametrs[1])
            zhest = parametrs[2]
            insert_zhest(id_video, time, zhest)
        elif function == 'insert_mimic':
            id_video = int(parametrs[0])
            time = int(parametrs[1])
            text = parametrs[2]
            insert_mimic(id_video, time, text)
        elif function == 'insert_text':
            id_video = int(parametrs[0])
            time = int(parametrs[1])
            text = parametrs[2]
            insert_text(id_video, time, text)
        return redirect(url_for('index'))
    return render_template('insert.html')


@app.route('/search_join', methods=['GET', 'POST'])
def search_join():
    if request.args:
        author = request.args['author']
        res = complex_search(author)
        return render_template('response.html', res=res)
    return render_template('search_join.html')


@app.route('/filter_items', methods=['GET', 'POST'])
def filter_items():
    if request.args:
        id_video = request.args['id_video']
        money = request.args['money']
        res = complex_text(int(id_video), int(money))
        return render_template('filter_items_response.html', res=res)
    return render_template('filter_items.html')


@app.route('/inner_select', methods=['GET', 'POST'])
def inner_select():
    if request.args:
        author = request.args['author']
        print(author)
        res = _inner_select(author)
        return render_template('inner_select_response.html', res=res)
    return render_template('inner_select.html')


@app.route('/show', methods=['GET', 'POST'])
def show_bd():
    if request.args:
        req = request.args['req']
        res = show(req)
        if req == 'meta':
            return render_template('show_response_meta.html', res=res)
        else:
            return render_template('show_response.html', res=res)
    return render_template('show.html')


if __name__ == '__main__':
    app.run(debug=True)
