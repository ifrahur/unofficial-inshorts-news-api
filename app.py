from flask import Flask, request, jsonify
from webscraping import getNews
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "i_am_not_feeling_sleepy_so_i_am_coding_this"
CORS(app)


@app.route('/')
def home():
    return '<br><br>Made by <a href="https://ifrahur.me/">Ifrahur</a> <br><br>Catigories: <a href="/news?category=all">all</a> , <a href="/news?category=national">Indian News only</a> , <a href="/news?category=business">business</a> , <a href="/news?category=sports">sports</a> , <a href="/news?category=world">world</a> , <a href="/news?category=politics">politics</a> , <a href="/news?category=technology">technology</a> , <a href="/news?category=startup">startup</a> , <a href="/news?category=entertainment">entertainment</a> , <a href="/news?category=science">science</a> , <a href="/news?category=automobile">automobile</a> , <a href="/news?category=miscellaneous">miscellaneous</a> ,   '


@app.route('/news')
def news():
    if request.method == 'GET':
        return jsonify(getNews(request.args.get('category')))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
