import flask
from lib import Bug
import logging
from flask_cors import CORS, cross_origin

def create_app():
    app = flask.Flask(__name__, static_url_path='/web', static_folder='../static-web')
    app.logger.setLevel(logging.INFO)
    CORS(app)
    bug = Bug(logger=app.logger)

    @app.route("/")
    def index():
        result = ['<pre>%s</pre>' % bug.graphic]
        result.append('<ul>')
        for x in ['l', 'h', 'f', 'o', 'p', 'w']:
            result.append('<a href="/cmd/%(cmd)s">%(cmd)s</a>' % {'cmd': x})

        result.append('</ul>')
        return "\n".join(result)

    @app.route("/status")
    def status():
        return flask.jsonify(**bug.getGpioState())

    @app.route("/cmd/l")
    def toggleLowBeamLight():
        bug.toggleLowBeamLight()
        return flask.jsonify(**bug.getGpioState())

    @app.route("/cmd/h")
    def toggleHeadLight():
        bug.toggleHeadLight()
        return flask.jsonify(**bug.getGpioState())

    @app.route("/cmd/f")
    def doFlash():
        bug.doFlash()
        return flask.jsonify(**bug.getGpioState())

    @app.route("/cmd/o")
    def toggleTurnLightLeft():
        bug.toggleTurnLightLeft()
        return flask.jsonify(**bug.getGpioState())

    @app.route("/cmd/p")
    def toggleTurnLightRight():
        bug.toggleTurnLightRight()
        return flask.jsonify(**bug.getGpioState())

    @app.route("/cmd/w")
    def toggleWarningLights():
        bug.toggleWarningLights()
        return flask.jsonify(**bug.getGpioState())

    return (app, bug)
