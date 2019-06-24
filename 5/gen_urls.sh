#! /bin/bash

base_url="http://www.pythonchallenge.com/pc/def/"
ext=".$1"
DISPLAY=:0

tail -n 3 req.log.bkp | grep -Po "\d+$" | for i in $(cat); do echo $base_url$i$ext; done | tee - | DISPLAY=:0 xargs firefox --new-tab {}


head -n 3 req.log | grep -Po "\d+$" | for i in $(cat); do echo $base_url$i$ext; done | tee - | DISPLAY=:0 xargs firefox --new-tab {}
