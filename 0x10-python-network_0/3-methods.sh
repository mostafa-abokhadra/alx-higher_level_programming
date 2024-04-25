#!/bin/bash
# all method http accept
curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d" " -f2
