LoginGenerator
==============

A simple login generator that outputs a username, password and valid e-mail address

Usage:

python generatePolLogin.py testlogins.txt NDLogins.tab NDLogin

python generatePolLogin.py testlogins.txt NDLogins.tab passwordPlease

python generatePolLogin.py testlogins.txt NDLogins.tab random

python generatePolLogin.py testlogins.txt NDLogins.tab RANDOM

Usage must be satisfied on the command line. Inputting a file that is simple a list of e-mail addresses is the strict
format required. This will peel a domain off the address, and based off the need for a strictly formed password or a
randomly generated password will output both with the original address and be saved locally as a tab file.

