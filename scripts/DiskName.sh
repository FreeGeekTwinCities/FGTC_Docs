#! /bin/bash
echo -n "Enter your name: "
read -e NAME
dcfldd textpattern=$NAME of=/dev/fd0
echo "I've written $NAME to the floppy about a BAJILLION times!"
