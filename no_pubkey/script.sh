#!/bin/bash

gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv $1
gpg --export --armor $1 | sudo apt-key add -
