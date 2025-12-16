# gesture_controller.py
import cv2
import mediapipe as mp
import time

class GestureHarmonium:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.6
        )
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")

    def count_fingers(self, hand_landmarks):
        """Count raised fingers using landmark positions."""
        landmarks = hand_landmarks.landmark
        tip_ids = [8, 12, 16, 20]  # Index, middle, ring, pinky tips
        base_ids = [6, 10, 14, 18]  # Their lower joints

        # Thumb (special case)
        thumb_tip = landmarks[4]
        thumb_base = landmarks[2]
        thumb_up = thumb_tip.x < thumb_base.x  # For right hand facing cam

        # Count other fingers
        fingers = []
        for tip, base in zip(tip_ids, base_ids):
            if landmarks[tip].y < landmarks[base].y:
                fingers.append(1)
            else:
                fingers.append(0)

        total = sum(fingers)
        # Optional: include thumb (uncomment if needed)
        # total += 1 if thumb_up else 0

        return total

    def get_gesture_note(self):
        """Returns note name (e.g., 'C4') or None if no hand."""
        ret, frame = self.cap.read()
        if not ret:
            return None, frame

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        note = None
        finger_count = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )
                finger_count = self.count_fingers(hand_landmarks)
                if finger_count in [1, 2, 3, 4, 5]:
                    from config import GESTURE_NOTE_MAP
                    note = GESTURE_NOTE_MAP.get(finger_count)

        # Display count
        cv2.putText(frame, f'Fingers: {finger_count}', (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        if note:
            cv2.putText(frame, f'Note: {note}', (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        return note, frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()