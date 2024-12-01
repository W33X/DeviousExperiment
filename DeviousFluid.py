import os
import sys
import time
import random

sizeX = os.get_terminal_size()[0]
sizeY = os.get_terminal_size()[1]

screen = []

def init():
    for Y in range(sizeY):
        temp = ""
        for X in range(sizeX):
            temp += " "
        screen.append(temp)

def replace(string, coordinate, new_char):
    temp_replace = string[:coordinate]
    temp_replace += new_char
    temp_replace += string[(coordinate + 1):]
    return temp_replace

