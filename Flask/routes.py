from Data import *
from WordBook import *
from flask import *

app = Flask(__name__)


@app.route('/addition')
def addition():
    return render_template(
        "addition.html"
    )
@app.route('/addition/fun', methods=['post'])
def additionFun():
    v = Vocabulary(
        word=request.form['word'],
        paraphrase=request.form['paraphrase'],
        roots=request.form['roots']
    )
@app.route('/tips')
def tips():
    return render_template(
        "tips.html",
        word="beautiful"
    )

@app.route('/show')
def show():
    return render_template(
        "show.html",
        word=           "beautiful",
        roots=          "beauty",
        paraphrase=     "adj.美丽的，漂亮的；",
        before=         int(time.time() // (86400)) - 19245,
        counts=         5
    )

@app.route('/delete')
def delete():
    return "delete"

@app.route('/update')
def update():
    return "update"

@app.route('/select')
def select():
    return render_template(
        "select.html"
    )

@app.route('/review/dates')
def reviewDates():
    return "reviewDates"

@app.route('/review/counts')
def reviewCounts():
    return "reviewCounts"

import time

@app.route('/review/use')
def reviewUse():

    return render_template(
        'review.html',
        word=           "beautiful",
        roots=          "beauty",
        paraphrase=     "adj.美丽的，漂亮的；",
        before=         int(time.time() // (86400)) - 19245,
        counts=         5
    )


