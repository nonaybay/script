#!/usr/bin/python


from os import system
from sys import argv
from time import sleep


def perform(code):
    system('clear')
    print('')
    print('-- Running sudo {}'.format(code))
    print('')
    sleep(1)
    system('sudo {}'.format(code))
    sleep(2)
    system('clear')


perform('apt-get update')
perform('apt-get install --yes --fix-missing --fix-broken')

if len(argv) > 1:
    for pkg in argv[1:]:
        perform('apt-get install --yes --fix-missing --fix-broken {}'.format(pkg))
else:
    pass

perform('apt-get upgrade --yes')
perform('apt-get full-upgrade --yes')
perform('apt-get dist-upgrade --yes')
perform('apt-get autoremove --yes')
perform('apt-get clean --yes')

sleep(3)

alternative = input('Reinstall -- tasksel -- ? [Y/N (default)]')

if (alternative == 'Y') or (alternative == 'y'):
    perform('apt-get purge --yes tasksel')
    perform('apt-get install --yes --fix-missing --fix-broken tasksel')

