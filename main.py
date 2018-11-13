from winsound import Beep
from time import sleep
from math import pow
#winsound.Beep(300, 1000)
# sleep(0.5)
#winsound.Beep(200, 1000)
strings = [324, 243, 192, 144, 108, 81]
strings = [x*2 for x in strings]
base = pow(2, 1/12)
delay = 500
bpm = 60


def to_hz(string, pow):
    #print(strings[string-1], base, pow, base**pow)
    return strings[string-1] * base**pow


def note(string, pow):
    hz = int(to_hz(string, pow))
    Beep(hz, delay)
    print(hz, delay)
    sleep(0.2)


note(4, 4)
note(3, 0)
note(3, 2)
note(3, 2)
note(3, 2)
