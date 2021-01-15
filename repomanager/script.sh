#!/bin/bash


if [ "$1" == "debian" ]; then
	sudo rm -rfv /etc/apt/sources.list
	sudo cp ./repo/debian.list /etc/apt/sources.list
else
	sudo rm -rfv /etc/apt/sources.list
	sudo cp ./repo/kali.list /etc/apt/sources.list
fi

clear

sudo apt-get update
