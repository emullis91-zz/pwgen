#!/usr/bin/python
from sys import argv, exit

try:
    src = open("/dev/urandom")
except IOError:
    print "`urandom` device not found."
    print "Either you are not on a Unix-like OS,",
    print "or you have severely messed something up."
    print exit(1)

validchars = ['abcdefghijklmnopqrstuvwxyz',
              'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              '1234567890',
              '_+=-?!@$&*']

if len(argv) > 2:
    n = int(argv[2])
else:
    n = 1

for arg in xrange(n):
    pw = ""
    while len(pw) < int(argv[1]):
        c = src.read(1)
        if c in ''.join(validchars): pw += c
    print pw
