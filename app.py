from flask import Flask, render_template, request, redirect
import json
from datetime import datetime
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

POSTS_FILE = 'posts.json'

# Ensure the JSON file exists
def load_posts():
    if not os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, 'w') as f:
            json.dump([], f)
    try:
        with open(POSTS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_post(title, content):
    posts = load_posts()
    posts.insert(0, {
        "title": title,
        "content": content,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    with open(POSTS_FILE, 'w') as f:
        json.dump(posts, f, indent=2)

@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@app.route('/new', methods=['POST'])
def new_post():
    title = request.form.get('title')
    content = request.form.get('content')
    if title and content:
        save_post(title, content)
    return redirect('/')

# Health check route (useful for Render)
@app.route('/healthz')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
