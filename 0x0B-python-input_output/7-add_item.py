#!/usr/bin/python3
"""load add and save module"""
import sys
import os

save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

listy = []

if os.path.exists("add_item.json"):
    listy = load_from("add_item.json")
for i in range(1, len(sys.argv)):
    listy.append(sys.argv[i])
save_to(listy, "add_item.json")
