Here’s a clean and attractive `README.md` tailored for your project under the new name **RunGestures**:

# 🏃‍♂️ RunGestures

Control Temple Run using just your hand gestures!  
**RunGestures** uses your webcam to detect specific hand movements and simulate keyboard inputs — no controller or keyboard needed.

---

## ✋ Supported Gestures

| Gesture                        | Action       | How to Perform                         |
|-------------------------------|--------------|----------------------------------------|
| 🖐 All five fingers up         | Jump         | Spread all your fingers                |
| 🤏 Thumb + index touching      | Slide        | Pinch thumb and index together         |
| 👍 Thumb to the right of index | Move Right   | Thumbs-up angled right                 |
| 👍 Thumb to the left of index  | Move Left    | Thumbs-up angled left                  |
| 🖖 Index + middle + ring up    | Boost        | Raise 3 fingers (no pinky or thumb)    |

---

## 🚀 How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/RunGestures.git
   cd RunGestures
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Start the program**

   ```bash
   python gesture_controller.py
   ```

4. **Open Temple Run or any arrow-key game**, and control it with your hand!

---

## ⚙️ Requirements

* Python 3.7+
* Webcam
* Game that uses arrow keys (e.g. Temple Run clone)
* Python packages:

  * `opencv-python`
  * `mediapipe`
  * `pyautogui`

---

## 🧠 How It Works

* Uses **MediaPipe** to detect hand landmarks in real-time
* Uses **OpenCV** to process webcam input
* Maps gestures to actions using landmark positions
* Sends key presses with **pyautogui**

---

## 📸 Screenshot

*(Add a screenshot of your app running here)*

---

## 🙌 Credits

* [MediaPipe by Google](https://mediapipe.dev/)
* [OpenCV](https://opencv.org/)
* [PyAutoGUI](https://pyautogui.readthedocs.io/)

---

## 💡 Future Ideas

* Add sound feedback for gestures
* Improve accuracy with gesture smoothing
* Add gesture-based game menus

---

🎮 Have fun running — hands-free!

````

---

### ✅ Also add a `requirements.txt` file:

```txt
opencv-python
mediapipe
pyautogui
````

---

Let me know if you want a **custom logo**, **demo GIF**, or **badges (stars, forks, license)** for the top of your README!
