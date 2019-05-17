import sys
import BeatGenerator
from midiutil import MIDIFile

seed = sys.argv[1]
track    = 0
channel  = 9
maxTime  = 60    # In beats
duration = 1    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard
subdivision = 4

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTrackName(track, 0, "Bass")
MyMIDI.addProgramChange(track, 9, 0, 0)
MyMIDI.addTempo(track, 0, tempo)

generator = BeatGenerator.BasicBeat(seed, 56, ['a', 'b'], -1, 56)
generator2 = BeatGenerator.BasicBeat(seed, 40, ['b', 'd'], -1, 42)

for i in range(0, maxTime * subdivision):
    time = i / subdivision
    value = next(generator)
    value2 = next(generator2)
    if value != -1:
        MyMIDI.addNote(track, channel, value, time, duration, volume)

    if value2 != -1:
        MyMIDI.addNote(track, channel, value2, time, duration, volume)

with open("BlastBeat.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
