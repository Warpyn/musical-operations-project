from Note import Note

# ---------- Interval Recognition ----------

def simple_note_base_distance(note1, note2):
    # assuming base2 is higher
    # within one octave ONLY
    base1 = note1.note_base
    base2 = note2.note_base
    all_note_bases = ["C", "D", "E", "F", "G", "A", "B"]
    index_distance = all_note_bases.index(base2) - all_note_bases.index(base1)
    if index_distance >= 0:
        # C and C returns 1, not 8
        return int(index_distance + 1)
    else:
        return int(index_distance + 8)

def qualityOfInterval(note1, note2):
    # assuming note2 is higher
    all_note_bases = ["C", "D", "E", "F", "G", "A", "B"]
    major_scale_values = [0, 2, 4, 5, 7, 9, 11] # will also be used for major scale intervals
    all_accidentals = ["bbb", "bb", "b", "", "#", "##", "###"]
    all_accidental_values = [-3, -2, -1, 0, 1, 2, 3]

    note_base_distance = simple_note_base_distance(note1, note2)
    scale_interval_value = major_scale_values[(note_base_distance - 1)%7]

    note1val = major_scale_values[all_note_bases.index(note1.note_base)] + all_accidental_values[all_accidentals.index(note1.note_accidental)]
    note2val = major_scale_values[all_note_bases.index(note2.note_base)] + all_accidental_values[all_accidentals.index(note2.note_accidental)]

    if note2val < note1val:
        simple_pitch_distance = note2val - note1val + 12
    else:
        simple_pitch_distance = note2val - note1val

    difference_from_majorScale = simple_pitch_distance - scale_interval_value

    if note_base_distance == 1 or note_base_distance == 4 or note_base_distance == 5:
        # perfect intervals
        perfect_qualities = ["dd", "d", "P", "A", "AA"]
        return perfect_qualities[difference_from_majorScale + perfect_qualities.index("P")]
    else:
        # major imperfect intervals
        imperfect_qualities = ["dd","d","m","M","A","AA"]
        return imperfect_qualities[difference_from_majorScale + imperfect_qualities.index("M")]

def octaveModifier(note1, note2):
    # assuming note2 is higher
    all_note_bases = ["C", "D", "E", "F", "G", "A", "B"]
    all_bases_values = [0, 2, 4, 5, 7, 9, 11]

    base1_full_pitch_value = all_bases_values[all_note_bases.index(note1.note_base)] + (note1.note_octave*12)
    base2_full_pitch_value = all_bases_values[all_note_bases.index(note2.note_base)] + (note2.note_octave*12)
    base_difference = base2_full_pitch_value - base1_full_pitch_value
    numOctaves = (base_difference-(base_difference%12))/12
    return int(numOctaves)

def findFullInterval(note1, note2):
    # this method finds the lower note, and then uses that as the root of the interval.
    all_note_bases = ["C", "D", "E", "F", "G", "A", "B"]
    all_bases_values = [0, 2, 4, 5, 7, 9, 11]
    absolute_pitch_distance = note2.full_pitch_value - note1.full_pitch_value

    if absolute_pitch_distance >= 0: # note 2 is higher than note 1
        return qualityOfInterval(note1, note2) + str(simple_note_base_distance(note1, note2)+(7*octaveModifier(note1, note2)))
    elif absolute_pitch_distance < 0: # note 1 is higher than note 1
        return qualityOfInterval(note2, note1) + str(simple_note_base_distance(note2, note1)+(7*octaveModifier(note2, note1)))

def findSimpleInterval(note1, note2):
    # this method finds the lower note, and then uses that as the root of the interval.
    all_note_bases = ["C", "D", "E", "F", "G", "A", "B"]
    all_bases_values = [0, 2, 4, 5, 7, 9, 11]
    absolute_pitch_distance = note2.full_pitch_value - note1.full_pitch_value

    if absolute_pitch_distance >= 0: # note 2 is higher than note 1
        return qualityOfInterval(note1, note2) + str(simple_note_base_distance(note1, note2))
    elif absolute_pitch_distance < 0: # note 1 is higher than note 1
        return qualityOfInterval(note2, note1) + str(simple_note_base_distance(note2, note1))
