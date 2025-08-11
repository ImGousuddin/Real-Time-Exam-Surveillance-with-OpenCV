import sounddevice as sd
import numpy as np

# Global variables
SOUND_AMPLITUDE = 0
AUDIO_CHEAT = 0

# Sound variables
CALLBACKS_PER_SECOND = 38         
SUS_FINDING_FREQUENCY = 2               
SOUND_AMPLITUDE_THRESHOLD = 20          

# Packing *n* frames to calculate SUS
FRAMES_COUNT = int(CALLBACKS_PER_SECOND / SUS_FINDING_FREQUENCY)
AMPLITUDE_LIST = [0] * FRAMES_COUNT
SUS_COUNT = 0
count = 0


def print_sound(indata, outdata, frames, time, status):
    global SOUND_AMPLITUDE, SUS_COUNT, count, AUDIO_CHEAT
    vnorm = int(np.linalg.norm(indata) * 10)
    AMPLITUDE_LIST.append(vnorm)
    count += 1
    AMPLITUDE_LIST.pop(0)
    
    if count == FRAMES_COUNT:
        avg_amp = sum(AMPLITUDE_LIST) / FRAMES_COUNT
        SOUND_AMPLITUDE = avg_amp
        if SUS_COUNT >= 2:
            AUDIO_CHEAT = 1
            SUS_COUNT = 0
        if avg_amp > SOUND_AMPLITUDE_THRESHOLD:
            SUS_COUNT += 1
        else:
            SUS_COUNT = 0
            AUDIO_CHEAT = 0
        count = 0


def sound():
    with sd.Stream(callback=print_sound):
        sd.sleep(int(1e6))


if __name__ == "__main__":
    sound()
