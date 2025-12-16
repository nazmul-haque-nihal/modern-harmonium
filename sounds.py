# sounds.py
import numpy as np
import pygame
import time

def generate_tone(frequency, duration=0.5, sample_rate=22050, volume=0.5):
    """
    Generate a harmonium-like tone using a sine wave with slight harmonics.
    """
    frames = int(duration * sample_rate)
    arr = np.zeros((frames, 2))  # Stereo

    # Base sine wave
    t = np.linspace(0, duration, frames)
    wave = np.sin(2 * np.pi * frequency * t)

    # Add 2nd and 3rd harmonics to mimic reed instrument (like harmonium)
    wave += 0.3 * np.sin(2 * np.pi * 2 * frequency * t)
    wave += 0.2 * np.sin(2 * np.pi * 3 * frequency * t)

    # Normalize and apply volume
    wave = np.clip(wave * volume, -1, 1)

    # Stereo
    arr[:, 0] = wave  # Left
    arr[:, 1] = wave  # Right

    # Convert to 16-bit int
    sound = np.int16(arr * 32767)
    return pygame.sndarray.make_sound(sound)