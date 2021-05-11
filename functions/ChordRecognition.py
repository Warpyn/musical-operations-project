from Note import Note

from functions.IntervalRecognition import *
from functions.OrderNotes import *

# ---------- Chord Recognition -------------

## Create Array of Intervals in a Chord
def createChordIntervalSet(chord):
    # done using SimpleIntervals
    ordered_chord = orderNotes(chord)
    # print(printNoteArray(ordered_chord))
    interval_set = []
    for i in ordered_chord:
        tempInterval = findSimpleInterval(ordered_chord[0],i)
        # print(ordered_chord[0].getFullName()+" and "+i.getFullName()+" = "+tempInterval)
        interval_set.append(tempInterval)
    return interval_set

## Chord Recognition Aggregate
def identifyChord(note_set):
    interval_set = createChordIntervalSet(note_set)
    ordered_notes = orderNotes(note_set)
    chord_str = ordered_notes[0].note_base + ordered_notes[0].note_accidental
    if interval_set.count("m3")>0:
        if interval_set.count("d5")>0:
            if interval_set.count("m7")>0:
                chord_str += "m7b5"
            elif interval_set.count("d7")>0:
                chord_str += "dim7"
            else:
                chord_str += "dim"
        else:
            chord_str += "m"
        if interval_set.count("P5")>0:
            if interval_set.count("m7")>0:
                chord_str += "7"
            elif interval_set.count("M7")>0:
                chord_str += "M7"
    elif interval_set.count("M3")>0:
        if interval_set.count("A5")>0:
            chord_str += "+"
        if interval_set.count("P5")>0:
            if interval_set.count("m7"):
                chord_str += "7"
        if interval_set.count("M7")>0:
            chord_str += "maj7"
    else:
        chord_str += " n.c."
    return chord_str

def findInversionNum(note_set):
    new_order = orderNotes(note_set)
    for i in range(0, len(note_set)):
        if note_set[0].equals(new_order[i]):
            inversionNum = i
    return inversionNum

def findChordandInversion(notes):
    num = findInversionNum(notes)
    if num == 0:
        return "Root Position of "+identifyChord(notes)
    else:
        return "Inversion #"+str(num)+" of "+identifyChord(notes)
