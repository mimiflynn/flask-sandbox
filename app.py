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


# http://localhost:5000/dimensions?height=25&width=500
@app.route('/dimensions')
def dimensions():
    height = request.args.get('height')
    width = request.args.get('width')
    return render_template('params.html', dimensions=Dimensions(height, width))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
