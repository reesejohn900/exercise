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
    pygame.mixer.music.play(-1)
        

    a = input('type drank to stop\n')

    if not a :
        pygame.mixer.music.stop()



    elif a=='drank':
        pygame.mixer.music.stop()


        f_1=open('water.txt','a')
        
        f_1.write(str(str(getdate()))+': '+a+'\n')






def eyes():

    pygame.mixer.music.load('eyes.mp3')
    pygame.mixer.music.play(-1)
    b = input('type done to stop\n')
    if not b:

        pygame.mixer.music.stop()



    elif b== 'done':
        pygame.mixer.music.stop()

        f_2 = open('eyes.txt', 'a')
    
        f_2.write(str(str(getdate())) + ': ' + b + '\n')


            
            
def physical_exercise():

    pygame.mixer.music.load('exercise.mp3')
    pygame.mixer.music.play(-1)
    c = input('type did to stop')
    if not c:

        pygame.mixer.music.stop()



    elif c== 'did':
        pygame.mixer.music.stop()

        f_3 = open('physical_exercise.txt', 'a')
    
        f_3.write(str(str(getdate())) + ': ' + c + '\n')






if __name__ == '__main__':           


    schedule.every(5).seconds.do(water)

    schedule.every(8).seconds.do(eyes)

    schedule.every(11).seconds.do(physical_exercise)

    while True:
        schedule.run_pending()

        time.sleep(2)
