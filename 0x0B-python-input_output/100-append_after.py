#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    counter = 0
    line = ""
    with open(filename, mode='r+', encoding='utf-8') as fily:

