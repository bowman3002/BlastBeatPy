def BasicBeat(seed, onValue, **opt):
    index = 0
    while True:
        yield onValue if (seed[index % len(seed)] in opt["keyList"]) else -1
        index += 1
