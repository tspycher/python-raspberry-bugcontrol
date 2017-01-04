import flask
from lib import Bug
from logging import StreamHandler
import logging

app = flask.Flask(__name__)
bug = Bug()


@app.route("/")
def index():
    result = ['<pre>%s</pre>' % bug.graphic]
    result.append('<ul>')
    for x in ['l', 'h', 'f', 'o', 'p', 'w']:
        result.append('<a href="/%(cmd)s">%(cmd)s</a>' % {'cmd': x})

    result.append('</ul>')
    return "\n".join(result)

@app.route("/l")
def toggleLowBeamLight():
    bug.toggleLowBeamLight()
    return flask.jsonify(**bug.getGpioState())

@app.route("/h")
def toggleHeadLight():
    bug.toggleHeadLight()
    return flask.jsonify(**bug.getGpioState())

@app.route("/f")
def doFlash():
    bug.doFlash()
    return flask.jsonify(**bug.getGpioState())

@app.route("/o")
def toggleTurnLightLeft():
    bug.toggleTurnLightLeft()
    return flask.jsonify(**bug.getGpioState())

@app.route("/p")
def toggleTurnLightRight():
    bug.toggleTurnLightRight()
    return flask.jsonify(**bug.getGpioState())

@app.route("/w")
def toggleWarningLights():
    bug.toggleWarningLights()
    return flask.jsonify(**bug.getGpioState())

if __name__ == "__main__":
    handler = StreamHandler()
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)

    app.logger.warning("running")
    bug.setLogger(app.logger)
    bug.bringToLife(interactive=False)
    app.run()

