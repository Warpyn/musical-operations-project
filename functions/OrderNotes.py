from Note import Note

# ----------- Ordering Notes and Logistics ----------- 

## Reorder Notes From Low to High
def compareNoteBases(note1, note2):
    # outputs 1 if note2>note1, and outputs -1 if note2<note1
    # about note2 relative to note1
    all_note_bases = ["C", "D", "E", "F", "G", "A", "B"]
    all_bases_values = [0, 2, 4, 5, 7, 9, 11]
    note1base_value = (all_bases_values[all_note_bases.index(note1.note_base)])+(12*note1.note_octave)
    note2base_value = (all_bases_values[all_note_bases.index(note2.note_base)])+(12*note2.note_octave)
    if note2base_value > note1base_value:
        return 1
    elif note2base_value < note1base_value:
        return -1
    else:
        return 0

def orderNotes(arr):
    all_notes = []
    for i in arr:
        all_notes.append(i)
    try:
        # sorting Note objects using Insertion Sort
        for i in range(1, len(all_notes)):
            note_current = all_notes[i]
            j = i-1

            while j >= 0 and compareNoteBases(all_notes[j], note_current) < 0:
                    # move current note left when it is lower than the previous note

                    all_notes[j + 1] = all_notes[j]
                    j -= 1
            all_notes[j + 1] = note_current

        return all_notes

    except TypeError:
        print("ERROR: Incorrect Input File Type. Correct Input File Type: Array of Note objects")
        return []

def printNoteArray(arr):
    str = ""
    for i in arr:
        str += i.getFullName()
        if arr.index(i) != len(arr)-1:
            str += " "
    return str
