#!/bin/bash

for i in $(ls /root/notes2/)
do
	nohup python /root/notes2/$i > /dev/null 2>&1 &
done
