from winsound import Beep
from time import sleep
from math import pow

# c d e f g a h
# step = pow(2, 1/6) (1/12 for eg. a4 to a#4)
# a4 = 440, so a4 is the 27th sound (?)
# so it's c1 * step**26 (?)
# ignore what's above, basically 440hz is the 1st sound on the staff (the one with added line)
# ... i think

root = pow(2, 1/12)
bpm = 116
base_sound = 329.6276  # E4
quarter_note = 0.5
sounds = [base_sound]

# E4 = 329 F5 = 698  == 14 semitones (bases)
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
#   1   3   5   7 8   10    12 13    15    17    19 20    22    24    26 27
#     2   4   6      9   11       14    16    18       21    23    25       28
#   1 2 3 4 5 6 0 1  2 3 4  5  6  0  1  2  3  4  5  6  0  1  2   3  4  5  6  0


for i in range(1, 14):
    sounds.append(sounds[i-1] * root)
s = [int(x) for x in sounds]
print(s)
sounds = [int(x) for x in sounds]
temp_sounds = []
for i in range(1, len(sounds)):
    if i % 7 in [2, 4, 6] and i < 13:
        continue
    elif i % 7 in [0, 2, 4] and i >= 13:
        print(i)
        continue
    else:
        temp_sounds.append(sounds[i])
sounds[-1] = 698
sounds = [int(base_sound)] + temp_sounds
print(sounds)

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
