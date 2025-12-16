# main.py
import cv2  # <-- ADD THIS
import pygame
import sys
import threading
import time
from config import KEY_NOTE_MAP, NOTE_FREQUENCIES, GESTURE_NOTE_MAP
from sounds import generate_tone
from gesture_controller import GestureHarmonium

# Initialize Pygame
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=256)
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Harmonium 🎹 - Keyboard + Hand Gestures")
clock = pygame.time.Clock()

# Colors
BG = (30, 30, 50)
KEY_COLOR = (220, 220, 220)
KEY_HIGHLIGHT = (100, 200, 255)
TEXT_COLOR = (240, 240, 240)

# Notes in order for GUI
NOTE_ORDER = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
KEY_WIDTH = WIDTH // len(NOTE_ORDER)
KEY_HEIGHT = 150

# Generate sounds
sound_cache = {}
for note in NOTE_ORDER:
    freq = NOTE_FREQUENCIES[note]
    sound_cache[note] = generate_tone(freq, duration=1.2, volume=0.8)

# State
active_note = None
gesture_note = None
running = True

# Shared variable lock
gesture_lock = threading.Lock()

def gesture_worker():
    global gesture_note, running
    try:
        harmonium = GestureHarmonium()
        last_note = None
        last_time = 0
        while running:
            note, frame = harmonium.get_gesture_note()
            cv2.imshow('Hand Gesture - Harmonium', frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC in OpenCV window
                running = False

            now = time.time()
            # Debounce: only trigger every 0.4 seconds
            with gesture_lock:
                if note != last_note or (note and now - last_time > 0.4):
                    gesture_note = note
                    last_note = note
                    last_time = now
                else:
                    gesture_note = None
        harmonium.release()
    except Exception as e:
        print("Gesture error:", e)

# Start gesture thread
gesture_thread = threading.Thread(target=gesture_worker, daemon=True)
gesture_thread.start()

print("🎹 Keyboard: A,S,D,F,G,H,J,K")
print("🖐️  Hand: Raise 1–5 fingers (webcam required)")
print("ESC to quit")

# Main loop
while running:
    screen.fill(BG)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key).lower()
            if key_name in KEY_NOTE_MAP:
                note = KEY_NOTE_MAP[key_name]
                sound_cache[note].play()
                active_note = note
            elif event.key == pygame.K_ESCAPE:
                running = False

    # Check gesture note
    with gesture_lock:
        note_to_play = gesture_note
        if note_to_play and note_to_play in sound_cache:
            sound_cache[note_to_play].play()
            active_note = note_to_play
            gesture_note = None  # consume once

    # Draw keys
    for i, note in enumerate(NOTE_ORDER):
        color = KEY_HIGHLIGHT if note == active_note else KEY_COLOR
        rect = pygame.Rect(i * KEY_WIDTH, HEIGHT - KEY_HEIGHT, KEY_WIDTH - 2, KEY_HEIGHT)
        pygame.draw.rect(screen, color, rect, border_radius=8)
        # Draw label
        font = pygame.font.SysFont(None, 28)
        text = font.render(note, True, (0, 0, 0) if note == active_note else TEXT_COLOR)
        screen.blit(text, (i * KEY_WIDTH + 10, HEIGHT - KEY_HEIGHT + 10))

    # Instructions
    instr = pygame.font.SysFont(None, 24).render(
        "Press A-K or use hand gestures (1-5 fingers). ESC to quit.", True, (200, 200, 200)
    )
    screen.blit(instr, (20, 20))

    pygame.display.flip()
    clock.tick(30)

# Cleanup
running = False
pygame.quit()
cv2.destroyAllWindows()
# At the very bottom of main.py, before sys.exit()
try:
    cv2.destroyAllWindows()
except:
    pass
sys.exit()