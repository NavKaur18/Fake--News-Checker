from flask import Flask, render_template, request
from processing import process
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    value = request.form.to_dict()
    news = ""
    results = []
    percent = 0

    if 'news' in value.keys():
        news = value['news']
        results = process(news)
        percent = sum([result['result'] for result in results]) / len(results) *100
    
    return render_template('index.html', results = results, news = news, percent = percent)

if __name__ == '__main__':
    app.run(debug=True)