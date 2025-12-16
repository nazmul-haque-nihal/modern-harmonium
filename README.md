
# 🎹 Modern Harmonium

A sleek and interactive digital harmonium that you can play using your keyboard or with hand gestures via your webcam. This project blends classic musical expression with modern computer vision technology.
<img width="1124" height="728" alt="harmonium" src="https://github.com/user-attachments/assets/076c0224-6c50-4a81-ac77-a44d38c3e116" />

---

## ✨ Features

- **Dual Control Modes:** Play notes using your computer keyboard or with intuitive hand gestures.
- **Real-time Gesture Recognition:** Uses your webcam to detect the number of fingers you're holding up and plays the corresponding note.
- **Rich, Harmonium-like Sound:** Tones are synthesized with added harmonics to emulate the sound of a real reed instrument.
- **Sleek & Modern UI:** A clean and visually appealing interface built with Pygame.
- **Low Latency:** Optimized for a responsive musical experience.

---

## 🚀 How It Works

The application is built with Python and leverages several powerful libraries:

- **Pygame:** Powers the graphical user interface, handles keyboard input, and manages audio playback.
- **OpenCV & MediaPipe:** Work together to capture video from your webcam, detect hand landmarks, and count the number of raised fingers in real-time.
- **NumPy:** Generates the audio waveforms for each musical note, creating a rich and authentic sound.

A background thread is dedicated to gesture recognition, ensuring the UI remains smooth and responsive while processing video frames.

---

## 📋 Requirements

- Python 3.7+
- Pygame
- OpenCV
- MediaPipe
- NumPy

---

## 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/modern-harmonium.git
    cd modern-harmonium
    ```

2.  **Install the dependencies:**
    ```bash
    pip install pygame opencv-python mediapipe numpy
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```

A window will open displaying the harmonium keyboard, and a separate OpenCV window will show your webcam feed for gesture control.

---

## 🎶 Controls

### Keyboard

- The keys `A, S, D, F, G, H, J, K` correspond to the notes `C4, D4, E4, F4, G4, A4, B4, C5`.

### Hand Gestures

- **Show 1 to 5 fingers** to the webcam to play notes:
    - **1 Finger:** C4
    - **2 Fingers:** D4
    - **3 Fingers:** E4
    - **4 Fingers:** F4
    - **5 Fingers:** G4

- **Press `ESC`** in either window to quit the application.

---

## 🌟 Future Ideas

- [ ] Add more notes and octaves.
- [ ] Implement a recording and playback feature.
- [ ] Allow users to customize key and gesture mappings.
- [ ] Package the application into a standalone executable.
- [ ] Add more complex gestures for chords or special effects.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Made with ❤️ and Python
