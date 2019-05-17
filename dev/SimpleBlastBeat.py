import sys
import BeatGenerator
from midiutil import MIDIFile
from Drums import Drums

def getKeyList (instrument):
    switcher = {
        Drums.bass_drum: ['e', 'o', 's', 'l', 'u', 'p', 'y', 'k', 'q', 'd'],
        Drums.closed_hi_hat: ['t', 'i', 'r', 'd', 'm', 'g', 'b', 'x', 'z'],
        Drums.snare: ['a', 'n', 'h', 'c', 'f', 'w', 'v', 'j', 'i']
    }
    return switcher.get (instrument, [])

seed = "Google News is a news aggregator and app developed by Google. It presents a continuous, customizable flow of articles organized from thousands of publishers and magazines."
track    = 0
channel  = 9
maxTime  = 60    # In beats
duration = 1    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard
subdivision = 4

seed = seed.replace (" ", "")

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTrackName(track, 0, "Drums")
MyMIDI.addProgramChange(track, 9, 0, 0)
MyMIDI.addTempo(track, 0, tempo)

closed_hit_hat = BeatGenerator.BasicBeat(seed, Drums.closed_hi_hat.value, keyList = getKeyList (Drums.closed_hi_hat))
snare = BeatGenerator.BasicBeat(seed, Drums.snare.value, keyList = getKeyList (Drums.snare))
bass_drum = BeatGenerator.BasicBeat(seed, Drums.bass_drum.value, keyList = getKeyList (Drums.bass_drum))

for i in range(0, maxTime * subdivision):
    time = i / subdivision
    value = next(closed_hit_hat)
    value2 = next(snare)
    value3 = next(bass_drum)
    if value != -1:
        MyMIDI.addNote(track, channel, value, time, duration, volume)

    if value2 != -1:
        MyMIDI.addNote(track, channel, value2, time, duration, volume)

    if value3 != -1:
        MyMIDI.addNote(track, channel, value3, time, duration, volume + 5)

with open("BlastBeat.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
