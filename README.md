# simple-network-health-check
Just a simple script outputing pings to a csv, for the purposes of checking the health of a network over time.

This might be useful if your wifi is lagging or you have intermittent disconnections and you want to diagnose issues on your network. Set this script running on a Raspberry Pi connected via ethernet and one on wifi to isolate where the issue is.

The output of the program is a log of the timestamp, if the machine can access a certain host and the ping time for that host

## Usage
```python3 main.py```

Start logging pings

```python3 main.py computername_wifi```

Start logging pings to computername_wifi.csv

```python3 ploy_graphs.py computername_wifi computername2_ethernet```

Plot a graph for pings for computername_wifi and computername2_ethernet
