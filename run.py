import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import os

# Screen size
screen_w, screen_h = pyautogui.size()

# Mediapipe init
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def finger_states(hand_landmarks):
    """Return which fingers are up (1=up, 0=down)."""
    tips = [4, 8, 12, 16, 20]  # thumb, index, middle, ring, pinky
    fingers = []
    for i, tip in enumerate(tips):
        if i == 0:  # thumb (compare x instead of y)
            if hand_landmarks.landmark[tip].x < hand_landmarks.landmark[tip - 2].x:
                fingers.append(1)
            else:
                fingers.append(0)
        else:
            if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)
    return fingers

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get finger states
            fingers = finger_states(hand_landmarks)

            # Get index finger tip coordinates
            x = int(hand_landmarks.landmark[8].x * w)
            y = int(hand_landmarks.landmark[8].y * h)

            # Map to screen
            screen_x = np.interp(x, [0, w], [0, screen_w])
            screen_y = np.interp(y, [0, h], [0, screen_h])

            # 👆 Mouse movement (Index only)
            if fingers == [0,1,0,0,0]:
                pyautogui.moveTo(screen_x, screen_y, duration=0.1)
                cv2.putText(frame, "Mouse Move", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            # 🤏 Pinch (Thumb + Index) = Left Click
            thumb_x = int(hand_landmarks.landmark[4].x * w)
            thumb_y = int(hand_landmarks.landmark[4].y * h)
            distance = np.hypot(x - thumb_x, y - thumb_y)

            if fingers[0] == 1 and fingers[1] == 1 and distance < 40:
                pyautogui.click()
                cv2.putText(frame, "Left Click", (50,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

            # ✌️ Two fingers up = Right Click
            elif fingers == [0,1,1,0,0]:
                pyautogui.click(button='right')
                cv2.putText(frame, "Right Click", (50,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

            # 🖐 Scroll with index + middle
            elif fingers == [0,1,1,0,0]:
                pyautogui.scroll(-100)

            # 👍 Thumbs Up = Volume Up
            elif fingers == [1,0,0,0,0]:
                pyautogui.press("volumeup")
                cv2.putText(frame, "Volume Up", (50,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            # 👎 Thumbs Down = Volume Down
            elif fingers == [0,1,1,1,1]:
                pyautogui.press("volumedown")
                cv2.putText(frame, "Volume Down", (50,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            # ✊ Fist = Open Notepad
            elif fingers == [0,0,0,0,0]:
                os.system("notepad.exe")
                cv2.putText(frame, "Open Notepad", (50,250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

            # 👉 Index Only = Next Slide
            elif fingers == [0,1,0,0,0]:
                pyautogui.press("right")

            # ✌ Victory = Previous Slide
            elif fingers == [0,1,1,0,0]:
                pyautogui.press("left")

    cv2.imshow("Full Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
