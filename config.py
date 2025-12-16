# config.py

# Keyboard mapping (unchanged)
KEY_NOTE_MAP = {
    'a': 'C4',
    's': 'D4',
    'd': 'E4',
    'f': 'F4',
    'g': 'G4',
    'h': 'A4',
    'j': 'B4',
    'k': 'C5',
}

# Frequencies
NOTE_FREQUENCIES = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25,
}

# Gesture-to-note mapping (based on number of raised fingers)
# 1 finger = C4, 2 = D4, ..., 5 = C5
GESTURE_NOTE_MAP = {
    1: 'C4',
    2: 'D4',
    3: 'E4',
    4: 'F4',
    5: 'G4',  # You can extend to A4, B4, C5 if needed
}