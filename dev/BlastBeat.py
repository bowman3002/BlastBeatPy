from midiutil import MIDIFile
from MIDISetup import MIDISetup
from BeatGenerator import BasicBeat, FillIn, HiHat
from Drums import Drums
import sys

def getKeyList (instrument):
    switcher = {
        Drums.bass_drum: ['e', 'o', 's', 'l', 'u', 'p', 'y', 'k', 'q', 'd'],
        Drums.closed_hi_hat: ['t', 'i', 'r', 'd', 'm', 'g', 'b', 'x', 'z'],
        Drums.snare: ['a', 'n', 'h', 'c', 'f', 'w', 'v', 'j', 'i']
    }
    return switcher.get (instrument, [])

def main(argv):
    with MIDISetup(sys.argv[1]) as midi:
        with open(sys.argv[2], "r") as file:
            data        = file.read().replace('\n', '').replace (' ', '')
            track       = 0
            channel     = 9
            maxTime     = int(sys.argv[3])  # In beats
            duration    = 1            # In beats
            tempo       = int (sys.argv[4])           # In BPM
            volume      = 100          # 0-127, as per the MIDI standard
            subdivision = float (sys.argv[5])  # 32nd notes

            midi.addTempo(track, 0, tempo)
            midi.addProgramChange(track, 9, 0, 30)

        closed_hit_hat = BasicBeat(data, Drums.closed_hi_hat.value, keyList = getKeyList (Drums.closed_hi_hat))
        snare = BasicBeat(data, Drums.snare.value, keyList = getKeyList (Drums.snare))
        bass_drum = BasicBeat(data, Drums.bass_drum.value, keyList = getKeyList (Drums.bass_drum))
        fillIn = FillIn (data, Drums.fillIn.value)
        hiHat = HiHat(data, [], cooldown=1, keylist=['a', 'i'], default=Drums.open_hi_hat.value, closed=Drums.closed_hi_hat.value)

        generators = [hiHat, snare, bass_drum, fillIn]
        for beat in range(0, int(maxTime / subdivision)):
            time = beat * subdivision

            for generator in generators:
                notes = next(generator)
                for note in notes:
                    midi.addNote(track, channel, note, time, duration, volume)


if __name__ == "__main__":
    main(sys.argv)
