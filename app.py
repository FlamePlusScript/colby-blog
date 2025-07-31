from flask import Flask, render_template, request, redirect, session, url_for
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a more secure key in production

ADMIN_USERNAME = "horsmanAdmin"
ADMIN_PASSWORD = "Spyglass4821"

def load_posts():
    try:
        with open('posts.json', 'r') as f:
            return json.load(f)
    except:
        return []

def save_post(title, content):
    posts = load_posts()
    posts.insert(0, {
        "title": title,
        "content": content,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=2)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blog')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == ADMIN_USERNAME and request.form['password'] == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('new_post'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        save_post(title, content)
        return redirect(url_for('index'))
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
from flask import Flask, render_template, request, redirect, session, url_for
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a more secure key in production

ADMIN_USERNAME = "horsmanAdmin"
ADMIN_PASSWORD = "Spyglass4821"

def load_posts():
    try:
        with open('posts.json', 'r') as f:
            return json.load(f)
    except:
        return []

def save_post(title, content):
    posts = load_posts()
    posts.insert(0, {
        "title": title,
        "content": content,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=2)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blog')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == ADMIN_USERNAME and request.form['password'] == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('new_post'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        save_post(title, content)
        return redirect(url_for('index'))
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
