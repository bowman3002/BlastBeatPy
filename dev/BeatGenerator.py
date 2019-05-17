def BasicBeat(seed, onValue, **opt):
    index = 0
    while True:
        yield [onValue] if (seed[index % len(seed)] in opt["keyList"]) else []
        index += 1

def FillIn (seed, onValue, **opt):
    index = 0
    while True:
        if not seed[index % len (seed)].isalpha ():
            for notes in onValue:
                yield notes
        else:
            yield []
        index +=1
