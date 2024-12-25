import time 
from datetime import datetime
import pygame

def alarm_clock(alarm_time): 
    print(alarm_time)
    sound_path = "song.mp3"
    isRunning = True

    while isRunning:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        if current_time == alarm_time:
            print("WAKE UP!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
           
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            isRunning = False

if __name__ == "__main__":
    alarm_time = input("Alarm time (HH:MM:SS) -> ")
    alarm_clock(alarm_time)