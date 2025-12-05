# main.py
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.digitalio import DirectPin

keyboard = KMKKeyboard()

keyboard.matrix = DirectPin(
    pins = [
        board.GP1,
        board.GP2,
        board.GP4,
        board.GP3,
        board.GP26,
        board.GP27,
        board.GP28,
        board.GP29,
    ]
)

keyboard.keymap = [
    [
        KC.A, KC.B, KC.C, KC.D,
        KC.E, KC.F, KC.G, KC.H,
    ]
]

if __name__ == '__main__':
    keyboard.go()
