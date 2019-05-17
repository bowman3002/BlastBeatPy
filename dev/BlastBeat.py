from midiutil import MIDIFile
from MIDISetup import MIDISetup
from BeatGenerator import BasicBeat
import sys

def main(argv):
    with MIDISetup(sys.argv[1]) as midi:
        with open(sys.argv[2], "r") as file:
            data        = file.read().replace('\n', '')
            track       = 0
            channel     = 9
            maxTime     = int(sys.argv[3])  # In beats
            duration    = 1            # In beats
            tempo       = 60           # In BPM
            volume      = 100          # 0-127, as per the MIDI standard
            subdivision = 0.125        # 32nd notes

            midi.addTempo(track, 0, tempo)
            midi.addProgramChange(track, 9, 0, 30)

            generators = []
            for beat in range(0, int(maxTime / subdivision)):
                time = beat * subdivision

                for generator in generators:
                    notes = next(generator)
                    for note in notes
                        midi.addNote(track, channel, note, time, duration, volume)


if __name__ == "__main__":
    main(sys.argv)
