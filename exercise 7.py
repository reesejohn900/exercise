import pygame
import time
import datetime
import schedule

pygame.init()
pygame.mixer.init()

def getdate():
    return datetime.datetime.now()

def water():
    pygame.mixer.music.load('water.mp3')
    pygame.mixer.music.play()

    f_1=open('water.txt','a')
    a=input()
    f_1.write(str(str(getdate()))+': '+a+'\n')
    pygame.mixer.music.stop()

def eyes():
    pygame.mixer.music.load('eyes.mp3')
    pygame.mixer.music.play()

    f_2 = open('eyes.txt', 'a')
    b = input()
    f_2.write(str(str(getdate())) + ': ' + b + '\n')
    pygame.mixer.music.stop()

def physical_exercise():
    pygame.mixer.music.load('physical_exercise.mp3')
    pygame.mixer.music.play()

    f_3 = open('physical_exercise.txt', 'a')
    c = input()
    f_3.write(str(str(getdate())) + ': ' + c + '\n')
    pygame.mixer.music.stop()

schedule.every(5).seconds.do(water)

schedule.every(8).seconds.do(eyes)

schedule.every(11).seconds.do(physical_exercise)

while(True):
    schedule.run_pending()

    time.sleep(2)
