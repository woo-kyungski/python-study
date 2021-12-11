# 플라스크 import 
from flask import Flask

# 플라스크 객체 생성
app = Flask(__name__)

# 서버 구동시, 개발 정의 URL값과 플라스크에서 정의된 함수를 연결
@app.route("/hello1")
def hello_flask():
		return "Hello, WKSK"

@app.route("/hello2", methods =['GET'])
def hello_flask_get():
    return "Get Method"
    
@app.route("/hello2", methods = ['POST'])
def hello_flask_post():
    return "Post Method"
    
@app.route("/hello/wksk")
def hello_name() :
    return "wksk"

@app.route("<hello/name>")
def hello_name3(name) :
     print(name)
     
     
# 해당 파일 실행시 플라스크 서버 실행
if __name__ == "__main__":
		app.run(host = "127.0.0.1", port = 5000, debug = True)