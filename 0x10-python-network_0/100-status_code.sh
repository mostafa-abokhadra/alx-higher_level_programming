#!/bin/bash
# showing status code only
curl -sLX HEAD -w "%{http_code}" "$1"
