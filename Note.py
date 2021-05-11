class Note:
    def __init__(self, note_base, note_accidental, note_octave):
        self.note_base = note_base
        self.note_accidental = note_accidental

        all_note_bases = ["C", "D", "E", "F", "G", "A", "B"]
        all_bases_values = [0, 2, 4, 5, 7, 9, 11]
        all_accidentals = ["bbb", "bb", "b", "", "#", "##", "###"]
        all_accidental_values = [-3, -2, -1, 0, 1, 2, 3]
        self.simple_pitch_value = (all_bases_values[all_note_bases.index(note_base)] + all_accidental_values[all_accidentals.index(note_accidental)])%12

        if note_octave == None:
            self.note_octave = 4
        else:
            self.note_octave = note_octave

        self.full_pitch_value = (12*self.note_octave)+(all_bases_values[all_note_bases.index(note_base)] + all_accidental_values[all_accidentals.index(note_accidental)])

    def augment(self):
        all_accidentals = ["bbb", "bb", "b", "", "#", "##", "###"]
        all_note_bases = ["C", "D", "E", "F", "G", "A", "B"]
        all_bases_values = [0, 2, 4, 5, 7, 9, 11]
        all_accidental_values = [-3, -2, -1, 0, 1, 2, 3]
        current_index = all_accidentals.index(self.note_accidental)

        if current_index == len(all_accidentals) - 1:
            current_note_index = all_note_bases.index(self.note_base)
            if current_note_index == len(all_note_bases)-1:
                self.note_octave += 1
            self.note_base = all_note_bases[(current_note_index + 1)%len(all_note_bases)]
            self.note_accidental = ""

            self.simple_pitch_value = (all_bases_values[all_note_bases.index(self.note_base)] + all_accidental_values[all_accidentals.index("")])%12
            self.full_pitch_value = (12*self.note_octave)+(all_bases_values[all_note_bases.index(self.note_base)] + all_accidental_values[all_accidentals.index("")])

        else:
            next_accidental = all_accidentals[(current_index + 1)%len(all_accidentals)]
            self.note_accidental = next_accidental

            self.simple_pitch_value = (self.simple_pitch_value + 1)%12
            self.full_pitch_value += 1



    def diminish(self):
        all_accidentals = ["bbb", "bb", "b", "", "#", "##", "###"]
        all_note_bases = ["C", "D", "E", "F", "G", "A", "B"]
        all_bases_values = [0, 2, 4, 5, 7, 9, 11]
        all_accidental_values = [-3, -2, -1, 0, 1, 2, 3]
        current_index = all_accidentals.index(self.note_accidental)

        if current_index == 0:
            current_note_index = all_note_bases.index(self.note_base)
            if current_note_index == 0:
                self.note_octave -= 1
            self.note_base = all_note_bases[(current_note_index - 1)%len(all_note_bases)]
            self.note_accidental = ""

            self.simple_pitch_value = (all_bases_values[all_note_bases.index(self.note_base)] + all_accidental_values[all_accidentals.index("")])%12
            self.full_pitch_value = (12*self.note_octave)+(all_bases_values[all_note_bases.index(self.note_base)] + all_accidental_values[all_accidentals.index("")])

        else:
            next_accidental = all_accidentals[(current_index - 1)%len(all_accidentals)]
            self.note_accidental = next_accidental

            self.simple_pitch_value = (self.simple_pitch_value - 1)%12
            self.full_pitch_value -= 1

    def getFullName(self):
        return (self.note_base + self.note_accidental + str(self.note_octave))

    def equals(self, note2):
        return self.note_base == note2.note_base and self.note_accidental == note2.note_accidental and self.note_octave == note2.note_octave

    def simpleEquals(self, note2):
        return self.note_base == note2.note_base and self.note_accidental == note2.note_accidental 
