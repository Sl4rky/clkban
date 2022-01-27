#!usr/bin/python3

"""A simple kanban board in python"""

from __future__ import annotations
import curses
from curses import wrapper, window


class ListWindow:
    """List window object"""
    def __init__(self, window: curses.window, col_offset: int,
                title: str, items: list):
        self.window = window
        self.title = title
        self.items = items
        self.col_offset = col_offset
        self.height, self.width = self.window.getmaxyx()
        self.pad = curses.newpad(100, 100)

    def render_window(self):
        """renders window object"""
        self.window.erase()

        # render outline and title
        self.window.attron(curses.A_BOLD)
        self.window.border(0, 0, 0, 0, 0, 0, 0, 0)
        self.window.addstr(self.title)
        self.window.refresh()

        # render textpad
        for i, item in enumerate(self.items):
            self.pad.addstr(i, 1, f'- {item}')
    
        self.pad.refresh(0, 0,
                        1, self.col_offset,
                        self.height - 2,
                        self.col_offset + self.width - 4)


def main(stdscr):
    """main function"""
    height, width = stdscr.getmaxyx()

    # item lists
    todo_items = ['get a life']
    in_progress_items = []
    done_items = []

    # setup windows
    todo_win = ListWindow(curses.newwin(height, width//3, 0, 0),
                    1,
                    'To Do',
                    todo_items)
    in_progress_win = ListWindow(curses.newwin(height, width//3, 0, width//3),
                    (width//3) + 1,
                    'In Progress',
                    in_progress_items)
    done_win = ListWindow(curses.newwin(height, width//3, 0, 2*width//3),
                    (2 * width//3) + 1,
                    'Done',
                    done_item
    windows = [todo_win, in_progress_win, done_win]

    # screen draw loop
    stdscr.refresh()

    for lwin in windows:
        lwin.render_window()

    todo_win.window.getch()


if __name__ == '__main__':
    wrapper(main)
