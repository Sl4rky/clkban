#!usr/bin/python3

"""A simple kanban board in python"""

from __future__ import annotations
import curses
from curses import wrapper, window


class ListWindow:
    """List window object"""
    def __init__(self, window: curses.window, title: str, items: list):
        self.window = window
        self.title = title
        self.items = items 

    def render_window(self):
        """renders window object"""
        self.window.clear()
        self.window.attron(curses.A_BOLD)
        self.window.border(0, 0, 0, 0, 0, 0, 0, 0)
        self.window.addstr(self.title)
        self.window.refresh()


def main(stdscr):
    """main function"""
    height, width = stdscr.getmaxyx()

    # item lists
    todo_items = []
    in_progress_items = []
    done_items = []

    # setup windows
    todo_win = ListWindow(curses.newwin(height, width//3, 0, 0),
                    'To Do',
                    todo_items)
    in_progress_win = ListWindow(curses.newwin(height, width//3, 0, width//3),
                    'In Progress',
                    in_progress_items)
    done_win = ListWindow(curses.newwin(height, width//3, 0, 2*width//3),
                    'Done',
                    todo_items)
    windows = [todo_win, in_progress_win, done_win]

    # screen draw loop
    stdscr.refresh()

    for lwin in windows:
        lwin.render_window()

    todo_win.window.getch()


if __name__ == '__main__':
    wrapper(main)
