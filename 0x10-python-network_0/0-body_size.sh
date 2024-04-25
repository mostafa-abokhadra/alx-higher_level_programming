#!/bin/bash
# takes url arg, send request, and display size of response
curl -si $1 | grep Content-Length: | cut -b 16-
