#Recursively git pull files under given dir:
#!/bin/bash

GITDIR="${HOME}/Documents/github"

for i in ${GITDIR}/*
do
   echo "Checking $i..."
   if [ ! -v ${1} ]; then
      GIT_SSH_COMMAND="ssh -o ConnectTimeout=1" git -C ${i} pull
   else
      git -C ${i} pull
   fi
done
