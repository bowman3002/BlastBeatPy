from midiutil import MIDIFile
from Drums import Drums

track    = 0
channel  = 9
time     = 0    # In beats
duration = 1    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for sound in Drums:
    MyMIDI.addNote(track, channel, sound.value, time, duration, volume)
    time += 1

with open("drums.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
