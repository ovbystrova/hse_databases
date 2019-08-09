from flask import Flask, request, render_template, redirect, url_for
import pymysql as pm
import argparse


class DataBase:
    """База данный с разметкой видеозаписей с TED конференций"""

    def __init__(self, user, password, name):
        self.user = user
        self.password = password
        self.name = name
        self.connection = pm.connect(user=self.user,
                                     password=self.password,
                                     db=self.name,
                                     charset='utf8mb4')
        self.cursor = self.connection.cursor()

    def __del__(self):
        # Тут нужно будет разорвать соединение с БД, закрыть Фласк.
        pass

    def insert_meta(self, id_video, name, date_of_recording,
                    location, author, lang):
        self.cursor.execute(
            'INSERT INTO meta (id_video, name, date_of_recording,'
            ' location, author, lang)'
            ' VALUES("%d", "%s", "%s", "%s", "%s", "%s")'
            % (id_video, name, date_of_recording, location, author, lang))
        self.connection.commit()

    def insert_zhest(self, id_video, time, zhesticulation):
        self.cursor.execute('INSERT INTO zhest '
                            '(id_video, time, zhesticulation)'
                            ' VALUES("%d", "%d", "%s")' %
                            (id_video, time, zhesticulation))
        self.connection.commit()

    def insert_mimic(self, id_video, time, text):
        self.cursor.execute('INSERT INTO mimic '
                            '(id_video, time, text) VALUES'
                            '("%d", "%d", "%s")' %
                            (id_video, time, text))
        self.connection.commit()

    def insert_text(self, id_video, time, text):
        self.cursor.execute('INSERT INTO text ('
                            'id_video, time, text) '
                            'VALUES("%d", "%d", "%s")' %
                            (id_video, time, text))
        self.connection.commit()

    def complex_text(self, id_video, time):
        """Запрос на текст после такой-то секунды видео (id_video, time)"""
        try:
            self.cursor.execute('SELECT * FROM text '
                                'WHERE id_video = "%d" '
                                'AND time > "%d"' %
                                (id_video, time))
            res = self.cursor.fetchall()
        except:
            print('Nothing like that')
        self.connection.commit()
        return res

    def complex_search(self, author):
        """Запрос на всю мимику по автору видео"""
        self.cursor.execute(
            'SELECT * FROM meta INNER JOIN mimic ON '
            '(meta.author = "%s" and mimic.id_video = meta.id_video)'
            % (author))
        res = self.cursor.fetchall()
        self.connection.commit()
        return res

    def show(self, request):
        """Просмотр БД (отбельной таблицы)"""
        if request == 'meta':
            self.cursor.execute('SELECT * FROM meta')
        elif request == 'zhest':
            self.cursor.execute('SELECT * FROM zhest')
        elif request == 'mimic':
            self.cursor.execute('SELECT * FROM mimic')
        elif request == 'text':
            self.cursor.execute('SELECT * FROM text')
        res = self.cursor.fetchall()
        self.connection.commit()
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
            DB.insert_meta(id_video, name, date_of_recording,
                           location, author, lang)
        elif function == 'insert_zhest':
            id_video = int(parametrs[0])
            time = int(parametrs[1])
            zhest = parametrs[2]
            DB.insert_zhest(id_video, time, zhest)
        elif function == 'insert_mimic':
            id_video = int(parametrs[0])
            time = int(parametrs[1])
            text = parametrs[2]
            DB.insert_mimic(id_video, time, text)
        elif function == 'insert_text':
            id_video = int(parametrs[0])
            time = int(parametrs[1])
            text = parametrs[2]
            DB.insert_text(id_video, time, text)
        return redirect(url_for('index'))
    return render_template('insert.html')


@app.route('/search_join', methods=['GET', 'POST'])
def search_join():
    if request.args:
        author = request.args['author']
        res = DB.complex_search(author)
        return render_template('response.html', res=res)
    return render_template('search_join.html')


@app.route('/filter_items', methods=['GET', 'POST'])
def filter_items():
    if request.args:
        id_video = request.args['id_video']
        money = request.args['money']
        res = DB.complex_text(int(id_video), int(money))
        return render_template('filter_items_response.html', res=res)
    return render_template('filter_items.html')


@app.route('/show', methods=['GET', 'POST'])
def show_bd():
    if request.args:
        req = request.args['req']
        res = DB.show(req)
        if req == 'meta':
            return render_template('show_response_meta.html', res=res)
        else:
            return render_template('show_response.html', res=res)
    return render_template('show.html')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='You should write USERNAME, PASSWORD, NAME')
    parser.add_argument(type=str, help='USERNAME', dest='USER')
    parser.add_argument(type=str, help='PASSWORD', dest="PASSWORD")
    parser.add_argument(type=str, help='NAME', dest="NAME")
    args = parser.parse_args()
    USER = args.USER
    PASSWORD = args.PASSWORD
    NAME = args.NAME

    DB = DataBase(USER, PASSWORD, NAME)
    app.run(debug=True)
