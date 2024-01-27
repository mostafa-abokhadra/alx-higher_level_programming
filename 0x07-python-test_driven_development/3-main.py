#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name





print("======================")
say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
try:
    say_my_name("messi_i3s_the_best", "ok")
except Exception as e:
    print(e)
try:
    say_my_name("moasta4444fa", "abokh6666adra")
except Exception as e:
    print(e)
try:
    say_my_name("moastafa", "abokh6666adra")
except Exception as e:
    print(e)

