from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)


app = Flask(__name__)

@app.route('/')
def base():
    return render_template("rogin.html")


@app.route('/rogin',methods=["GET","POST"])
def rogin():
    
    return render_template("rogin.html")


@app.route('/register',methods=["GET","POST"])
def register():
    
    return render_template("register.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)