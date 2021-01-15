#!/usr/bin/python3

from os import system
from time import sleep


def script(code):
    system('sudo {}'.format(code))


script('apt-get update')
script('apt-get install --yes --fix-missing --fix-broken')
script('apt-get upgrade --yes')
script('apt-get full-upgrade --yes')
script('apt-get dist-upgrade --yes')
script('apt-get autoremove --yes')
script('apt-get clean --yes')
