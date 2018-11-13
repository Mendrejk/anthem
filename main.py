from winsound import Beep
from time import sleep
from math import pow

# c d e f g a h
# step = pow(2, 1/6) (1/12 for eg. a4 to a#4)
# a4 = 440, so a4 is the 27th sound (?)
# so it's c1 * step**26 (?)
# ignore what's above, basically 440hz is the 1st sound on the staff (the one with added line)
# ... i think

base = pow(2, 1/6)
bpm = 116
base_sound = 440
sounds = [base_sound * base**x for x in range(10)]


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
