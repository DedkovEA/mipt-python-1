#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():

    def func():
        move_right()
        fill_cell()
        move_down()
        fill_cell()
        move_down()
        fill_cell()
        move_left()
        move_up()
        fill_cell()
        move_right()
        move_right()
        fill_cell()
        move_left()
        move_left()
        move_up()


    move_down()
    move_right()
    func()





if __name__ == '__main__':
    run_tasks()


