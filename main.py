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

anthem = [
    (3, "eight_note", 1.5),
    (4, "sixteenth_note", 1),
    (5, "quarter_note", 1),
    (5, "quarter_note", 1),  # takt 2
    (4, "eight_note", 1.5),
    (3, "sixteenth_note", 1),
    (6, "eight_note", 1),
    (5, "eight_note", 1),
    (4, "eight_note", 1),
    (3, "eight_note", 1),  # takt 3
    (2, "eight_note", 1.5),
    (2, "sixteenth_note", 1),
    (5, "quarter_note", 1.5),
    (4, "sixteenth_note", 1),  # takt 4
    (4, "quarter_note", 1),
    (3, "quarter_note", 1),
    (0, "quarter_note,", -1),  # takt 5
    (3, "eight_note", 1.5),
    (4, "sixteenth_note", 1),
    (5, "quarter_note", 1),
    (5, "quarter_note", 1),  # takt 6
    (4, "eight_note", 1.5),
    (3, "sixteenth_note", 1),
    (6, "eight_note", 1),
    (5, "eight_note", 1),
    (4, "eight_note", 1),
    (3, "eight_note", 1),  # takt 7
    (2, "eight_note", 1.5),
    (2, "sixteenth_note", 1),
    (5, "quarter_note", 1.5),
    (0, "sixteenth_note", 1),  # takt 8
    (2, "quarter_note", 1),
    (1, "quarter_note", 1),
    (0, "quarter_note", -1),
    (2, "quarter_note", 1),
    (2, "quarter_note", 1.5),
    (4, "eight_note", 1),                  # takt9
    (4, "eight_note", 1),
    (3, "eight_note", 1),
    (3, "half_note", 1),  # takt 10
    (4, "quarter_note", 1.5),
    (4, "sixteenth_note", 1),
    (4, "quarter_note", 1),
    (4, "eight_note", 1),
    (6, "eight_note", 1),  # takt 11
    (6, "quarter_note", 1),
    (5, "half_note", 1),  # takt 12
    (3, "eight_note", 1.5),
    (5, "sixteenth_note", 1),
    (8, "quarter_note", 1.5),
    (7, "eight_note", 1),  # takt 13
    (7, "eight_note", 1),
    (6, "eight_note", 1),
    (6, "half_note", 1),  # takt 14
    (5, "eight_note", 1),
    (5, "eight_note", 1),
    (4, "quarter_note", 1.5),
    (0, "eight_note", 1),  # takt 15
    (2, "quarter_note", 1),
    (1, "quarter_note", 1),
    (0, "quarter_note", -1),  # takt 16
]

for i in anthem:
    value, note, multiplier = i
    if multiplier == -1:
        sleep(value/1000)
    else:
        Beep(sounds[value], int(notes[note]*multiplier))
