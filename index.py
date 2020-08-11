from flask import Flask,render_template

app=Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio-details.html')

@app.route('/innerpage')
def innerpage():
    return render_template('inner-page.html')
app.run()