"""
kInstr.py

This module defines constants and dictionaries for MIDI instrument numbers and names.
It provides mappings between instrument names and their corresponding MIDI numbers, and vice versa.

Constants:
    - ACCORDION: The MIDI number for the accordion.
    - BANDONEON: The MIDI number for the bandoneon.
    - BRIGHT_PIANO: The MIDI number for the bright piano.
    - (Additional constants...)

Dictionaries:
    - INSTR_NUMS: A dictionary mapping instrument names to their MIDI numbers.
    - INSTR_NAMES: A dictionary mapping MIDI numbers to instrument names.
"""
# Constants for instrument numbers
ACCORDION             =  21;  BANDONEON            =  23;  BRIGHT_PIANO         =   1;  CELESTA               =   8
CHORUSED_PIANO        =   5;  CLAVINET             =   7;  DULCIMER             =  15;  ELECTRIC_PIANO        =   2
GERMAN_HARPSICHORD    =   6;  GLOCKENSPIEL         =   9;  GRAND_PIANO          =   0;  HONKYTONK_PIANO       =   3
MUSIC_BOX             =  10;  RHODES_PIANO         =   4;  VIBRAPHONE           =  11;  XYLOPHONE             =  13
TUBULAR_BELLS         =  14;  HAMMOND_ORGAN        =  16;  PERCUSSIVE_ORGAN     =  17;  ROCK_ORGAN            =  18
PIPE_ORGAN_AND_PEDALS =  19;  REED_ORGAN           =  20;  HOHNER_HARMONICA     =  22;  NYLON_GUITAR          =  24
STEEL_GUITAR          =  25;  JAZZ_GUITAR          =  26;  CLEAN_GUITAR         =  27;  GUITAR_MUTES          =  28
STRAT_MARSHALL        =  29;  GARCIA_DIST_GUITAR   =  30;  GUITAR_HARMONICS     =  31;  ACOUSTIC_BASS         =  32
FINGERED_BASS         =  33;  EPIPHONE_PICK_BASS   =  34;  FRETTLESS_BASS       =  35;  SLAP_BASS_1           =  36
SLAP_BASS_2           =  37;  SYNTH_BASS_1         =  38;  SYNTH_BASS_2         =  39;  VIOLIN                =  40
VIOLA                 =  41;  CELLO                =  42;  CONTRABASS           =  43;  TREMELO_STRINGS       =  44
PIZZICATO_STRINGS     =  45;  HARP                 =  46;  TIMPANI_AND_ROLLS    =  47;  STRING_ENSEMBLE_1     =  48
STRING_ENSEMBLE_2     =  49;  SYNTH_STRINGS_1      =  50;  SYNTH_STRINGS_2      =  51;  SYNTH_CHOIR_OOHS      =  54
ORCHESTRA_HIT         =  55;  TRUMPET              =  56;  TROMBONE             =  57;  TUBA                  =  58
TRUMPET_CUP_MUTE      =  59;  FRENCH_HORN          =  60;  BRASS_SECTION        =  61;  SYNTH_BRASS_1         =  62
SYNTH_BRASS_2         =  63;  SOPRANO_SAX          =  64;  ALTO_SAX             =  65;  BREATHY_TENOR_SAX     =  66
BARITONE_SAX          =  67;  OBOE                 =  68;  ENGLISH_HORN         =  69;  BASSOON               =  70
CLARINET              =  71;  PICCOLO              =  72;  FLUTE                =  73;  RECORDER              =  74
PAN_FLUTE             =  75;  BOTTLE_CHIFF         =  76;  SHAKUHACHI           =  77;  WHISTLE               =  78
OCARINA               =  79;  LEAD_1_SQUARE        =  80;  LEAD_2_SAWTOOTH      =  81;  LEAD_3_CALLIOPE       =  82
LEAD_4_CHIFF          =  83;  LEAD_5_CHARANG       =  84;  LEAD_6_VOICE         =  85;  LEAD_7_FIFTHS         =  86
LEAD_8_BASSANDLEAD    =  87;  PAD_1_NEW_AGE        =  88;  PAD_2_WARM           =  89;  PAD_3_POLYSYNTH       =  90
PAD_4_CHOIR           =  91;  PAD_5_BOWED          =  92;  PAD_6_METALLIC       =  93;  PAD_7_HALO            =  94
PAD_8_SWEEP           =  95;  FX_1_RAIN            =  96;  FX_2_SOUNDTRACK      =  97;  FX_3_CRYSTAL          =  98
FX_4_ATMOSPHERE       =  99;  FX_5_BRIGHTNESS      = 100;  FX_6_GOBLINS         = 101;  FX_7_ECHOES           = 102
FX_8_SCIFI            = 103;  SITAR                = 104;  BANJO                = 105;  SHAMISEN              = 106
KOTO                  = 107;  KALIMBA              = 108;  BAGPIPE              = 109;  FIDDLE                = 110
SHANAI                = 111;  TINKLE_BELL          = 112;  AGOGO                = 113;  STEEL_DRUM            = 114
WOOD_BLOCK            = 115;  TAIKO_DRUM           = 116;  MELODIC_TOM          = 117;  SYNTH_DRUM            = 118
REVERSE_CYMBAL        = 119;  GUITAR_FRET_NOISE    = 120;  BREATH_NOISE         = 121;  SEASHORE              = 122
BIRD_TWEET            = 123;  TELEPHONE_RING       = 124;  HELICOPTER           = 125;  APPLAUSE              = 126
GUN_SHOT              = 127

INSTR_NAMES = {
    ACCORDION:             'Accordion',           BANDONEON:          'Bandoneon',
    BRIGHT_PIANO:          'Bright Piano',        CELESTA:            'Celesta',
    CHORUSED_PIANO:        'Chorused Piano',      CLAVINET:           'Clavinet',
    DULCIMER:              'Dulcimer',            ELECTRIC_PIANO:     'Electric Piano',
    GERMAN_HARPSICHORD:    'German Harpsichord',  GLOCKENSPIEL:       'Glockenspiel',
    GRAND_PIANO:           'Grand Piano',         HONKYTONK_PIANO:    'Honkytonk Piano',
    MUSIC_BOX:             'Music Box',           RHODES_PIANO:       'Rhodes Piano',
    VIBRAPHONE:            'Vibraphone',          XYLOPHONE:          'Xylophone',
    TUBULAR_BELLS:         'Tubular Bells',       HAMMOND_ORGAN:      'Hammond Organ',
    PERCUSSIVE_ORGAN:      'Percussive Organ',    ROCK_ORGAN:         'Rock Organ',
    PIPE_ORGAN_AND_PEDALS: 'Pipe Organ & Pedals', REED_ORGAN:         'Reed Organ',
    HOHNER_HARMONICA:      'Hohner Harmonica',    NYLON_GUITAR:       'Nylon Guitar',
    STEEL_GUITAR:          'Steel Guitar',        JAZZ_GUITAR:        'Jazz Guitar',
    CLEAN_GUITAR:          'Clean Guitar',        GUITAR_MUTES:       'Guitar Mutes',
    STRAT_MARSHALL:        'Strat. Marshall',     GARCIA_DIST_GUITAR: 'Garcia Dist. Guitar',
    GUITAR_HARMONICS:      'Guitar Harmonics',    ACOUSTIC_BASS:      'Acoustic Bass',
    FINGERED_BASS:         'Fingered Bass',       EPIPHONE_PICK_BASS: 'Epiphone Pick Bass',
    FRETTLESS_BASS:        'Frettless Bass',      SLAP_BASS_1:        'Slap Bass 1',
    SLAP_BASS_2:           'Slap Bass 2',         SYNTH_BASS_1:       'Synth Bass 1',
    SYNTH_BASS_2:          'Synth Bass 2',        VIOLIN:             'Violin',
    VIOLA:                 'Viola',               CELLO:              'Cello',
    CONTRABASS:            'Contrabass',          TREMELO_STRINGS:    'Tremelo Strings',
    PIZZICATO_STRINGS:     'Pizzicato Strings',   HARP:               'Harp',
    TIMPANI_AND_ROLLS:     'Timpani and Rolls',   STRING_ENSEMBLE_1:  'String Ensemble 1',
    STRING_ENSEMBLE_2:     'String Ensemble 2',   SYNTH_STRINGS_1:    'Synth Strings 1',
    SYNTH_STRINGS_2:       'Synth Strings 2',     SYNTH_CHOIR_OOHS:   'Synth Choir Oohs',
    ORCHESTRA_HIT:         'Orchestra Hit',       TRUMPET:            'Trumpet',
    TROMBONE:              'Trombone',            TUBA:               'Tuba',
    TRUMPET_CUP_MUTE:      'Trumpet Cup Mute',    FRENCH_HORN:        'French Horn',
    BRASS_SECTION:         'Brass Section',       SYNTH_BRASS_1:      'Synth Brass 1',
    SYNTH_BRASS_2:         'Synth Brass 2',       SOPRANO_SAX:        'Soprano Sax',
    ALTO_SAX:              'Alto Sax',            BREATHY_TENOR_SAX:  'Breathy Tenor Sax',
    BARITONE_SAX:          'Baritone Sax',        OBOE:               'Oboe',
    ENGLISH_HORN:          'English Horn',        BASSOON:            'Bassoon',
    CLARINET:              'Clarinet',            PICCOLO:            'Piccolo',
    FLUTE:                 'Flute',               RECORDER:           'Recorder',
    PAN_FLUTE:             'Pan Flute',           BOTTLE_CHIFF:       'Bottle Chiff',
    SHAKUHACHI:            'Shakuhachi',          WHISTLE:            'Whistle',
    OCARINA:               'Ocarina',             LEAD_1_SQUARE:      'Lead 1 (Square)',
    LEAD_2_SAWTOOTH:       'Lead 2 (Sawtooth)',   LEAD_3_CALLIOPE:    'Lead 3 (Calliope)',
    LEAD_4_CHIFF:          'Lead 4 (Chiff)',      LEAD_5_CHARANG:     'Lead 5 (Charang)',
    LEAD_6_VOICE:          'Lead 6 (Voice)',      LEAD_7_FIFTHS:      'Lead 7 (Fifths)',
    LEAD_8_BASSANDLEAD:    'Lead 8 (Bass&Lead)',  PAD_1_NEW_AGE:      'Pad 1 (New Age)',
    PAD_2_WARM:            'Pad 2 (Warm)',        PAD_3_POLYSYNTH:    'Pad 3 (Polysynth)',
    PAD_4_CHOIR:           'Pad 4 (Choir)',       PAD_5_BOWED:        'Pad 5 (Bowed)',
    PAD_6_METALLIC:        'Pad 6 (Metallic)',    PAD_7_HALO:         'Pad 7 (Halo)',
    PAD_8_SWEEP:           'Pad 8 (Sweep)',       FX_1_RAIN:          'FX 1 (Rain)',
    FX_2_SOUNDTRACK:       'FX 2 (Soundtrack)',   FX_3_CRYSTAL:       'FX 3 (Crystal)',
    FX_4_ATMOSPHERE:       'FX 4 (Atmosphere)',   FX_5_BRIGHTNESS:    'FX 5 (Brightness)',
    FX_6_GOBLINS:          'FX 6 (Goblins)',      FX_7_ECHOES:        'FX 7 (Echoes)',
    FX_8_SCIFI:            'FX 8 (Sci-Fi)',       SITAR:              'Sitar',
    BANJO:                 'Banjo',               SHAMISEN:           'Shamisen',
    KOTO:                  'Koto',                KALIMBA:            'Kalimba',
    BAGPIPE:               'Bagpipe',             FIDDLE:             'Fiddle',
    SHANAI:                'Shanai',              TINKLE_BELL:        'Tinkle Bell',
    AGOGO:                 'Agogo',               STEEL_DRUM:         'Steel Drum',
    WOOD_BLOCK:            'Wood Block',          TAIKO_DRUM:         'Taiko Drum',
    MELODIC_TOM:           'Melodic Tom',         SYNTH_DRUM:         'Synth Drum',
    REVERSE_CYMBAL:        'Reverse Cymbal',      GUITAR_FRET_NOISE:  'Guitar Fret Noise',
    BREATH_NOISE:          'Breath Noise',        SEASHORE:           'Seashore',
    BIRD_TWEET:            'Bird Tweet',          TELEPHONE_RING:     'Telephone Ring',
    HELICOPTER:            'Helicopter',          APPLAUSE:           'Applause',
    GUN_SHOT:              'Gun Shot'
}

INSTR_NUMS = {v: k for k, v in INSTR_NAMES.items()}
