from midiutil import MIDIFile

track    = 0
channel  = 9
time     = 0    # In beats
duration = 1    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTrackName(track, 0, "Bass")
MyMIDI.addProgramChange(track, 9, 0, 30)
MyMIDI.addTempo(track, time, tempo)

for i in range(33, 81):
    MyMIDI.addNote(track, channel, i, time + i, duration, volume)

with open("BlastBeat.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
