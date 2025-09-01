from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(24)

# ✅ Helper function: Get user by email from DB
def get_user(email):
    conn = sqlite3.connect('gearzone.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = c.fetchone()
    conn.close()
    return user

@app.route('/')
def homepage():
    lang = request.args.get('lang', 'en')
    theme = request.args.get('theme', 'light')
    return render_template('index.html', lang=lang, theme=theme, user=session.get('user'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    lang = request.args.get('lang', 'en')
    theme = request.args.get('theme', 'light')

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = get_user(email)

        if user and check_password_hash(user['password'], password):
            session['user'] = {
                'id': user['id'],
                'name': user['name'],
                'email': user['email'],
                'type': user['type']
            }
            flash('Login successful!')
            return redirect(url_for('homepage', lang=lang, theme=theme))
        else:
            flash('Invalid email or password.')

    return render_template('login.html', lang=lang, theme=theme, user=session.get('user'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    lang = request.args.get('lang', 'en')
    theme = request.args.get('theme', 'light')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['type']

        conn = sqlite3.connect('gearzone.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (name, email, password, type) VALUES (?, ?, ?, ?)",
                      (name, email, generate_password_hash(password), user_type))
            conn.commit()
            flash("Account created successfully! Please login.")
            return redirect(url_for('login', lang=lang, theme=theme))
        except sqlite3.IntegrityError:
            flash("Email already registered.")
        finally:
            conn.close()

    return render_template('signup.html', lang=lang, theme=theme, user=session.get('user'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out successfully.")
    return redirect(url_for('homepage'))

@app.route('/cart')
def cart():
    lang = request.args.get('lang', 'en')
    theme = request.args.get('theme', 'light')
    return render_template('cart.html', lang=lang, theme=theme)

if __name__ == '__main__':
    app.run(debug=True)