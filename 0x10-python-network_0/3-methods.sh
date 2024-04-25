#!/bin/bash
# all method http accept
curl -si $1 | grep "Allow:" | cut -b 7-
