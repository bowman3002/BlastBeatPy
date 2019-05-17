def BasicBeat(seed, note, keyList, offValue, onValue):
    index = 0
    seedList = list(seed)
    while True:
        yield onValue if (seed[index % len(seed)] in keyList) else offValue
        index += 1
