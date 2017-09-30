# sandbox/__init__.py

from flask import Flask

from sandbox.server.dimensions.views import dimensions_blueprint
from sandbox.server.main.views import main_blueprint

app = Flask(
    __name__,
    template_folder='client/templates',
    static_folder='client/static'
)


app.register_blueprint(dimensions_blueprint)
app.register_blueprint(main_blueprint)
