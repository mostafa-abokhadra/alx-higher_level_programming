#!/usr/bin/python3
for i in range(97, 123):
    if int(i) == 'q' or int(i) == 'e':
        continue
    print("{:c}".format(i), end = "")
