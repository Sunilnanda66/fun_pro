import datetime
from flask import Flask, render_template, request
import pywhatkit as pwt
import gunicorn


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=["POST"])
def index_post():
    text = request.form['text']
    processed_text = pwt.search(text)
    return render_template("index.html", )

@app.route("/video")
def video():
    return render_template("video.html")

@app.route('/video', methods=["POST"])
def video_post():
    content = request.form['content']
    processed_text = pwt.playonyt(content)
    return render_template("video.html", )


if __name__ == "__main__":
    app.run(debug=True)
