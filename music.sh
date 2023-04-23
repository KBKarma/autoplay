#!/bin/bash

setterm -cursor off
setterm -clear

for file in $1/*
do
 omxplayer "$file" > /dev/null
done

setterm -cursor on