#!/bin/bash
# all method http accept
curl -i $1 | grep Allow: | cut -b 7-
