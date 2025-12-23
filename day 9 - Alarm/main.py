import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import datetime
import time

# pygame initialization
pygame.mixer.init()
pygame.mixer.music.load("./day 9 - Alarm/ringtone2.mp3")
pygame.mixer.music.set_volume(1)

def set_alarm(alarm_time):
    print(f"alarm set for {alarm_time}")
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time < alarm_time:
            print(current_time)
        else:
            print("Wake up!")
            pygame.mixer.music.play(0)
            input("press enter to wake the f up and turn off the alarm! ")
            pygame.mixer.music.stop()
            break
        time.sleep(1)



if __name__ == '__main__':
    set_alarm(input("Enter alarm time (HH:MM:SS): "))