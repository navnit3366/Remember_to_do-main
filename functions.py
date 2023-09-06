from visuals.visual import run
from time import sleep
from datetime import date
import playsound
import json


def check_remember():
    with open("data/rememberlist.json", "r") as file:
        rememberlist = json.load(file)
        file.close()
        for i in rememberlist:
            if not rememberlist[i]:
                return True
        return False

def update():
    with open("data/date.txt", "w") as file_w:
        file_w.write(str(date.today()))
        file_w.close()
    
    with open("data/rememberlist.json", "r") as file:
        rememberlist = json.load(file)
        for i in rememberlist:
            rememberlist[i] = False
        file.close()
    with open("data/rememberlist.json", "w") as file:
        json.dump(rememberlist, file)
        file.close()

def remember():
    sleep(20)
    playsound.playsound("sounds/sound.mp3")
    run()

def check_date():
    with open("data/date.txt", "r") as file_r:
        if str(date.today()) != file_r.read():
            return True
        else:
            return False

def get_time():
    with open("data/time.txt", "r") as file:
        time = file.read()
        file.close()
    with open("data/times.json", "r") as file:
        times = json.load(file)
        seconds = times[time]
        file.close()
    return seconds
