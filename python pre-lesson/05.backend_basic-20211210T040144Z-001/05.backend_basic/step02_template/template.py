from flask import Flask, render_template

app = Flask(__name__)

@app.route("/template-basic")
def view_template():
	title = '템플릿'
	nums_list = [1, 2, 3, 4, 5]
	nums_dict = { 'one' : 1, 'two' : 2 }
	return 

if __name__ == "__main__":
		app.run(host = "127.0.0.1", port = 5000, debug = True)