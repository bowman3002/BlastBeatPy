'''
opt:
    pitches: {int, [char]} Key: the value of each pitch, Value: keyList
'''

def Pentatonic (seed, onValue, **opt):
    index = 0
    while True:
        note = []
        for pitch, keyList in opt["pitches"].items ():
            if seed[index % len (seed)] in keyList:
                note = [pitch]
                break
        yield note
        index += 1