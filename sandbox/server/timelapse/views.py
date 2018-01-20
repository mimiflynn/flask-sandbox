import datetime
from flask import render_template, request, Blueprint

timelapse_blueprint = Blueprint('timelapse', __name__,)


def timelapse(frames, freq):
    print('start taking timelapse at {:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now()))
    print('timelapse parameter frames  is ' + frames + ' and frequency is ' + freq)


# http://localhost:5000/timelapse?frames=100&freq=2
@timelapse_blueprint.route('/timelapse')
def photos():
    frames = request.args.get('frames')
    freq = request.args.get('freq')
    timelapse(frames, freq)
    return render_template('timelapse.html', params=Params(frames, freq))
