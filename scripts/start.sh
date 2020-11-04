#!/bin/sh

uwsgi --socket :8000 --master --enable-threads --module todo_app.wsgi
