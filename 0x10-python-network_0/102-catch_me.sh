#!/bin/bash
# trying cool stuff
curl -X POST -s 0.0.0.0:5000/catch_me --data "user_id=1000" -H "Content-Type: application/x-www-form-urlencoded" --location
