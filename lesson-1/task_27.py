#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    k = 0
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_on_the_right():
                fill_cell()
        for i in range(k):
            if not wall_is_on_the_right():
                move_right()
        k+=1





if __name__ == '__main__':
    run_tasks()


