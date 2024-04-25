#!/bin/bash
# showing status code only
curl -sL -X HEAD -w "%{http_code}" "$1"
