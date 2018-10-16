import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.executescript("""
                CREATE TABLE IF NOT EXISTS subjects(
                   sub_id integer PRIMARY KEY AUTOINCREMENT not null,
                   subj_name text not null
                   );
                   
                CREATE TABLE IF NOT EXISTS students(
                   st_id integer PRIMARY KEY AUTOINCREMENT not null,
                   fio text not null,
                   group1 text not null
                   );
                   
                CREATE TABLE IF NOT EXISTS control_w(
                   cw_id integer PRIMARY KEY AUTOINCREMENT not null,
                   subj int not null,
                   mark integer not null,
                   student integer not null,
                    FOREIGN KEY(subj) REFERENCES subjects(sub_id),
                    FOREIGN KEY(student) REFERENCES students(st_id)
                   );

                CREATE TABLE IF NOT EXISTS questions(
                   q_id integer PRIMARY KEY AUTOINCREMENT not null,
                   task text not null,
                   con_w integer not null,
                   FOREIGN KEY(con_w) REFERENCES control_w(cw_id)
                   );
                   """)
conn.commit()


def add_subject(subj_name):
    cursor.execute("INSERT INTO subjects (subj_name) VALUES ('%s')" %subj_name)
    conn.commit()
    return 'Perfection'


def add_student(fio, group1):
    cursor.execute("INSERT INTO students (fio, group1) VALUES ('%s', '%s')" %(fio, group1))
    conn.commit()
    return 'Perfection'


def add_control_w(subj, mark, student):
    cursor.execute("INSERT INTO control_w (subj, mark, student) VALUES ('%s', '%s', '%s')" % (subj, mark, student))
    conn.commit()
    return 'Perfection'


def add_questions(task, con_w):
    cursor.execute("INSERT INTO questions (task, con_w) VALUES ('%s', '%s')" % (task, con_w))
    conn.commit()
    return 'Perfection'


def delete_subj(subj_name):
    cursor.execute("DELETE FROM subjects WHERE subj_name='%s'" %subj_name)
    conn.commit()


def delete_student(st_id):
    cursor.execute("DELETE FROM students WHERE st_id='%s'" % st_id)
    conn.commit()


def delete_control_w(cw_id):
    cursor.execute("DELETE FROM control_w WHERE cw_id='%s'" % cw_id)
    conn.commit()


def delete_questions(q_id):
    cursor.execute("DELETE FROM questions WHERE q_id='%s'" % q_id)
    conn.commit()


def search_subjects(subj_name):
    cursor.execute("SELECT * FROM subjects WHERE subj_name = '%s'" % subj_name)
    result = cursor.fetchall()
    conn.commit()
    return result


def search_student(fio):
    cursor.execute("SELECT * FROM students WHERE fio = '%s'" % fio)
    result = cursor.fetchall()
    conn.commit()
    return result


def search_control_w(cw_id):
    cursor.execute("SELECT * FROM cotrol_w WHERE cw_id = '%s'" % cw_id)
    result = cursor.fetchall()
    conn.commit()
    return result


def search_questions(q_id):
    cursor.execute("SELECT * FROM questions WHERE q_id = '%s'" % q_id)
    result = cursor.fetchall()
    conn.commit()
    return result


def update_subjects(subj_name, sub_id):
    cursor.execute("UPDATE subjects SET subj_name='%s' WHERE sub_id='%s'" % (subj_name, sub_id))
    conn.commit()
    return


def update_student(fio, st_id):
    cursor.execute("UPDATE students SET fio='%s' WHERE st_id='%s'" % (fio, st_id))
    conn.commit()
    return


def update_questions(task, q_id):
    cursor.execute("UPDATE subjects SET task='%s' WHERE q_id='%s'" % (task, q_id))
    conn.commit()
    return


def update_control_w(mark, cw_id, student):
    cursor.execute("UPDATE control_w SET mark='%s' WHERE cw_id='%s' and student='%s'" % (mark, cw_id, student))
    conn.commit()
    return
