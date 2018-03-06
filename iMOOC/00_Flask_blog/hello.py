from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s</h1>' % name  # %与name之间要有空格。


@app.route('/mobile/<int:id>')
def mobile(id):
    return '<h1>Your mobile phone number is : %s</h1>' % id


if __name__ == '__main__':
    app.run(debug = True)
