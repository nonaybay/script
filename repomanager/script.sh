#!/bin/bash


if [ "$1" == "debian" ]; then
	sudo rm -rfv /etc/apt/sources.list
	sudo cp ./debian.list /etc/apt/sources.list
else
	sudo rm -rfv /etc/apt/sources.list
	sudo cp ./kali.list /etc/apt/sources.list
fi

clear

sudo apt-get update
