import datetime
from flask import render_template, request, Blueprint

timelapse_blueprint = Blueprint('timelapse', __name__,)


class Params(object):
    frames = 0
    freq = 0

    def __init__(self, frames, freq):
        self.frames = frames
        self.freq = freq


def timelapse(frames, freq):
    print('start taking timelapse at {:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now()))
    print('timelapse parameter frames  is ' + str(frames) + ' and frequency is ' + str(freq))


# http://localhost:5000/timelapse?frames=100&freq=2
@timelapse_blueprint.route('/timelapse')
def photos():
    frames = request.args.get('frames', 50, type=int)
    freq = request.args.get('freq', 5, type=int)
    timelapse(frames, freq)
    return render_template('timelapse.html', params=Params(frames, freq))
