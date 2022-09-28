from Data import *
from WordBook import *
from flask import *
app = Flask(__name__)

msg = ''
review = ''
wb = WorkBook()
todo = ""
word = ''
v = None

@app.route('/')
def index():
    global msg
    __msg__ = msg if msg else "请选择操作"
    msg = ""
    return render_template("index.html", msg=__msg__)

@app.route('/index/judge',methods = ['POST'])
def indexJudge():
    choose = request.form["choose"]
    if choose == 'addition'     : return redirect(url_for('addition'))
    if choose == 'delete'       : return redirect(url_for('delete'))
    if choose == 'update'       : return redirect(url_for('update'))
    if choose == 'select'       : return redirect(url_for('select'))
    else :
        global todo
        todo = choose
        return redirect(url_for('review'))


@app.route('/addition')
def addition():
    global todo
    todo = 'addition'

    return render_template(
        "addition.html",
        msg = "ADDITION"
    )

@app.route('/addition/fun', methods=['post'])
def additionFun():
    try:
        if choose := request.form['choose']:
            global msg
            __msg__ = msg if msg else "请选择操作"
            msg = ""
            return redirect(url_for('index'))
    except:
        pass
    word = request.form['word']
    if not word :
        return render_template("addition.html", msg="请输入单词")
    if v := wb.selectVocabulary(word) :
        return __show__(v, " %s 已存在"%(word))
        
    else :
        v = Vocabulary(
            word=request.form['word'],
            paraphrase=request.form['paraphrase'],
            roots=request.form['roots'],
            dates=getNowTime(),
            counts=5
        )
        wb.additionVocabulary(v)
        return __show__(v, "添加成功")

@app.route('/update')
def update():
    global msg, word
    todo = 'addition'
    __msg__ = msg if msg else "ADDITION"
    msg = ""
    return render_template(
        "update.html",
        word= word,
        msg = __msg__
    )

@app.route('/update/fun', methods=['post'])
def updateFun():
    try:
        if choose := request.form['choose']:
            global msg
            __msg__ = msg if msg else "请选择操作"
            msg = ""
            return render_template("index.html", msg=__msg__)
    except:
        pass
    global word
    __word__ = word
    word = ""
    # print(word, type(word))
    
    v = Vocabulary(
        word=__word__,
        paraphrase=request.form['paraphrase'],
        roots=request.form['roots']
    )
    wb.updateVocabulary(v)
    return __show__(v, "已更新")


def __show__(v : Vocabulary, msg:str):
    return render_template(
           "show.html",
            msg=            msg,
            word=           v.getWord(),
            roots=          v.getRoots(),
            paraphrase=     v.getParaphrase(),
            before=         int(getNowTime() - v.getDates()),
            counts=         v.getCounts()
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

@app.route('/show/fun', methods=['post'])
def showFun():
    global todo
    choose = request.form['choose']
    if 'continue' == choose :
        if "select" == todo: 
            return select()
        if "addition" == todo: 
            return addition()
    
    global word
    __word__ = word
    if 'delete' == choose:
        word = ""
        msg = "delete " + ("succeed" if wb.deleteVocabulary(__word__) else "error" )
        return render_template(
            "tips.html",
            word=__word__,
            msg=msg
        )
    if 'update' == choose:
        return render_template(
            "update.html",
            msg= "Update " + __word__.title(),
            word=  word
        )
    return index()

@app.route('/select')
def select():
    global todo
    todo = 'select'
    
    return render_template(
        "select.html",
        msg="SELECT"
    )

@app.route('/select/fun', methods=['post'])
def selectFun():
    try:
        if choose := request.form['choose']:
            return redirect(url_for('index'))
    except:
        pass
    global msg, word
    word = request.form['word']
    # print(word, type(word))
    if v := wb.selectVocabulary(word) :
        return __show__(v, "VOCABULARY")
    else :
        msg = "%s NOT FIND"%word
        return select()


def __review__() :
    return render_template(
           "review.html",
            word=           v.getWord(),
            roots=          v.getRoots(),
            paraphrase=     v.getParaphrase(),
            before=         int(getNowTime() - v.getDates()),
            counts=         v.getCounts()
        )

@app.route('/review')
def review():
    global msg, todo, v
    print(todo)
    if "reviewDates" == todo :
        v = wb.reviewByDate()
    if "reviewCounts" == todo:
        v = wb.reviewByCounts()
    if "reviewUse" == todo:
        v = wb.reviewByUse()
    
    if not v : 
        msg="所有单词已经被复习"
        return redirect(url_for('index'))

    
    return __review__()


@app.route('/review/fun', methods=['post'])
def reviewFun():
    choose = request.form['choose']
    
    global v
    if v and 'true' == choose and 'reviewCounts' == todo:
        v.setCounts(-1)
        wb.updateVocabulary(v)
        return redirect(url_for('review'))
    if v and 'false' == choose :
        wb.updateVocabulary(v)
        return redirect(url_for('review'))

    v = None
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=1432)
    # app.run(debug=True,host='127.0.0.1',port=1423)
    # app.run(debug=True,host='0.0.0.0',port=1423)
