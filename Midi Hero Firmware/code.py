print("Starting")

import keypad
from adafruit_midi.control.change import ControlChange
from microcontroller import pin
from digitalio import DigitalInOut, Direction, Pull
from superviser import ticks_ms
from analogio import AnalogIn
from kmk.modules import Module
from kmk.keys import AX, KC
from kmk.keys import Key
from kmk.kmktime import PeriodicTimer
from kmk.scanners import Scanner
from kmk.scanners.keypad import KeysScanner
from kmk.modules.midi import MidiKeys
from kmk.module.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.kmk_keyboard import KMKKeyboard

class Joystick(Module):
    def __init__(
        self,
        Xpin = pin.GPIO11,
        Ypin = pin.GPIO10,
        swPin = None,
        invX = False,
        invY = Flase
    ):
        self.AX = AnalogIn(Xpin)
        self.AY = AnalogIn(Ypin)
        if swPin == None:
            self.SW = None
        else:
            dio = DigitalInOut(swPin)
            dio.direction = Direction.INPUT
            dio.pull = Pull.UP
            self.sw = dio
        self.prev_SW = False

        self.dirX = -1 if invX else 1
        self.dirY = -1 if invY else 1

        self._timer = PeriodicTimer(10)

    def before_matrix_scan(self, keyboard):
        if not self._timer.tick():
            return

        x = self._fix_value(self.AX.value, self.dirX)
        y = self._fix_value(self.AY.value, self.dirY)
        if x != 0:
            AX.X.move(keyboard, x)
        if y != 0:
            AX.Y.move(keyboard, y)
        if self.sw != None:
            sw = not self.sw.value
            if(self.prev_SW or sw) and not (self.prev_SW and sw):
                keyboard.pre_process_key(KC.MB_LMB, is_pressed=sw)
            sel.prev_SW = sw

    def _fix_value(self, v, d):
        return int((v - 32767.5) * d / 2048)

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def during_bootup(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return
    

keyboard = KMKKeyboard()

midi = MidiKeys()
media_keys = MediaKeys()

keyboard.matrix = [

    KeysScanner([pin.GPIO1, pin.GPIO2,pin.GPIO3, pin.GPIO4, pin.GPIO5], value_when_pressed=False, pull=True)
]

encoder = EncoderHandler()
encoder.pins = ((pin.GPIO6, pin.GPIO7, None),)  # A = TX, B = RX, no button
encoder.map = [((KC.VOLD, KC.VOLU, KC.NO),)]

keyboard.modules = [midi, encoder, sliders]
keyboard.extensions = [
    media_keys
]