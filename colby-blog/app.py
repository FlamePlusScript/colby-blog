from flask import Flask, render_template, request, redirect
import json
from datetime import datetime

app = Flask(__name__)

def load_posts():
    try:
        with open('posts.json', 'r') as f:
            return json.load(f)
    except:
        return []

def save_post(content):
    posts = load_posts()
    posts.insert(0, {
        "content": content,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        save_post(content)
        return redirect('/')
    posts = load_posts()
    return render_template('index.html', posts=posts)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
