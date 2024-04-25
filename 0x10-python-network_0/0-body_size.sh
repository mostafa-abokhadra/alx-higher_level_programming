#!/usr/bin/env bash
# takes url arg, send request, and display size of response
curl -i $1 | grep Content-Length: | cut -b 16-
