from enum import Enum

# grbl settings
GRBL_CONFIG = [
    "$21=0",  # hard limits
    "$24=6000",  # homing feed
    "$25=6000",  # homing seek
    "$100=2.50",  # x mm per step
    "$101=2.50",  # y mm per step
    "$110=6000",  # x max speed
    "$111=6000",  # y max speed
    "$120=100",  # x acceleration
    "$121=100",  # y acceleration
    "$130=100000",  # x size
    "$131=100000",  # y size
    "G91" # relative mode
]

# hardware settings
GRBL_PORT = "COM9"
GRBL_BAUD = 115200

# command options
class Command(Enum):
    UP = "K_UP"
    DOWN = "K_DOWN"
    LEFT = "K_LEFT"
    RIGHT = "K_RIGHT"
    CHEESE = "K_SPACE"
    STOP = "K_ESCAPE"

DEFAULT_MOVE = 100
MAX_MOVE = 500
