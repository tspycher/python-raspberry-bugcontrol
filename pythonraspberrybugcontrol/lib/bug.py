import threading
import time
import curses

from . import Relay

class Bug(object):

    INTERVAL = 0.5

    bug_ascii = """
                        /-----------------------------\\
            /---------\/                               \/---------\\
           /           \                               /           \\
          /    /----\   \                             /   /----\    \\
         /    /   %(headlightL)s  \   \                           /   /  %(headlightR)s   \    \\
        |     |   %(lowbeamL)s  |    \            V            /    |  %(lowbeamR)s   |    |
        |     \      /     \           W           /     \      /    |
        |      \----/       \_____________________/       \----/     |
        |  ______                                            ______  |
        | |___%(turnlightL)s__|                                          |__%(turnlightR)s___| |
        --------------------------------------------------------------
    """

    headlight = None
    lowbeam = None
    turnlight_left = None
    turnlight_right = None
    flash = None
    warning = None
    _previous_state_headlight_left = None
    _previous_state_headlight_right = None
    _previous_state_turnlight_left = None
    _previous_state_turnlight_right = None

    _current_gpio = None

    _logger = None
    _relay = None

    _relay_mapping = {
            "headlight": 2,
            "lowbeam": 1,
            "turnlight_left": 3,
            "turnlight_right": 4
        }

    def __init__(self, logger=None):
        super(Bug, self).__init__()
        self._current_gpio = {}
        self.setLogger(logger)
        self._relay = Relay(logger=self._logger)

    def setLogger(self, logger):
        self._logger = logger

    def getGpioState(self):
        return self._current_gpio

    @property
    def headlightL(self):
        if self.headlight or self.flash:
            if self.flash:
                self.flash -= 1
                if self._previous_state_headlight_left:
                    self._previous_state_headlight_left = False
                    return False
                else:
                    self._previous_state_headlight_left = True
                    return True
            else:
                return True
        return False

    @property
    def headlightR(self):
        if self.headlight or self.flash:
            if self.flash:
                if self._previous_state_headlight_right:
                    self._previous_state_headlight_right = False
                    return False
                else:
                    self._previous_state_headlight_right = True
                    return True
            else:
                return True
        return False

    @property
    def bothlowbeams(self):
        if self.lowbeam:
            return True
        return False

    @property
    def lowbeamL(self):
        return self.bothlowbeams

    @property
    def lowbeamR(self):
        return self.bothlowbeams

    @property
    def turnlightL(self):
        if self.turnlight_left:
            if self._previous_state_turnlight_left:
                self._previous_state_turnlight_left = False
            else:
                self._previous_state_turnlight_left = True
            return self._previous_state_turnlight_left
        return False

    @property
    def turnlightR(self):
        if self.turnlight_right:
            if self._previous_state_turnlight_right:
                self._previous_state_turnlight_right = False
            else:
                self._previous_state_turnlight_right = True
            return self._previous_state_turnlight_right
        return False

    @property
    def graphic(self):
        return self.bug_ascii % {
            'headlightL': self._visualizeState(self.headlightL),
            'headlightR': self._visualizeState(self.headlightR),
            'lowbeamL': self._visualizeState(self.lowbeamL),
            'lowbeamR': self._visualizeState(self.lowbeamR),
            'turnlightL': self._visualizeState(self.turnlightL),
            'turnlightR': self._visualizeState(self.turnlightR)
        }

    def toggleLowBeamLight(self):
        if self.lowbeam:
            self.lowbeam = False
        else:
            self.lowbeam = True
        return self.lowbeam

    def toggleHeadLight(self):
        if self.headlight:
            self.headlight = False
        else:
            self.headlight = True
        return self.headlight

    def doFlash(self, times = 3):
        times = times * 2
        self._previous_state_headlight_left = False
        self._previous_state_headlight_right = False
        if self.flash:
            self.flash = 0
        else:
            self.flash = times
        return self.flash

    def toggleTurnLightLeft(self):
        if self.turnlight_left:
            self.turnlight_left = False
        else:
            self.turnlight_right = False
            self.turnlight_left = True
        return self.turnlight_left

    def toggleTurnLightRight(self):
        if self.turnlight_right:
            self.turnlight_right = False
        else:
            self.turnlight_left = False
            self.turnlight_right = True
        return self.turnlight_right

    def toggleWarningLights(self):
        if self.turnlight_right or self.turnlight_left:
            self.turnlight_right = False
            self.turnlight_left = False
            self.warning = False
            return False

        self.turnlight_right = True
        self.turnlight_left = True
        self.warning = True
        return True

    def diff_dict(self, new, old):
        diff = {}
        for key in new.keys():
            if not key in old:
                diff[key] = new[key]
            else:
                if new[key] != old[key]:
                    diff[key] = new[key]
        return diff

    def _controlGPIO(self):
        new_gpio = {
            "headlight": self.headlightL & self.headlightR,
            "lowbeam": self.lowbeamL & self.lowbeamR,
            "turnlight_left": self.turnlightL,
            "turnlight_right": self.turnlightR,
        }
        diff = self.diff_dict(new=new_gpio, old=self._current_gpio)
        if diff:
            self._current_gpio = new_gpio
            if self._logger:
                self._logger.info("GPIO State change: %s" % str(diff))

            for light in diff.keys():
                relay_port = self._relay_mapping[light]
                if diff[light]:
                    getattr(self._relay, 'on_%i' % relay_port)()
                else:
                    getattr(self._relay, 'off_%i' % relay_port)()


    def life(self, interactive=False):
        if interactive:
            stdscr = curses.initscr()
            stdscr.nodelay(True)

        while True:
            if interactive:
                stdscr.addstr(1, 0, self.graphic)
                stdscr.refresh()
                c = stdscr.getch(0, 0)
                if not c == -1:
                    cmd = str(chr(c)).lower()
                    if cmd == '?':
                        stdscr.addstr(0, 2, "f = flash, w = warning, h = headlight, l = lowbeam, o = turnleft, p = turnright")
                    else:
                        self._interpretInput(cmd)
                    del c

            else:
                self._controlGPIO()
            time.sleep(Bug.INTERVAL)


    def _interpretInput(self, input):
        input = str(input).lower()
        if input == "f":
            self.doFlash(times=3)
        elif input == "w":
            self.toggleWarningLights()
        elif input == "h":
            self.toggleHeadLight()
        elif input == "l":
            self.toggleLowBeamLight()
        elif input == "p":
            self.toggleTurnLightRight()
        elif input == "o":
            self.toggleTurnLightLeft()

    def bringToLife(self, interactive=False):
        t = threading.Thread(target=self.life, args=(interactive,))
        if not interactive:
            t.daemon = True
        t.start()
        if self._logger: self._logger.warning("Started bug in seperate thread")

    def _visualizeState(self, state):
        if state:
            return "X"
        return " "

if __name__ == "__main__":
    bug = Bug()
    bug.doFlash(times=3)
    bug.toggleLowBeamLight()
    #bug.toggleTurnLightLeft()
    #bug.toggleTurnLightRight()
    #bug.toggleWarningLights()
    bug.bringToLife(interactive=True)
    """bug.toggleHeadLight()
    bug.toggleLowBeamLight()
    bug.toggleTurnLightLeft()
    bug.toggleTurnLightRight()
    print bug.graphic
    bug.toggleHeadLight()
    bug.toggleLowBeamLight()
    bug.toggleTurnLightLeft()
    bug.toggleTurnLightRight()
    print bug.graphic
    bug.doFlash(3)
    bug.toggleWarningLights()
    print bug.graphic
    bug.toggleWarningLights()
    print bug.graphic"""