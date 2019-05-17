import enum

class Drums (enum.Enum):
    bass_drum = 36
    snare = 38
    closed_hi_hat = 42
    open_hi_hat = 46
    crash = 49
    ride = 51
    fillIn = [[snare], [snare], [snare], [crash]]

class Pitch (enum.Enum):
    C = 60
    D = 62
    E = 64
    F = 65
    G = 67
    A = 69
    B = 71