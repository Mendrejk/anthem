from winsound import Beep
from time import sleep
from math import pow
import pysine

root = pow(2, 1/12)
bpm = 116
base_sound = 329.6276  # E4
quarter_note = 0.5
sounds = [base_sound]


for i in range(1, 14):
    sounds.append(sounds[i-1] * root)
s = [int(x) for x in sounds]
sounds = [int(x) for x in sounds]
temp_sounds = []
for i in range(1, len(sounds)):
    if i % 7 in [2, 4, 6] and i < 13:
        continue
    elif i % 7 in [0, 2, 4] and i >= 13:
        continue
    else:
        temp_sounds.append(sounds[i])
sounds[-1] = 698
sounds = [int(base_sound)] + temp_sounds
sounds[4] = 466

notes = {"full_note": int(quarter_note*4000), "half_note": int(quarter_note*2000), "quarter_note": int(quarter_note*1000),
         "eight_note": int(quarter_note*500), "sixteenth_note": int(quarter_note*250)}

anthem = [
    (3, "eight_note", 1.5),
    (4, "sixteenth_note", 1),
    (5, "quarter_note", 1),
    (5, "quarter_note", 1),  # takt 2
    (5, "eight_note", 1.5),
    (3, "sixteenth_note", 1),
    (6, "eight_note", 1),
    (5, "eight_note", 1),
    (4, "eight_note", 1),
    (3, "eight_note", 1),  # takt 3
    (2, "eight_note", 1.5),
    (2, "sixteenth_note", 1),
    (5, "quarter_note", 1.5),
    (4, "eight_note", 1),  # takt 4
    (4, "quarter_note", 1),
    (3, "quarter_note", 1),
    (0, "quarter_note", -1),  # takt 5
    (3, "eight_note", 1.5),
    (4, "sixteenth_note", 1),
    (5, "quarter_note", 1),
    (5, "quarter_note", 1),  # takt 6
    (5, "eight_note", 1.5),
    (3, "sixteenth_note", 1),
    (6, "eight_note", 1),
    (5, "eight_note", 1),
    (4, "eight_note", 1),
    (3, "eight_note", 1),  # takt 7
    (2, "eight_note", 1.5),
    (2, "sixteenth_note", 1),
    (5, "quarter_note", 1.5),
    (0, "eight_note", 1),  # takt 8
    (2, "quarter_note", 1),
    (1, "quarter_note", 1),
    (0, "quarter_note", -1),  # koniec zwrotki
    (2, "quarter_note", 1),
    (2, "quarter_note", 1.5),
    (4, "eight_note", 1),                  # takt9
    (4, "eight_note", 1),
    (3, "eight_note", 1),
    (3, "half_note", 1),  # takt 10
    (4, "eight_note", 1.5),
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
        sleep(notes[note]/1000)
    else:
        Beep(sounds[value], int(notes[note]*multiplier))
