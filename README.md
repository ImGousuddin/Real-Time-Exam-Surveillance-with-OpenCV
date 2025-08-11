# 🎯 Real-Time Exam Surveillance System

This project is a **Real-Time Exam Monitoring System** that detects suspicious behavior (cheating) during an online exam using **audio analysis** and **head pose detection**.  
It combines microphone input and head movement tracking to calculate a "cheat probability" and visualize it in real-time.

---

## 📂 Project Structure

├── audio.py # Captures microphone input & detects abnormal sound activity
├── detection.py # Combines audio & head pose data to calculate cheat probability
├── run.py # Main runner that starts all modules in parallel
├── head_pose.py # (Not provided here) Tracks head movement via webcam


---

## ⚙️ Features
- 🎤 **Audio-based cheating detection**: Monitors microphone input for abnormal loudness patterns.
- 👀 **Head pose tracking**: Detects if the candidate is looking away frequently.
- 📊 **Cheating probability score**: Uses weighted averages to estimate the likelihood of cheating.
- 📈 **Real-time plotting**: Displays a live graph of cheating probability using `matplotlib`.
- 🔄 **Multi-threaded execution**: Runs audio, head pose, and detection modules simultaneously.

---

## 🛠 Requirements

Install the dependencies before running the project:

```bash
pip install sounddevice
pip install numpy
pip install matplotlib
pip install opencv-python
🚀 Usage
Clone the repository:

bash
git clone https://github.com/ImGousuddin/Exam-Surveillance.git
cd Exam-Surveillance
Ensure all required files are present:

audio.py

detection.py

head_pose.py (you will need to create or add this file)

run.py

Run the main program:

bash
python run.py
View results:

A real-time graph will show cheating probability.


Console will print "CHEATING" when probability exceeds 0.6.

🖼 How It Works
1. audio.py
Captures microphone audio stream.

Calculates sound amplitude.

Flags suspicious noises (like people talking or external disturbances).

2. head_pose.py
Uses OpenCV to track head rotation angles.

Detects when a person frequently looks away from the screen.

3. detection.py
Combines audio and head pose detection results.

Calculates a probability score (0 to 1) of cheating.

Plots results in real-time using matplotlib.

4. run.py
Runs all modules in parallel threads for real-time performance.
