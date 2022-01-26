#!usr/bin/python3

"""A simple kanban board in python"""

from __future__ import annotations
import curses
from curses import wrapper
from enum import Enum

class Status(Enum):
    """Window Enum"""
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2

def drawscr(windows: list) -> None:
    """Prints screen frame"""
    for window, title in windows:
        window.refresh()
        window.attron(curses.A_BOLD)
        window.border(0, 0, 0, 0, 0, 0, 0, 0)
        window.addstr(title)
        window.refresh() 


def main(stdscr):
    """main function"""
    height, width = stdscr.getmaxyx()

    # setup windows
    todo_win = curses.newwin(height, width//3, 0, 0)
    in_progress_win = curses.newwin(height, width//3, 0, width//3 + 1)
    done_win = curses.newwin(height, width//3, 0, 2*width//3 + 1) 
    windows = [[todo_win, 'To Do'],
               [in_progress_win, 'In Progress'],
               [done_win, 'Done']]
    todo_items = [{"task": "Walk the dog", "status": Status.TODO}]

    # screen draw loop
    drawscr(windows)
    todo_win.getch()



if __name__ == '__main__':
    wrapper(main)
