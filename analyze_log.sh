#!/bin/bash
# analyze_log.sh - summarise transit_session.log

LOG="${1:-transit_session.log}"

if [ ! -f "$LOG" ]; then
    echo "Error: file '$LOG' not found."
    exit 1
fi

sessions=$(grep -c "New session started" "$LOG")
zebra_stops=$(grep -c "Waiting at the zebra crossing... 0s left" "$LOG")
lane_changes=$(grep "Lane changes" "$LOG" | awk -F: '{s += $NF} END {print s + 0}')

driver=$(grep "Driver  " "$LOG" | tail -1 | awk -F: '{print $NF}' | xargs)
top_speed=$(grep "Top speed" "$LOG" | tail -1 | awk -F: '{print $NF}' | xargs)

echo "===== LOG SUMMARY ($LOG) ====="
echo "Sessions (runs)     : $sessions"
echo "Zebra crossing stops: $zebra_stops"
echo "Lane changes        : $lane_changes"
echo "Latest driver       : ${driver:-N/A}"
echo "Latest top speed    : ${top_speed:-N/A}"
