#!/bin/bash

export BUILD_DATE=$(date +%Y-%m-%d)

case $1 in
    build)
        docker compose up --build -d
        ;;
    
    up)
        docker compose up -d
        ;;
    
    down)
        docker compose down
        ;;
    
    stop)
        docker compose stop
        ;;
    
    start)
        docker compose start
        ;;
    
    restart)
        docker compose restart
        ;;

    *)
        echo "Usage: $0 {build|up|down|stop|start|restart}"
        exit 1
        ;;
esac