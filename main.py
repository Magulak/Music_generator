import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pretty_midi

# https://www.tensorflow.org/tutorials/audio/music_generation?hl=pl

# Load MIDI file into PrettyMIDI object
midi_data = pretty_midi.PrettyMIDI(r'G:\Skrypty\Scripts\Music_Generating\Music_generator\archive\albeniz\alb_esp1.mid')

print('Instruments:', len(midi_data.instruments))


for instrument in midi_data.instruments:
    instr = instrument
    instrument_name = pretty_midi.program_to_instrument_name(instrument.program)
    print('Instrument name:', instrument_name)
