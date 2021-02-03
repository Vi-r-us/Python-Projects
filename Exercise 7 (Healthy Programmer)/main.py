#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio

from pygame import mixer
import datetime
import time

def time_for_log():
    return datetime.datetime.now()

def is_work_time(current):
    if current > '09:00:00' and current < '17:00:01':
        return True
    else:
        print("\nYour work time is ended.")
        return False

def notification(x):
    mixer.init()
    mixer.music.load(x)
    mixer.music.play()

def logs(file,wl,s):
    if file=='Water.txt':
        f = open(file, 'a')
        time = time_for_log()
        if s==1:    f.write("[" + str(time) + "]\t" + f" {wl*200 -100} ML Water Left" + "\n")
        else:   f.write("[" + str(time) + "]\t" + f" {wl*200 -100} ML Water Left\t" + "Snoozed" + "\n")
        f.close()
    else:
        f = open(file, 'a')
        time = time_for_log()
        if s==1:    f.write("[" + str(time) + "]\t"  + "\n")
        else:   f.write("[" + str(time) + "]\t"  + "Snoozed" + "\n")
        f.close()

NoOfWaterRemaining = 18

water_Duration_Time = 15  # 1500 sec = 25 min
eyes_Duration_Time = 1800   # 1800 sec = 30 min
exercise_Duration_Time = 2700   # 2700 sec = 45 min

current_time = time.strftime('%H:%M:%S')
water_taken_at = time.time()
eyes_exercise_at = time.time()
physical_exercise_at = time.time()

water = 'Water_Notification.mp3'
eyes = 'Eyes_Notification.mp3'
exercise = 'Exercise_Notification.mp3'

w = 'Water.txt'
e = 'Eyes.txt'
p = 'Exercise.txt'

while is_work_time(current_time):

    if NoOfWaterRemaining>0:
        if (time.time()-water_taken_at)>water_Duration_Time :
            print("Time to take Water")
            i=1
            while True:
                notification(water)
                ch = int(input("\n\t1. Stop\n\t2. Snooze\nEnter your choice :\t"))
                if ch == 1:
                    water_taken_at = time.time()
                    NoOfWaterRemaining -= 1
                    logs(w,NoOfWaterRemaining,i)
                    mixer.quit()
                    break
                elif ch == 2:
                    if i==0:
                        print("You can't snooze it anymore")
                        continue
                    print("\n\t\tSNOOZED FOR 5 MINUTES")
                    mixer.music.pause()
                    time.sleep(300)
                    i -=1
                else:
                    print("Wrong Choice")
    time.sleep(60)

    if (time.time()-eyes_exercise_at)>eyes_Duration_Time:
        print("Time to do eyes exercise")
        i=1
        while True:
            notification(eyes)
            ch = int(input("\t1. Stop\n\t2. Snooze\nEnter your choice :\t"))
            if ch == 1:
                eyes_exercise_at = time.time()
                logs(e, NoOfWaterRemaining, i)
                mixer.quit()
                break
            elif ch == 2:
                if i==0:
                    print("You can't snooze it anymore")
                    continue
                print("\n\t\tSNOOZED FOR 5 MINUTES")
                mixer.music.pause()
                time.sleep(300)
                i -=1
            else:
                print("Wrong Choice")
    time.sleep(60)

    if (time.time()-physical_exercise_at)>exercise_Duration_Time:
        print("Time to do Physical exercise")
        i=1
        while True:
            notification(exercise)
            ch = int(input("\t1. Stop\n\t2. Snooze\nEnter your choice :\t"))
            if ch == 1:
                physical_exercise_at = time.time()
                logs(p, NoOfWaterRemaining, i)
                mixer.quit()
                break
            elif ch == 2:
                if i==0:
                    print("You can't snooze it anymore")
                    continue
                print("\n\t\tSNOOZED FOR 5 MINUTES")
                mixer.music.pause()
                time.sleep(300)
                i -=1
            else:
                print("Wrong Choice")
    current_time = time.strftime('%H:%M:%S')
    time.sleep(60)









