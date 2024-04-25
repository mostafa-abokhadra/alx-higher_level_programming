#!/bin/bash
# all method http accept
curl -s -i "$1" | grep "Allow:" | cut -d" " -f2-
