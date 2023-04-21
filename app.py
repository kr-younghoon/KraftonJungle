from flask import Flask, render_template, request, flash, session, redirect, url_for
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
import jwt
import datetime
from random import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwda;asodihjf#@@ef2312"
secret_key = "qwda;asodihjf#@@ef2312"
token_algorithm = "HS256"

client = MongoClient('mongodb+srv://test:sparta@cluster0.ecijcpt.mongodb.net/?retryWrites=true&w=majority')
db = client.dbtest
#client = MongoClient("mongodb+srv://test:1234@cluster0.i0ovzkc.mongodb.net/?retryWrites=true&w=majority")
#db = client.dbtest
# 토큰 생성


def create_token(nickname):
    payload = {
        'nickname': nickname,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 24)
    }
    token = jwt.encode(payload, secret_key, token_algorithm)
    return token

# 토큰 검증


def validate_token(get_token):
    try:
        jwt.decode(get_token, secret_key, token_algorithm)
    except jwt.ExpiredSignatureError:  # 토큰 인증만료시 리턴
        return
    except jwt.InvalidTokenError:  # 토른 검증 실패시 리턴
        return

# 문자열 비교
def checking(str1, str2):
    if str1 == str2:
        return True
    else:
        return False

# 빈곳 확인
def voidchecking(str1):
    if str1 == "":
        return True
    else:
        return False


client = MongoClient(
    'mongodb+srv://test:sparta@cluster0.ecijcpt.mongodb.net/?retryWrites=true&w=majority')
db = client.dbtest


@app.route('/')
def base():
    if "nickname" in session:
        return redirect(url_for("logout"))
    else:
        #return redirect(url_for("main"))
        #return render_template("create.html")
        return render_template("login.html")
        #return render_template("register.html")
        


@app.route('/login', methods=["GET"])
def login():
    if "nickname" in session:
        return redirect(url_for("logout"))
    
    if request.method == 'GET':
        if voidchecking(request.args.get('user_id')) or voidchecking(request.args.get('user_password')):
            flash("빈공간이 존재합니다.")
            return render_template("login.html")
        user_db_list = list(db.User.find({}, {'_id': False}))
        for i in range(0, len(user_db_list)):
            user_db_single = user_db_list[i]
            if checking(user_db_single['id'], request.args.get('user_id')):
                if checking(user_db_single['pw'], request.args.get('user_password')):
                    flash("로그인 성공")
                    # jwt 토큰?
                    #access_token = create_token(user_db_single['nickname'])
                    #print(access_token)
                    # 섹션 사용
                    session["nickname"] = user_db_single['nickname']
                    return redirect(url_for("main"))
                    #return render_template("main.html", nickname=session.get("nickname"))
                else:
                    flash("비밀번호가 아닙니다.")
                    return render_template("login.html")
        flash("아이디가 없습니다.")

    return render_template("login.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if "nickname" in session:
        return redirect(url_for("logout"))
    
    if request.method == 'POST':
        if voidchecking(request.form['user_id']) or voidchecking(request.form['user_password']) or voidchecking(request.form['user_checkpassword']) or voidchecking(request.form['user_nickname']):
            flash("빈공간이 존재합니다.")
            return render_template("register.html")
        user_db_list = list(db.User.find({}, {'_id': False}))
        for i in range(0, len(user_db_list)):

            user_db_single = user_db_list[i]

            if checking(user_db_single['id'], request.form['user_id']):
                flash("중복된 아이디가 존재합니다.")
                return render_template("register.html")

            if checking(user_db_single['nickname'], request.form['user_nickname']):
                flash("중복된 닉네임이 존재합니다.")
                return render_template("register.html")

        if checking(request.form['user_password'], request.form['user_checkpassword']):
            user_info = {'id': request.form['user_id'],
                         'pw': request.form['user_password'],
                         'nickname': request.form['user_nickname'],
                         'record' : 0,
                         'count' : 0
                         }
            db.User.insert_one(user_info)
            flash("아이디가 생성 되었습니다.")
            return redirect(url_for("login"))
            # return render_template("login.html")
        else:
            flash("비밀번호가 다릅니다.")
            return render_template("register.html")

    return render_template("register.html")


@app.route('/logout', methods=["GET"])
def logout():
    if "nickname" in session:
        flash("로그아웃 되었습니다.")
        session.pop("nickname")
        return redirect(url_for("login"))
    
    flash("로그인 페이지로 이동되었습니다.")
    return redirect(url_for("login"))

@app.route('/main', methods=["GET"])
def main():
    player = db.User.find_one({"nickname": session.get("nickname")})
    if player['count']>0:
        if player["record"] < player['count']:
            db.User.update_one({'nickname': session.get("nickname")}, {'$set': {'record': player['count']}})
<<<<<<< HEAD

    db.User.update_one({'nickname': session.get("nickname")}, {'$set': {'count': -1}})

=======
            
>>>>>>> main
    global count
    count = -1
    rank={}
    user_db_sort = list(db.User.find({},{'_id': False},).sort("record",-1))
    if len(user_db_sort) > 10:
        for i in range(0, 10):
            user_single = user_db_sort[i]
            rank[user_single['nickname']] = user_single['record']
        
        return render_template("main.html",quiz={"quiz": "Game Start를 누르세요"}, nickname=session.get("nickname"), ranked = rank, count=player['count'])
    else:
        for i in range(0, len(user_db_sort)):
            user_single = user_db_sort[i]
            rank[user_single['nickname']] = user_single['record']
        
        return render_template("main.html",quiz={"quiz": "Game Start를 누르세요"}, nickname=session.get("nickname"), ranked = rank, count=player['count'])
    #return render_template("main.html", nickname=session.get("nickname"))

@app.route('/main/gamestart', methods=["GET"])
def makequiz():

    player = db.User.find_one({"nickname": session.get("nickname")})
    global count
    # 점수 세는 부분
    count += 1
    
    #user_nickname = "youngsang"  #"youngsang" 부분 나중에 클라이언트쪽에서 받아올 예정
    db.User.update_one({'nickname': session.get("nickname")}, {'$set': {'count': count}})

    #퀴즈 / 답 가져오는 부분
    quiz_category = request.args.get('quizType')

    quiz_list = list(db.quiz.find({'quiz_category': quiz_category}, {'_id': False})) # quiz DB 크기(갯수) 가져와서 난수 생성 및 해당 난수 quiz/answer 값 가져오기
    quiz_length = len(quiz_list)
    randomint = randint(1, quiz_length)

    quiz = {
    "quiz_category": quiz_category,
    "num": randomint,
    "quiz": quiz_list[randomint-1]["quiz"],
    "answer": quiz_list[randomint-1]["answer"]
    }

    user_db_sort = list(db.User.find({},{'_id': False},).sort("record",-1))
    rank={}
    if len(user_db_sort) > 10:
        for i in range(0,10):
            user_single = user_db_sort[i]
            rank[user_single['nickname']] = user_single['record']

        return render_template("main.html",quiz=quiz, nickname=session.get("nickname"), ranked = rank ,  count=player['count'])
    else:
        for i in range(0, len(user_db_sort)):
            user_single = user_db_sort[i]
            rank[user_single['nickname']] = user_single['record']
        
<<<<<<< HEAD
        return render_template("main.html",quiz=quiz, nickname=session.get("nickname"), ranked = rank, count = player['count'])
=======
        return render_template("main.html",quiz=quiz, nickname=session.get("nickname"), ranked = rank, count=player['count'])
>>>>>>> main

    # query = {"$and": [{"quiz_category": {"$gte": quiz_category}}, {"num": str(randomint)}]}
    # quiz = db.quiz.find_one(query)

    # Jinja2 템플릿 엔진을 사용하여 HTML 렌더링
<<<<<<< HEAD

=======
>>>>>>> main


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
        return render_template("create.html", new_num = new_num, nickname=session.get("nickname"))
    
    
    # elif request.method == "GET":
    #     quiz_list = list(db.quiz.find({}, {'_id': False}))
    #     len_num = len(quiz_list)
    #     new_num = len_num + 1
    
    #     return render_template("main.html")
        
    
    else:
        new_num = new_num + 1
        return render_template("create.html",new_num = new_num, nickname=session.get("nickname"))
    
    
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