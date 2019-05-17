from midiutil import MIDIFile
from MIDISetup import MIDISetup
from BeatGenerator import BasicBeat, FillIn, HiHat
from PitchGenerator import Pentatonic
from Instrument import Drums, Pitch
import sys

def getKeyList (instrument):
    ''' e t a o n i s r h l d c m u f p g w y b v k j x q z '''
    switcher = {
        Drums.bass_drum: ['e', 'o', 's', 'l', 'u', 'p', 'y', 'k', 'q', 'd'],
        Drums.closed_hi_hat: ['t', 'i', 'r', 'd', 'm', 'g', 'b', 'x', 'z'],
        Drums.snare: ['a', 'n', 'h', 'c', 'f', 'w', 'v', 'j', 'i'],
        "Pentatonic": {Pitch.C.value: ['e', 'i', 'd', 'p', 'v', 'z'],
                    Pitch.D.value: ['t', 's', 'c', 'g', 'k'],
                    Pitch.E.value: ['a', 'r', 'm', 'w', 'j'],
                    Pitch.G.value: ['o', 'h', 'u', 'y', 'x'],
                    Pitch.A.value: ['n', 'l', 'f', 'b', 'q']
                    }
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

            ''' Guitar '''
            midi.addProgramChange(1, 0, 0, 30)


        pitchShift = int (input ("Pitch Shift: "))



        ''' Drums '''
        closed_hit_hat = BasicBeat(data, Drums.closed_hi_hat.value, keyList = getKeyList (Drums.closed_hi_hat))
        snare = BasicBeat(data, Drums.snare.value, keyList = getKeyList (Drums.snare))
        bass_drum = BasicBeat(data, Drums.bass_drum.value, keyList = getKeyList (Drums.bass_drum))
        fillIn = FillIn (data, Drums.fillIn.value)
<<<<<<< HEAD

        ''' Pitch '''
        pentatonic = Pentatonic (data, 0, pitches = getKeyList ("Pentatonic"))
        
        generators = [closed_hit_hat, snare, bass_drum, fillIn]
=======
        hiHat = HiHat(data, [], cooldown=1, keylist=['a', 'i'], default=Drums.open_hi_hat.value, closed=Drums.closed_hi_hat.value)

        generators = [hiHat, snare, bass_drum, fillIn]
>>>>>>> 1046c62ecb4c7daf93516b015d8c7e445a749a00
        for beat in range(0, int(maxTime / subdivision)):
            time = beat * subdivision

            for generator in generators:
                notes = next(generator)
                for note in notes:
                    midi.addNote(track, channel, note, time, duration, volume)
            notes = next (pentatonic)
            for note in notes:
                midi.addNote (1, 0, note + pitchShift, time, duration, volume)
            


if __name__ == "__main__":
    main(sys.argv)
