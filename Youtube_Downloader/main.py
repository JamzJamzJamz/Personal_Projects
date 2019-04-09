import yt_convert
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def form_update():
    if request.method == 'POST':
        url = request.form['url']
        title = request.form['title']
        video = yt_convert.convert(url, title)
        video = '\n'.join(video)
        return render_template('index.html', complete = video)


if __name__ == '__main__':
    app.run(debug=True)