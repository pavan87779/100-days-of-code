from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/blog')
def get_blog():
    url = 'https://api.npoint.io/c9d175b4ea3e2f704c78'
    response = requests.get(url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)