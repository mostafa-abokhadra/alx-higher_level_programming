#!/bin/bash
# showing status code only
curl -s -L -X HEAD -w "%{http_code}" "$1"
