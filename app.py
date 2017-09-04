from flask import Flask, render_template, request, send_from_directory, url_for

app = Flask(__name__)

class Dimensions(object):
    height = 0
    width = 0

    def __init__(self, height, width):
        self.height = height
        self.width = width


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/styles/<path:path>')
def styles(path):
    return send_from_directory('styles', path)


@app.route('/dimensions')
def dimensions():
    height = request.args.get('height')
    width = request.args.get('width')
    return render_template('params.html', dimensions=Dimensions(height, width))


@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username='John Doe')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
