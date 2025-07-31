from flask import Flask, render_template, request, redirect, session
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session

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
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'horsmanAdmin' and password == 'Spyglass4821':
            session['logged_in'] = True
            return redirect('/new')
        else:
            return 'Invalid credentials', 403
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if not session.get('logged_in'):
        return redirect('/login')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        save_post(title, content)
        return redirect('/')
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
