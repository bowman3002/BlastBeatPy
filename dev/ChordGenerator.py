import random

scale = [36, 38, 40, 41, 43, 45]
cScale = [36, 38, 40, 41, 43, 45, 47]

def makeChords(scale):
    chordDictionary = []
    for root in scale:
        majorChord = [root, root + 4, root + 7]
        minorChord = [root, root + 3, root + 7]
        sus4Chord = [root, root + 5, root + 7]
        sus2Chord = [root, root + 2, root + 7]
        sixChord = [root, root + 4, root + 7, root + 9]
        dom7Chord = [root, root + 4, root + 7, root + 10]

        majorList = majorChord + [x+12 for x in majorChord] + [x+24 for x in majorChord] + [x+36 for x in majorChord]
        minorList = minorChord + [x+12 for x in minorChord] + [x+24 for x in minorChord] + [x+36 for x in minorChord]
        sus4List = sus4Chord + [x+12 for x in sus4Chord] + [x+24 for x in sus4Chord] + [x+36 for x in sus4Chord]
        sus2List = sus2Chord + [x+12 for x in sus2Chord] + [x+24 for x in sus2Chord] + [x+36 for x in sus2Chord]
        sixList = sixChord + [x+12 for x in sixChord] + [x+24 for x in sixChord] + [x+36 for x in sixChord]
        dom7List = dom7Chord + [x+12 for x in dom7Chord] + [x+24 for x in dom7Chord] + [x+36 for x in dom7Chord]

        chordDictionary.append([majorList, minorList, sus4List, sus2List, sixList, dom7List])

    return chordDictionary

def makeChordsInKey(scale):
    chordDictionary = []
    for idx in range(0, len(cScale)):
        majorChord = [scale[idx % len(scale)], scale[(idx + 2) % len(scale)], scale[(idx + 4) % len(scale)]]
        sus4Chord = [scale[idx % len(scale)], scale[(idx + 3) % len(scale)], scale[(idx + 4) % len(scale)]]
        sus2Chord = [scale[idx % len(scale)], scale[(idx + 1) % len(scale)], scale[(idx + 4) % len(scale)]]
        sixChord = [scale[idx % len(scale)], scale[(idx + 2) % len(scale)], scale[(idx + 4) % len(scale)], scale[(idx + 5) % len(scale)]]
        dom7Chord = [scale[idx % len(scale)], scale[(idx + 2) % len(scale)], scale[(idx + 4) % len(scale)], scale[(idx + 6) % len(scale)]]

        majorList = majorChord + [x+12 for x in majorChord] + [x+24 for x in majorChord] + [x+36 for x in majorChord]
        sus4List = sus4Chord + [x+12 for x in sus4Chord] + [x+24 for x in sus4Chord] + [x+36 for x in sus4Chord]
        sus2List = sus2Chord + [x+12 for x in sus2Chord] + [x+24 for x in sus2Chord] + [x+36 for x in sus2Chord]
        sixList = sixChord + [x+12 for x in sixChord] + [x+24 for x in sixChord] + [x+36 for x in sixChord]
        dom7List = dom7Chord + [x+12 for x in dom7Chord] + [x+24 for x in dom7Chord] + [x+36 for x in dom7Chord]

        chordDictionary.append([majorList, sus4List, sus2List, sixList, dom7List])

    return chordDictionary

'''
opt:
    cooldown:int        The amount of beats to wait before playing again
    keylist:[String]    The list of keys which close the hihat
    default:int         The default value to use
    closed:int          The closed value to use
'''
def ChordGenerator(seed, onValue, **opt):
    chordNum = 0
    currentCooldown = 0
    chords = makeChordsInKey(cScale)
    root = 0
    chord = 0
    cooldown = opt['cooldown']
    pitchShift = opt['pitchShift']
    while True:
        if currentCooldown == 0:
            currentCooldown = cooldown
            start = random.randint(0, len(chords[root][chord]) - 5 - 1)
            yield [x+pitchShift for x in chords[root][chord][start:start+5]]
        else:
            yield []
            currentCooldown -= 1
            chordNum = (chordNum + 1) % 8
            if chordNum == 0:
                root = 0
                print("RESET TO ROOT")
            else:
                root = random.randint(0, len(chords) - 1)

            chord = random.randint(0, len(chords[root]) - 1)

