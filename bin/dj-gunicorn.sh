#!/usr/bin/env bash

cd src

# Run guniconr to start app
gunicorn app.wsgi
