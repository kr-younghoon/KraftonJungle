from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)


app = Flask(__name__)

client = MongoClient(
    'mongodb+srv://test:sparta@cluster0.ecijcpt.mongodb.net/?retryWrites=true&w=majority')
db = client.dbtest

@app.route('/')
def base():
    return render_template("rogin.html")


@app.route('/rogin',methods=["GET","POST"])
def rogin():
    
    return render_template("rogin.html")


@app.route('/register',methods=["GET","POST"])
def register():
    
    return render_template("register.html")



# CREATE Part - YOUNGHOON
# submit 기능과 countNUM 기능(일단 살려뒀습니다.)이 있습니다.
# 혹시 몰라 주석해놓고 지켜보려고 합니다.

#def index(): 였지만 중복될까 하여 submitQ로 수정합니다.

@app.route("/create", methods=["POST","GET"])
def submitQ():    
    quiz_list = list(db.quiz.find({}, {'_id': False}))
    len_num = len(quiz_list)
    new_num = len_num + 1
    
    print(f"num: {new_num}")
    
    if request.method == "POST":
        quiz = request.form["quiz"]
        answer = request.form["answer"]
        quiz_category = request.form["quiz_category"]

        doc = {
            'quiz': quiz,
            'answer': answer,
            'quiz_category': quiz_category,
            'NUM': new_num
        }
        db.quiz.insert_one(doc)
        return render_template("main.html", new_num = new_num)
    
    
    # elif request.method == "GET":
    #     quiz_list = list(db.quiz.find({}, {'_id': False}))
    #     len_num = len(quiz_list)
    #     new_num = len_num + 1
    
    #     return render_template("main.html")
        
    
    else:
        new_num = new_num + 1
        return render_template("main.html",new_num = new_num)
    
    
# @app.route("/create", methods=["GET"])
# def make_num():     
#     if request.method == "GET":
#         quiz_list = list(db.quiz.find({}, {'_id': False}))
#         len_num = len(quiz_list)
#         new_num = len_num + 1
    
#         return render_template("main.html", new_num = new_num)
    
#     else:
#         return render_template("main.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)