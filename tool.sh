#!/bin/bash

run() {
    sudo apt-get install -y python3.6
    sudo apt-get install -y python3-pip
    sudo pip3 install --no-cache-dir -r requirements.txt

    nohup python3.6 Telegram.py &
}

pull() {
    git fetch --all
    git reset --hard origin/master
}

push() {
    git add .
    git commit -m "update"
    git push origin
}


if [ "$1" == "run" ]; then
    run

elif [ "$1" == "pull" ]; then
    pull

elif [ "$1" == "push" ]; then
    push

elif [ "$1" == "" ]; then
    echo "run 
pull
push"

fi
