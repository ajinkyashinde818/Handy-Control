Handy-Control

Handy-Control is a gesture-based laptop control system built with Python.
It leverages Google’s pre-trained hand/gesture recognition models (e.g., MediaPipe, TensorFlow Hub, or Teachable Machine exports) for fast and accurate gesture detection.

This project allows you to control your computer with hand gestures in real-time — without needing a mouse or keyboard.

🚀 Features

Uses Google pre-trained model for gesture recognition

Real-time webcam feed processing with OpenCV

Maps recognized gestures to system actions (play, pause, volume, slide navigation, etc.)

Lightweight and works on CPU

📂 Project Structure
Handy-Control/
│
├── model/                  # Pre-trained Google model (saved_model / keras.h5 / .tflite)
├── run.py                  # Main script for Handy-Control
├── requirements.txt        # Dependencies
└── README.md

⚙️ Installation

Clone the repository:

git clone https://github.com/ajinkyashinde818/Handy-Control.git
cd Handy-Control


Install required dependencies:

pip install -r requirements.txt


requirements.txt

tensorflow==2.15
mediapipe
opencv-python
numpy
pyautogui
matplotlib   # optional (for debugging/visualization)


⚠️ Recommended: Use Python 3.10 for TensorFlow compatibility.

🛠️ Usage

Run the main script:

python run.py


Webcam will open.

Gestures are detected using the pre-trained model.

Mapped actions are executed (keyboard/mouse/system control).

✋ Example Controls

✊ Fist → Play/Pause Media

☝️ One Finger → Next Slide

✌️ Two Fingers → Previous Slide

🖐️ Open Palm → Increase Volume

👍 Thumb Up → Decrease Volume

(You can customize these mappings inside run.py)

📊 Why Use Google’s Pre-Trained Model?

No dataset collection or training needed

High accuracy out-of-the-box

Optimized for real-time inference

Easy to extend with your own gestures

🔧 Future Improvements

Add custom gestures (train with Teachable Machine or TensorFlow)

Extend to voice + gesture hybrid control

Add more system controls (brightness, app launching, etc.)

Convert to .tflite for mobile deployment

📜 License & Credits

Google MediaPipe / TensorFlow Hub / Teachable Machine – for pretrained models

OpenCV – for video processing

PyAutoGUI – for system automation

👤 Author

Ajinkya Shinde
🔗 GitHub: ajinkyashinde818
