#!/bin/bash
if [ $# -eq 0 ]; then
    exec /capture_traffic.sh
if [ "$1" = "sh" ]; then
    exec sh -l
elif [ "$1" = "bash" ]; then
    exec bash --login
# else
#     gradle --no-daemon -Pcmdargs=$1:$2 runcmd
fi

# exec /capture_traffic.sh