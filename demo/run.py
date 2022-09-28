from Data import *
from WordBook import *
from flask import *
app = Flask(__name__)

# 传递的消息
msg = ""
# 操作对象
wb = WorkBook()
# 跳转对象
jump = ""
