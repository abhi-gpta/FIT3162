from flask import Flask, render_template

app = Flask(__name__)




# @app.route('/images/<filename>')
# def serve_image(filename):
#     return send_from_directory('static/images', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/navi')
def nav():
    return render_template('nav.html')


@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/product.html')
def product():
    return render_template('product.html')

@app.route('/trends.html')
def trend():
    return render_template('trends.html')

@app.route('/seasonal.html')
def seasonal():
    return render_template('seasonal.html')

@app.route('/forecast.html')
def forecast():
    return render_template('forecast.html')