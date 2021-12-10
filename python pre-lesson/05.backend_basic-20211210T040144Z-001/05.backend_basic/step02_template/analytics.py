from flask import Flask, render_template

app = Flask(__name__)

# !!! 7번 라인 route 작성
# !!! 10번 라인 render_template() 파라미터 작성
@app.route("")
def view_analytics(name):
	pre_course = ['파이썬 프로그래밍 기초1', '파이썬 프로그래밍 기초2', '데이터 수집', '데이터 시각화', '백엔드 프로그래밍 기초']
	return render_template()

if __name__ == "__main__":
		app.run(host = "127.0.0.1", port = 5000, debug = True)