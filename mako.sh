#Wrapper for brightening up my day
#!/bin/bash

mako () { notify-send -i ~/Pictures/Personal/Emotes/mako.png "Mako Time" "      Woof"; }

case $1 in
   bomb)
      for i in {1..110}; do mako; done
   ;;
   *)
      mako
   ;;
esac
