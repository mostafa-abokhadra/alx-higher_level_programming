#!/bin/bash
# takes in url, send get request, display if OK
curl -i $1 >> file.txt
line=$(head -n 1 file.txt)
state=$(echo "$line" | cut -d " " -f2)

echo "===================="
if [ $state -eq "200" ]; then
	echo "successful!"
	cat file.txt
fi
