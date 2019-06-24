#! /bin/bash

name=$1
ext=$2

if [ -z $ext ]
then
	ext=html
fi

url="http://www.pythonchallenge.com/pc/def/$name.$ext"
echo opening $url

#DISPLAY=:0 firefox --new-tab $url & >/dev/null

curl -s $url -D - | head -n 1

