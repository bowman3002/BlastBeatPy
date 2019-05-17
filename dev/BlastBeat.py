from midiutil import MIDIFile
from MIDISetup import MIDISetup
from BeatGenerator import BasicBeat
import sys

def main(argv):
    with MIDISetup(sys.argv[1]) as midi:
        track       = 0
        channel     = 9
        maxTime     = int(sys.argv[2])  # In beats
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
                value = next(generator)
                if value != -1:
                    midi.addNote(track, channel, value, time, duration, volume)


if __name__ == "__main__":
    main(sys.argv)
