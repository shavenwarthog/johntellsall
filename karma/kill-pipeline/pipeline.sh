#!/bin/bash

# pipeline.sh -- start workflow; restart if jammed


while true; do

    date '+%X workflow starting'
    (sleep 30; echo gin) &
    (sleep 30; echo tonic) &

    date '+%X waiting for workflow to complete'
    sleep 5

    # count number of child procs (ie: workflow procs)
    # If there are any, kill them then restart.
    if pgrep -cP $$ > /dev/null ; then 
	    date '+%X workflow jammed -- restarting; trying again'
        pkill -P $$
        sleep 2
        continue
    fi

	date '+%X workflow done!'
    break

done

