from winsound import Beep
from time import sleep
from math import pow

# c d e f g a h
# step = pow(2, 1/6) (1/12 for eg. a4 to a#4)
# a4 = 440, so a4 is the 27th sound (?)
# so it's c1 * step**26 (?)
# ignore what's above, basically 440hz is the 1st sound on the staff (the one with added line)
# ... i think

base = pow(2, 1/12)
bpm = 116
base_sound = 261.626
quarter_note = 0.5
sounds = [base_sound]

for i in range(1, 11):
    sounds.append(sounds[i-1] * base)
sounds = [int(x) for x in sounds[2:]]
print(sounds)

notes = {"full_note": int(quarter_note*4000), "half_note": int(quarter_note*2000), "quarter_note": int(quarter_note*1000),
         "eight_note": int(quarter_note*500), "sixteenth_note": int(quarter_note*250)}

Beep(sounds[3], int(notes["eight_note"]*1.5))
