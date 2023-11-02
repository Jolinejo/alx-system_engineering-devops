#!/bin/bash
#curling
URL=$1
curl -sI $URL | grep -i Content-Length | awk '{print $2}'
