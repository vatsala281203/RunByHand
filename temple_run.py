import cv2
import mediapipe as mp
import pyautogui
import time
import math

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

prev_gesture = ""
cooldown = 1
last_time = 0

# Helper: check if finger is up
def finger_up(lm, tip, pip, threshold=10):
    return (lm[pip][2] - lm[tip][2]) > threshold

# Helper: calculate Euclidean distance between two landmarks
def distance(p1, p2):
    return math.hypot(p2[1] - p1[1], p2[2] - p1[2])

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    gesture = ""
    current_time = time.time()

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []
            h, w, _ = img.shape

            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))

            if lm_list:
                # Finger states
                index_up = finger_up(lm_list, 8, 6)
                middle_up = finger_up(lm_list, 12, 10)
                ring_up = finger_up(lm_list, 16, 14)
                pinky_up = finger_up(lm_list, 20, 18)
                thumb_up = finger_up(lm_list, 4, 2)

                thumb_tip = lm_list[4]
                index_tip = lm_list[8]
                thumb_index_dist = distance(thumb_tip, index_tip)

                # 1. Jump: All 5 fingers up
                if all([index_up, middle_up, ring_up, pinky_up, thumb_up]):
                    gesture = "jump"

                # 2. Slide: Thumb and index tips are close
                elif thumb_index_dist < 40:
                    gesture = "slide"

                # 3. Right: Thumb up and to the right of index
                elif thumb_up and thumb_tip[1] > index_tip[1]:
                    gesture = "right"

                # 4. Left: Thumb up and to the left of index
                elif thumb_up and thumb_tip[1] < index_tip[1]:
                    gesture = "left"

                # 5. Boost: Only index, middle, and ring fingers are up
                elif index_up and middle_up and ring_up and not pinky_up and not thumb_up:
                    gesture = "boost"

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    # Trigger action if new gesture and cooldown passed
    if gesture and gesture != prev_gesture and (current_time - last_time > cooldown):
        print(f"Gesture Detected: {gesture}")

        if gesture == "jump":
            pyautogui.press("up")
        elif gesture == "slide":
            pyautogui.press("down")
        elif gesture == "left":
            pyautogui.press("left")
        elif gesture == "right":
            pyautogui.press("right")
        elif gesture == "boost":
            pyautogui.press("space")

        prev_gesture = gesture
        last_time = current_time

    # Display
    cv2.putText(img, f"Gesture: {gesture}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.imshow("Gesture Controller", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
