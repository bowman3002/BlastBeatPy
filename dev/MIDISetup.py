from midiutil import MIDIFile

class MIDISetup:

    def __init__(self, outputFileName):
        self.outputFileName = outputFileName

    def __enter__(self):
        self.midi = MIDIFile(2)  # One track, defaults to format 1 (tempo track is created
        return self.midi

    def __exit__(self, type, value, traceback):
        with open("{}.mid".format(self.outputFileName), "wb") as output_file:
            self.midi.writeFile(output_file)

