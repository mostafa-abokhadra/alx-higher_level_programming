#!/usr/bin/env bash
# takes url arg, send request, and display size of response
curl -i $1 | grep Accept-Ranges: >> file.txt
cat file.txt
