from Note import Note

from functions.ChordRecognition import *
from functions.IntervalRecognition import *
from functions.OrderNotes import *

# ---------- Music Set Theory ----------

# set without transposing to 0
def createSet(temp):
    notes_set = temp.copy()
    # remove duplicates
    for i in range(1, len(notes_set)):
        if i>len(notes_set)-1:
            break
        for j in range(0, i):
            if notes_set[i].simpleEquals(notes_set[j]):
                notes_set.remove(notes_set[i])
                i = i-1
                break

    # note values create
    note_values = []
    for i in notes_set:
        note_values.append(i.simple_pitch_value)

    # make set
    clock_values = ["0","1","2","3","4","5","6","7","8","9","T","E"]
    set_string = ""
    for i in range(0, len(note_values)):
        set_string = set_string+clock_values[note_values[i]]

    return set_string

# prime version of the test (transposed so first note is at 0)
def createPrimeSet(temp):
    notes_set = temp.copy()
    # remove duplicates
    for i in range(1, len(notes_set)):
        if i>len(notes_set)-1:
            break
        for j in range(0, i):
            if notes_set[i].simpleEquals(notes_set[j]):
                notes_set.remove(notes_set[i])
                i = i-1
                break

    # note values create
    note_values = []
    for i in notes_set:
        note_values.append(i.simple_pitch_value)
    note_values.sort()
    translationMod = note_values[0]
    for i in range(0,len(note_values)):
        note_values[i] = note_values[i] - translationMod

    # make set
    clock_values = ["0","1","2","3","4","5","6","7","8","9","T","E"]
    set_string = ""
    for i in range(0, len(note_values)):
        set_string = set_string+clock_values[note_values[i]]

    return set_string

## Set Theory - Interval Vector (with an actual set as input)
def createIntervalVector(set_str):
    clock_values = ["0","1","2","3","4","5","6","7","8","9","T","E"]
    intervalCounts = [0, 0, 0, 0, 0, 0] # [1s, 2s, 3s, 4s, 5s, 6s] index: 0 to 5

    try:
        for i in range(0, len(set_str)-1):
            for j in range(i+1, len(set_str)):
                pitch_dist = int(set_str[j]) - int(set_str[i])
                if pitch_dist > 6:
                    intervalCounts[12-pitch_dist-1] += 1
                else:
                    intervalCounts[pitch_dist-1] += 1

        intervalVector = "<"
        for k in intervalCounts:
            intervalVector += str(k)
        intervalVector += ">"

        return intervalVector

    except ValueError:
        print("Invalid Input. Sets are defined with the characters 0-9, T, and E.")
        return ""

## Invert Sets on the Clock Diagram
def invertSet(set_str, axis_str):
    # inverts a set of pitches about an axis on the clock diagram
    clock_values = ["0","1","2","3","4","5","6","7","8","9","T","E"]
    invertedSet = ""

    if float(axis_str)%1 == 0.0:
        axis_num = int(axis_str)
    else:
        axis_num = float(axis_str)

    try:
        for i in range(0, len(set_str)):
            x = clock_values.index((set_str[i]))
            invertedSet += clock_values[(int(2*axis_num)-x)%12]

        return invertedSet

    except ValueError:
        print("Invalid Input. Sets are defined with the characters 0-9, T, and E.")
        return ""
