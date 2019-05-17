from midiutil import MIDIFile
from MIDISetup import MIDISetup
from BeatGenerator import BasicBeat, FillIn, HiHat
from PitchGenerator import BasicPitch
from Instrument import Drums, Pitch
import sys

def spreadNote (keys):
    letters = ['e', 't', 'a', 'o', 'n', 'i', 's', 'r', 'h', 'l', 'd', 'c', 'm', 'u', 'f', 'p', 'g', 'w', 'y', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
    
    tmpList = []
    for i in range (0, len (keys)):
        tmpList.append ([])

    for i in range (0, len (letters)):
        tmpList[i % len (keys)].append (letters[i])

    keyList ={}
    for i in range (0, len (tmpList)):
        keyList[keys[i].value] = tmpList[i]

    return keyList

def getKeyList (instrument):
    ''' e t a o n i s r h l d c m u f p g w y b v k j x q z '''
    switcher = {
        Drums.bass_drum: ['e', 'o', 's', 'l', 'u', 'p', 'y', 'k', 'q', 'd'],
        Drums.closed_hi_hat: ['t', 'i', 'r', 'd', 'm', 'g', 'b', 'x', 'z'],
        Drums.snare: ['a', 'n', 'h', 'c', 'f', 'w', 'v', 'j', 'i'],
    }
    return switcher.get (instrument, [])

def main(outputFile, inputFile, bpm, songLength, subdivision, pitchShift, scale):
    print (pitchShift)
    print (scale)
    with MIDISetup(outputFile) as midi:
        with open(inputFile, "r") as file:
            data        = file.read().replace('\n', '').replace (' ', '')
            track       = 0
            channel     = 9
            maxTime     = int(songLength)  # In beats
            duration    = 1            # In beats
            tempo       = int (bpm)           # In BPM
            volume      = 100          # 0-127, as per the MIDI standard

            midi.addTempo(track, 0, tempo)
            midi.addProgramChange(track, 9, 0, 30)

            ''' Guitar '''
            guitar = 30 if scale == "p" else 26
            midi.addProgramChange(1, 0, 0, guitar)

        ''' Drums '''
        closed_hit_hat = BasicBeat(data, Drums.closed_hi_hat.value, keyList = getKeyList (Drums.closed_hi_hat))
        snare = BasicBeat(data, Drums.snare.value, keyList = getKeyList (Drums.snare))
        bass_drum = BasicBeat(data, Drums.bass_drum.value, keyList = getKeyList (Drums.bass_drum))
        fillIn = FillIn (data, Drums.fillIn.value)
        hiHat = HiHat(data, [], cooldown=1, keylist=['a', 'i'], default=Drums.open_hi_hat.value, closed=Drums.closed_hi_hat.value)

        ''' Pitch '''
        #pentatonic = Pentatonic (data, 0, pitches = getKeyList ("Pentatonic"))
        #blues = Pentatonic (data, 0, pitches = spreadNote ([Pitch.C, Pitch.D, Pitch.Eb, Pitch.E, Pitch.G, Pitch.A]))
        pitches = [Pitch.C, Pitch.D, Pitch.E, Pitch.G, Pitch.A]
        if scale == "b":
            pitches.insert (2, Pitch.Eb)
        guitar = BasicPitch (data, 0, pitches = spreadNote (pitches))

        generators = [hiHat, snare, bass_drum, fillIn]
        for beat in range(0, int(maxTime / subdivision)):
            time = beat * subdivision

            for generator in generators:
                notes = next(generator)
                for note in notes:
                    midi.addNote(track, channel, note, time, duration, volume)

            notes = next (guitar)
            for note in notes:
                midi.addNote (1, 0, note + pitchShift, time, duration, volume)
            


# if __name__ == "__main__":
#     main(sys.argv)
