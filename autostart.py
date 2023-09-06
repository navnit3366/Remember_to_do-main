from threading import Thread
from time import sleep
from functions import *

def infinit_run(seconds):
    if check_date():
        update()
        remember()
    elif check_remember():
        remember()
    else:
        ...
    while True:
        if check_remember():
            sleep(seconds)
            remember()
        else:
            break

with open("data/rememberlist.json", "r") as file:
    if not file.read() == {} or "":
        main_thread = Thread(target=infinit_run, args=(get_time(),))
        main_thread.start()
