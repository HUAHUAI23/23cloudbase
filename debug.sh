#!/bin/bash
flask_debug() {
    flask --app flaskr run --debug
}
flask() {
    command flask --app flaskr run --debug
}

if [ "$1" == '1' ]; then
    flask_debug
fi

if [ "$#" == '0' ]; then
    flask_debug
fi
