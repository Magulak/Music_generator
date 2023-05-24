import pretty_midi
# dataset: https://www.kaggle.com/datasets/soumikrakshit/classical-music-midi
# https://www.tensorflow.org/tutorials/audio/music_generation?hl=pl

path = r'G:\Skrypty\Scripts\Music_Generating\Music_generator\archive\albeniz\alb_esp1.mid'


class ExtractAndSortData:
    def __init__(self, file_path):

        self.midi_data = pretty_midi.PrettyMIDI(file_path)
        self.show_instrument_names_and_x_notes(100)





    def show_instrument_names_and_x_notes(self,ammount_of_notes):

        print('Amount of instruments::', len(self.midi_data.instruments))
        for instrument in self.midi_data.instruments:
            instrument_name = pretty_midi.program_to_instrument_name(instrument.program)
            print('Instrument name:', instrument_name)


            for i, note in enumerate(instrument.notes[:ammount_of_notes]):
                note_name = pretty_midi.note_number_to_name(note.pitch)
                duration = note.end - note.start
                print(f'{i}: pitch={note.pitch}, note_name={note_name},'
                      f' duration={duration:.3f}')

    def sort_notes(self):
        """ this function sorts notes inside instrument.notes, basing on note_start_time """
        pass


ExtractAndSortData(path)
