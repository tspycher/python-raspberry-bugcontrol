import flask
from lib import Bug
import logging
from flask_cors import CORS, cross_origin

DEFAULT_FLASHTIMES = 3

def create_app():
    app = flask.Flask(__name__, static_url_path='/web', static_folder='../static-web')
    app.logger.setLevel(logging.INFO)
    CORS(app, expose_headers='X-Server-Identity')
    bug = Bug(logger=app.logger)

    @app.after_request
    def set_server_identity_header(response):
        response.headers["X-Server-Identity"] = "BUGCONTROL"
        return response

    @app.route("/")
    def index():
        result = ['<pre>%s</pre>' % bug.graphic]
        result.append('<ul>')
        for x in ['l', 'h', 'f', 'o', 'p', 'w', 's']:
            result.append('<a href="/cmd/%(cmd)s">%(cmd)s</a>' % {'cmd': x})

        result.append('</ul>')
        return "\n".join(result)

    @app.route("/status")
    def status():
        state = bug.getGpioState()
        state['turnlight_left_on'] = True if bug.turnlight_left_on else False
        state['turnlight_right_on'] = True if bug.turnlight_right_on else False
        state['warning'] = True if bug.warning else False
        state['warning'] = True if bug.warning else False
        state['static_warning'] = True if bug.static_warning else False
        state['flash'] = True if bug.flash else False
        state['flashing'] = True if bug.flash > 0 else False
        state['flash_count'] = 0 if not bug.flash else bug.flash
        state['blink_interval'] = Bug.INTERVAL
        state['default_flash'] = DEFAULT_FLASHTIMES
        return flask.jsonify(**state)

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
        bug.doFlash(times=DEFAULT_FLASHTIMES)
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

    @app.route("/cmd/s")
    def toggleStaticWarningLights():
        bug.toggleStaticWarningLights()
        return flask.jsonify(**bug.getGpioState())

    return (app, bug)
