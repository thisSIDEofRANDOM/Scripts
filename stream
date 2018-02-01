#Simple Wrapper for streamlink
#!/bin/bash
#streamlink launcher for desktop layout

if [ $# -lt 1 ]; then
   echo "Usage: stream <streamname> <pos - bl,br>"
   exit
fi

case $2 in
   tl)
      LOCATION="--geometry=958x522+0+0"
   ;;
   tr)
      LOCATION="--geometry=961x522+959+0"
   ;;
   bl)
      LOCATION="--geometry=958x526+0+554"
   ;;
   *)
      LOCATION="--geometry=961x526+959+554"
   ;;
esac

streamlink twitch.tv/$1 ${2:-best} -p "mpv --title $1 --mute=yes --cache=4096 --no-border --ontop $LOCATION"
