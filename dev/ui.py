from tkinter import *
from BlastBeat import main as BlastBeat

def main ():
    root = Tk ()

    pitchShiftText = Label (root, text = "Pitch Shift: ")
    pitchShiftEntry = Entry (root)

    outputFileText = Label (root, text = "Output Filename: " )
    outputFileEntry = Entry (root)

    inputFileText = Label (root, text = "Input Filename: " )
    inputFileEntry = Entry (root)

    bpmText = Label (root, text = "BPM: " )
    bpmEntry = Entry (root)

    songLengthText = Label (root, text = "SongLength (ie. 30 for 60 bpm = 30 secs): " )
    songLengthEntry = Entry (root)

    subdivisionText = Label (root, text = "Subdivision: " )
    subdivisionEntry = Entry (root)

    scale = StringVar ()
    scale.set ("p")
    Radiobutton (root, text = "Pentatonic", variable = scale, value = "p").pack ()
    Radiobutton (root, text = "Blues", variable = scale, value = "b").pack ()

    button = Button (root, text = "Blast Beat, Yo!", command = lambda: BlastBeat (outputFileEntry.get (), inputFileEntry.get (), (bpmEntry.get ()),
                                                                             (songLengthEntry.get ()),  (subdivisionEntry.get ()),
                                                                             (pitchShiftEntry.get ()), scale.get ()))

    pitchShiftText.pack ()
    pitchShiftEntry.pack ()
    outputFileText.pack ()
    outputFileEntry.pack ()

    inputFileText.pack ()
    inputFileEntry.pack ()

    bpmText.pack ()
    bpmEntry.pack ()

    songLengthText.pack ()
    songLengthEntry.pack ()

    subdivisionText.pack ()
    subdivisionEntry.pack ()
    button.pack ()
    root.mainloop ()

if __name__ == "__main__":
    main()
