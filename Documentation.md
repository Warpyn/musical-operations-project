# The Note Object
(Note.py)

## Initilization / Creation
`Note(note_base, note_accidental, note_octave)`

- note_base (string)
  - one of the following: "A", "B", "C", "D", "E", "F", "G"
- note_accidental (string)
  - one of the following: "bbb", "bb", "b", "", "#", "##", "###"
- note_octave (number)
  - any integer greater than zero

`Note("C","",4) # this represents middle C`

## Attributes
These values can be retrieved by writing a period and the attribute name following the Note object itself or as a variable.

- Note.note_base
- Note.note_accidental
- Note.note_octave
  - defaults to `4` if no octave is given
- Note.simple_pitch_value
  - returns an integer value between 0-11 (equivalent to C-B) that represents the pitch within one octave of the C major scale
- Note.full_pitch_value
  - returns an integer value greater than 0 that represents the value of the pitch along with the octave of the Note. similar to MIDI values for pitches.
  - ex. `Note("C","",4).full_pitch_value` would yield `48`

## Object Functions
These functions can be called by writing a period and the function name with any necessary parameters in parantheses.

- Note.augment()
  - raises the Note's pitch by one semitone / raises the accidental of the note only, not the base of the note. augmenting a Note with a `###` accidental will change the base of the note to the next higher base and reset the accidental to `""`.
- Note.diminish()
  - lowers the Note's pitch by one semitone / lowers the accidental of the note only, not the base of the note. diminishing a Note with a `bbb` accidental will change the base of the note to the next lower base and reset the accidental to `""`.
- Note.getFullName()
  - returns a string that describes the Note object.
  - ex. `Note("C","#",3).getFullName()` would return `"C#3"`.
- Note1.equals(Note2)
  - returns a boolean describing whether Note1 and Note2 have the exact same note base, accidental, *and octave*.
- Note1.simpleEquals(Note2)
  - returns a boolean describing whether Note1 and Note2 have the exact same note base and accidental only. *the octaves of both notes are not considered*.

# Interval Recognition
(IntervalRecognition.py)

## Primary Functions
- findFullInterval(note1, note2)
  - Paramaters: two Note objects
  - returns a string which is the interval between note1 and note2 including the octave distance. the function finds the lower note between the two notes and uses that for the base note of the interval.
  - ex. `findFullInterval( Note("D","",4) , Note("C","",3) )` will evaluate to the string `"M9"` (a major 9th interval)
- findSimpleInterval(note1, note2)
  - Paramaters: two Note objects
  - returns a string which is the interval between note1 and note2 *disregarding octave distance*. the function finds the lower note between the two notes and uses that for the base note of the interval.
  - ex. `findFullInterval( Note("D","",4) , Note("C","",3) )` will evaluate to the string `"M2"` (a major 2nd interval)


## Supporting Functions
These functions can be called by a user, but their main purpose was to improve efficiency for the primary functions.

- simple_note_base_distance(note1, note2)
  - Paramaters: two Note objects
  - returns a positive integer value which is the distance between two note bases *disregarding octave* (the distance of the interval). this also assumes that note2 is higher in pitch than note1.
- qualityOfInterval(note1, note2)
  - Parameters: two Note objects
  - returns a string that describes the quality of the interval between note1 and note2, assuming note2 is higher in pitch.
  - all possible qualities are the following for perfect intervals: "dd", "d", "P", "A", "AA"
  - all possible qualities are the following for imperfect intervals: "dd","d","m","M","A","AA"
- octaveModifier(note1, note2)
  - Paramaters: two Note objects
  - returns a positive integer value that is the number of full octaves between note1 and note2, assuming note2 is higher in pitch.


# Ordering Notes and Logistics
(OrderNotes.py)

## Primary Functions
- printNoteArray(arr)
  - Parameters: one Python list of Note objects
  - returns a string that lists the Note objects in the Python list's original order.
  - ex.`printNoteArray([Note("F","#",2), Note("A","",4), Note("C","",3)])` would return the string `"F#2 A4 C3"`
- orderNotes(arr)
  - Parameters: one Python list of Note objects
  - returns a Python list of Note objects that reorders the original list of Notes from lowest to highest in terms of pitch.
  - ex. `orderNotes([Note("F","#",2), Note("A","",4), Note("C","",3)])` would return the Python list `[Note("F","#",2), Note("C","",3), Note("A","",4)]`

## Supporting Functions
These functions can be called by a user, but their main purpose was to improve efficiency for the primary functions.

- compareNoteBases(note1, note2)
  - Paramaters: two Note objects
  - returns an integer value that describes the pitch of note2 relative to note1 *ignoring accidentals (only the note base and its octave value)*. so, if note2>note1, then the function returns `1`. if note2<note1, then the function returns `-1`. if note2=note1, the function returns `0`.

# Chord Recognition
(ChordRecognition.py)

## Primary Functions
- identifyChord(note_set)
  - Paramaters: a Python list of Note objects
  - returns a string that describes the chord found from the notes in the given list. this function recognizes major/minor/augmented/diminished chords as well as dominant/minor/major 7th chords. it also *uses the lowest note in the list as the root of the chord*.
  - ex. `identifyChord([Note("A","",3), Note("C","#",5), Note("E","#",4)])` would yield `"A+"` (an A augmented chord)
- findInversionNum(note_set)
  - Paramaters: a Python list of Note objects
  - returns an integer value which is the inversion number of the given set of notes based on the chord they produce.
  - ex. `findInversionNum([Note("A","",2), Note("D","",2), Note("F","",2)])` would return `2`
- findChordandInversion(note_set)
  - Paramaters: a Python list of Note objects
  - returns a string that describes the chord and its inversion from the inputted list of Note objects
  - ex. `findChordandInversion([Note("A","",2), Note("D","",2), Note("F","",2)])` would return `"Inversion #2 of Dm"`

## Supporting Functions
These functions can be called by a user, but their main purpose was to improve efficiency for the primary functions.

- createChordIntervalSet(chord)
  - Parameters: a Python list of Note objects
  - returns a Python list of strings that describe the intervals of each note in the chord, using the first note as the root of the chord/interval
  - ex. `createChordIntervalSet([Note("C","b",4), Note("B","",5), Note("E","b",6)])` would return the list `['P1', 'A7', 'M3']`

# Musical Set Theory
(MusicalSetTheory.py)

- createSet(note_set)
  - Paramaters: a Python list of Note objects
  - returns a string that describes the set of notes using the values of a clock diagram with the values 0-9,T,E with 0 representing the pitch value of C.
  - ex. `createSet([Note("E","",2), Note("G","#",3), Note("B","",2)])` would return `"48E"`
- createPrimeSet(note_set)
  - Paramaters: a Python list of Note objects
  - returns a string that describes the set of notes using clock diagram values (0-9,T,E), but *the set is transposed such that the lowest note in the set becomes 0*.
  - ex. `createSet([Note("E","",2), Note("G","#",3), Note("B","",2)])` would return `"047"`
- createIntervalVector(set_str)
  - Paramaters: a string that represents a musical set (a string that only contains the clock diagram characters: 0-9,T,E)
  - returns a string that represents the interval vector of the given set. the interval vector shows how many 1-semitone intervals through 6-semitone intervals there are between all possible interval combinations.
  - ex. `createIntervalVector("047")` would yield `"<001110>"`, meaning there is one 3-semitone interval, one 4-semitone interval, and one 5-semitone interval.
- invertSet(set_str, axis_str)
  - Paramaters: a string that represents a musical set, and *a string* that represents the axis of inversion/reflection.
  - returns a string which is the inverted musical set using the given set and axis on the clock diagram [(shown in Sideway's video on the clock diagram)](https://youtu.be/oGeBem72R3Y).
  - to denote an axis that passes through two pitches on the clock diagram, either value will yield a correct result. for example, for the 0-6 axis, either ``"0"`` or ``"6"`` would be valid options for axis_str.
  - to denote an axis that passes [between pitches on the clock diagram](https://youtu.be/oGeBem72R3Y?t=274), pick a value between the two pitches as the value for axis_str. the Cmaj9 example in the Sideways video shows an axis that passes between 4 and 5 as well as T and E. in this case, either `"4.5"` or `"10.5"` would be valid optinos for axis_str.
