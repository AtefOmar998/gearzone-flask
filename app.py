from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    lang = request.args.get('lang', 'en')
    theme = request.args.get('theme', 'light')
    return render_template('index.html', lang=lang, theme=theme)

@app.route('/product')
def product():
    lang = request.args.get('lang', 'en')
    theme = request.args.get('theme', 'light')
    return render_template('product.html', lang=lang, theme=theme)

@app.route('/cart')
def cart():
    lang = request.args.get('lang', 'en')
    theme = request.args.get('theme', 'light')
    return render_template('cart.html', lang=lang, theme=theme)

@app.route('/login')
def login():
    lang = request.args.get('lang', 'en')
    theme = request.args.get('theme', 'light')
    return render_template('login.html', lang=lang, theme=theme)

@app.route('/store-dashboard')
def store_dashboard():
    lang = request.args.get('lang', 'en')
    theme = request.args.get('theme', 'light')
    return render_template('store_dashboard.html', lang=lang, theme=theme)

if __name__ == '__main__':
    app.run(debug=True)
