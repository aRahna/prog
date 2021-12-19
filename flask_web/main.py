from flask import Flask, render_template, request
from models import User, Answers, db

import sqlite3


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///results.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)


# in python console: from main import app
# then:db.create_all()
@app.route("/")  # главная страница
def main():
    return render_template("main.html")


@app.route('/ank', methods=["POST", "GET"])  # анкета
def ank():
    if request.method == "POST":
        u = User(
            age=request.form['age'],
            sex=request.form['sex'],
            dalt=request.form['dalt']
        )
        db.session.add(u)
        db.session.flush()

        a = Answers(
            q1=request.form['q1'],
            q2=request.form['q2'],
            q3=request.form['q3'],
            q4=request.form['q4'],
            q5=request.form['q5'],
            q6=request.form['q6'],
            q7=request.form['q7'],
            q8=request.form['q8'],
            q9=request.form['q9'],
            q10=request.form['q10'],
            q11=request.form['q11'],
            q12=request.form['q12'],
            q13=request.form['q13'],
            q14=request.form['q14'],
            q15=request.form['q15'],
            user_id=u.id
        )
        db.session.add(a)
        db.session.commit()

        return render_template("ank1.html")

    else:
        return render_template("ank.html")


@app.route('/ank1')  # анкета завершена
def ank1():
    return render_template("ank1.html")


@app.route('/res')  # результаты
def res():
    con = sqlite3.connect('results.db')  # подключение
    cur = con.cursor()

    cur.execute("""SELECT COUNT(id) as n FROM user""")
    quon = list(cur.fetchone())[0]

    cur.execute("""
    SELECT COUNT(id) as n FROM answers
    WHERE q6 == 2
    """)
    gray = list(cur.fetchone())[0]
    print(quon)
    return render_template("res.html", a=quon, b=gray)


@app.route('/check')  # ответы
def check():
    return render_template("check.html")


if __name__ == "__main__":
    app.run(debug=True)
