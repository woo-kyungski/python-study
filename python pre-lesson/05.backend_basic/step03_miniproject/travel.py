import crawling, mapping
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/travel")
def drawing_travel():
		# 데이터 수집 대상 페이지 지정하기
		url = 'https://www.forbes.com/advisor/travel-rewards/top-50-best-places-to-visit/'
		
		# 크롤링한 여행지 리스트를 site_list 변수에 담기
		site_list = crawling.crawling_sites(url)

		# 시각화 결과물 템플릿을 html_map 변수에 담기 (단, 시각화 결과물객체 뒤에  ._repr_html_() 붙이기)
		html_map = mapping.drawing_map(url)._repr_html_()

		# render_template() 내부 파라미터 작성하기
		return render_template("map.html", sites = site_list, map = html_map)

if __name__ == "__main__":
		app.run(host = "127.0.0.1", port = 5000, debug = True)