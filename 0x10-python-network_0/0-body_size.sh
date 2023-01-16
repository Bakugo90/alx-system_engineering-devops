#!/bin/bash env
#Connect to an url and display the size of body header

url=$1
response=$(curl -s -o /dev/null -w "%{size_download}" $url)
echo "$response"