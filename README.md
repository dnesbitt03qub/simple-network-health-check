# simple-network-health-check
Just a simple script outputing pings to a csv, for the purposes of checking the health of a network over time.

This might be useful if your wifi is lagging or you have intermittent disconnections and you want to diagnose issues on your network. Set this script running on a Raspberry Pi connected via ethernet and one on wifi to isolate where the issue is.

The output of the program is a log of the timestamp, if the machine can access a certain host and the ping time for that host

## TODO
Add graphing to visualize status over time
