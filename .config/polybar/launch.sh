#!/usr/bin/bash

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -x polybar >/dev/null; do sleep 1; done

# Launch top and bottom with custom theme
if [[ $# -ne 1 ]]; then
	polybar top &
	echo "WARNING: No theme applied to polybar"
else
polybar -c $HOME/.config/polybar/themes/$THEME top &
fi 

echo "Bars launched..."
