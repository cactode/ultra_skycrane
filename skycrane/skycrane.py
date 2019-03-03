from skycrane.controller.controller import Controller
from config import Command, DEFAULT_MOVE
from time import sleep
import inputs

THRESHOLD = 1000
DWELL_TIME = 2

class SkyCrane():
    def __init__(self):
        self.c = Controller()

        pads = inputs.devices.gamepads
        if len(pads) == 0:
            raise IOError("No gamepad found")

    def run(self):
        events = inputs.get_gamepad()
        doing_something = False
        for event in events:
            doing_something = doing_something or self.handle(event)

        if doing_something:
            sleep(DWELL_TIME) 

    def handle(self, event):
        if event.code == "ABS_X":
            if event.state < -THRESHOLD:
                self.c.do(Command.LEFT, DEFAULT_MOVE)
                return True
            elif event.state > THRESHOLD:
                self.c.do(Command.RIGHT, DEFAULT_MOVE)
                return True
        if event.code == "ABS_Y":
            if event.state < -THRESHOLD:
                self.c.do(Command.DOWN, DEFAULT_MOVE)
                return True
            elif event.state > THRESHOLD:
                self.c.do(Command.UP, DEFAULT_MOVE)
                return True
        if event.code == "BTN_TL":
            if event.state:
                self.c.do(Command.CHEESE, DEFAULT_MOVE)
                return True
        return False

    
        


        
