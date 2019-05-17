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

'''
opt:
    cooldown:int        The amount of beats to wait before playing again
    keylist:[String]    The list of keys which close the hihat
    default:int         The default value to use
    closed:int          The closed value to use
'''
def HiHat(seed, onValue, **opt):
    index = 0
    currentCooldown = 0
    cooldown = opt['cooldown']
    keyList = opt['keylist']
    while True:
        if currentCooldown == 0:
            currentCooldown = cooldown
            index += 1
            yield [opt['default']] if (seed[index % len(seed)] in keyList) else [opt['closed']]
        else:
            index += 1
            yield []
            currentCooldown -= 1
