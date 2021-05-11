from Note import *

from functions.ChordRecognition import *
from functions.OrderNotes import *
from functions.IntervalRecognition import *
from functions.MusicalSetTheory import *

note1 = Note("B","",4)
note2 = Note("E","",2)
note3 = Note("G","",5)
note4 = Note("D","#",3)
test_chord = [note1, note2, note3, note4]
print("The given chord is "+findChordandInversion(test_chord)+".")
print()

print("The given chord can also be represented as a set, "+createSet(test_chord)+", or its prime form, "+createPrimeSet(test_chord)+".")
print()
print("The interval vector for this set is "+createIntervalVector(createPrimeSet(test_chord))+".")
