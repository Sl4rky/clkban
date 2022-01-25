#!usr/bin/python3

"""A simple kanban board in python"""

from __future__ import annotations
import curses
from curses import wrapper


def drawscr(stdscr: curses.window) -> None:
    """Prints screen frame"""
    stdscr.addstr(f"{type(stdscr)}")


def main(stdscr):
    """main function"""
    stdscr.clear()

    drawscr(stdscr)
    stdscr.refresh()
    stdscr.getch()



if __name__ == '__main__':
    wrapper(main)
