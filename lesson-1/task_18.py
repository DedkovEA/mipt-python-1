#!/usr/bin/python3

from pyrob.api import *


@task(delay = 0.01)
def task_8_28():
    
    while not wall_is_on_the_left():
    	move_left()

    while wall_is_above() and wall_is_beneath():
    	move_right()

    while not wall_is_above():
    	move_up()
    while not wall_is_on_the_left():
    	move_left()	



if __name__ == '__main__':
    run_tasks()

