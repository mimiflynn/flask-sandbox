from flask import render_template, request, Blueprint

dimensions_blueprint = Blueprint('dimensions', __name__,)


class Dimensions(object):
    height = 0
    width = 0

    def __init__(self, height, width):
        self.height = height
        self.width = width


def timelapse(**kwargs):
    print('start taking timelapse at {:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now()))
    print('timelapse parameters')


# http://localhost:5000/dimensions?height=25&width=500
@dimensions_blueprint.route('/dimensions')
def dimensions():
    height = request.args.get('height')
    width = request.args.get('width')
    return render_template('params.html', dimensions=Dimensions(height, width))
