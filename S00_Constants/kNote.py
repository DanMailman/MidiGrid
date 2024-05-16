"""
kNote.py

Constants for musical note numbers and dictionaries for mapping between note names and their MIDI numbers.

Constants:
    - Bass_D_SHARP_E_FLAT: The MIDI number for the note D#/Eb in the bass octave.
    - (Additional constants...)

Dictionaries:
    - NOTE_NUMS: A dictionary mapping note names to their MIDI numbers.
    - NOTE_NAMES: A dictionary mapping MIDI numbers to note names.
"""

# Constants for note numbers
Bass_D_SHARP_E_FLAT   = 51; Bass_E                 = 52; Bass_F                = 53; Bass_F_SHARP_G_FLAT   = 54
Middle_G              = 55; Middle_G_SHARP_A_FLAT  = 56; Middle_A              = 57; Middle_A_SHARP_B_FLAT = 58
Middle_B              = 59; Middle_C               = 60; Middle_C_SHARP_D_FLAT = 61; Middle_D              = 62
Middle_D_SHARP_E_FLAT = 63; Middle_E               = 64; Middle_F              = 65; Treble_F_SHARP_G_FLAT = 66
Treble_G              = 67; Treble_G_SHARP_A_FLAT = 68; Treble_A               = 69; Treble_A_SHARP_B_FLAT = 70
Treble_B              = 71; Treble_C              = 72; Treble_C_SHARP_D_FLAT  = 73; Treble_D              = 74
Treble_D_SHARP_E_FLAT = 75; Treble_E              = 76; Treble_F               = 77; High_F_SHARP_G_FLAT   = 78
High_G                = 79; High_G_SHARP_A_FLAT   = 80; High_A                 = 81; High_A_SHARP_B_FLAT   = 82
High_B                = 83; High_C                = 84; High_C_SHARP_D_FLAT    = 85; High_D                = 86
High_D_SHARP_E_FLAT   = 87; High_E                = 88; High_F                 = 89

# Dictionary mapping note names to numbers
NOTE_NUMS = {
    'Bass_D♯/E♭':   Bass_D_SHARP_E_FLAT,   'Bass_E':       Bass_E,                'Bass_F':       Bass_F,
    'Bass_F♯/G♭':   Bass_F_SHARP_G_FLAT,   'Middle_G':     Middle_G,              'Middle_G♯/A♭': Middle_G_SHARP_A_FLAT,
    'Middle_A':     Middle_A,              'Middle_A♯/B♭': Middle_A_SHARP_B_FLAT, 'Middle_♭':     Middle_B,
    'Middle_C':     Middle_C,              'Middle_C♯/D♭': Middle_C_SHARP_D_FLAT, 'Middle_D':     Middle_D,
    'Middle_D♯/E♭': Middle_D_SHARP_E_FLAT, 'Middle_E':     Middle_E,              'Middle_F':     Middle_F,
    'Treble_F♯/G♭': Treble_F_SHARP_G_FLAT, 'Treble_G':     Treble_G,              'Treble_G♯/A♭': Treble_G_SHARP_A_FLAT,
    'Treble_A':     Treble_A,              'Treble_A♯/B♭': Treble_A_SHARP_B_FLAT, 'Treble_♭':     Treble_B,
    'Treble_C':     Treble_C,              'Treble_C♯/D♭': Treble_C_SHARP_D_FLAT, 'Treble_D':     Treble_D,
    'Treble_D♯/E♭': Treble_D_SHARP_E_FLAT, 'Treble_E':     Treble_E,              'Treble_F':     Treble_F,
    'High_F♯/G♭':   High_F_SHARP_G_FLAT,   'High_G':       High_G,                'High_G♯/A♭':   High_G_SHARP_A_FLAT,
    'High_A':       High_A,                'High_A♯/B♭':   High_A_SHARP_B_FLAT,   'High_♭':       High_B,
    'High_C':       High_C,                'High_C♯/D♭':   High_C_SHARP_D_FLAT,   'High_D':       High_D,
    'High_D♯/E♭':   High_D_SHARP_E_FLAT,   'High_E':       High_E,                'High_F':       High_F
}

# Dictionary mapping numbers to note names
NOTE_NAMES = {value: key for key, value in NOTE_NUMS.items()}
