from midiutil import MIDIFile
from Drums import Drums

track    = 0
channel  = 9
time     = 0    # In beats
duration = 1    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(2)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)
MyMIDI.addProgramChange (track, channel, time, 115)

for i, sound in enumerate (Drums):
    MyMIDI.addNote(track, channel, sound.value, time + i, duration, volume)


degrees = [60, 62, 64, 65, 67]  # MIDI note number
time = 0
track = 1
channel = 0

MyMIDI.addProgramChange (track, channel, time, 30)

pitchShift = int (input ("Pitch Shift: "))

degrees = [x + pitchShift for x in degrees]

for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)