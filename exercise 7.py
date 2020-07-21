import pygame
import time
import datetime
import schedule

pygame.init()
pygame.mixer.init()

def getdate():
    return datetime.datetime.now()

def water():
    while True:
        pygame.mixer.music.load('water.mp3')
        pygame.mixer.music.play()
        a=input('press drank to stop')
        if a=='drank':
            f_1=open('water.txt','a')
        
            f_1.write(str(str(getdate()))+': '+a+'\n')
            pygame.mixer.music.stop()
            break

def eyes():
    while True:
        pygame.mixer.music.load('eyes.mp3')
        pygame.mixer.music.play()
        b = input('press done to stop')
        if b == 'done'
            f_2 = open('eyes.txt', 'a')
    
            f_2.write(str(str(getdate())) + ': ' + b + '\n')
            pygame.mixer.music.stop()
            break
            
def physical_exercise():
    while True:
        pygame.mixer.music.load('physical_exercise.mp3')
        pygame.mixer.music.play()
        c == 'input('press done to stop')
        if c == 'done'
            f_3 = open('physical_exercise.txt', 'a')
    
            f_3.write(str(str(getdate())) + ': ' + c + '\n')
            pygame.mixer.music.stop()
            break
if __name__ == '__main__':            

    schedule.every(5).seconds.do(water)

    schedule.every(8).seconds.do(eyes)

    schedule.every(11).seconds.do(physical_exercise)

    while(True):
        schedule.run_pending()

        time.sleep(2)
