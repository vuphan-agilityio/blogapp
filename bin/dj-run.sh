#!/usr/bin/env bash
PORT=$1

if [ "$PORT" = "" ]; then
    PORT='8000'
fi

bin/dj.sh runserver 0.0.0.0:$PORT