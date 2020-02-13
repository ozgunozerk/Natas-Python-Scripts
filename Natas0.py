#!/usr/bin/env python

import requests
import re

user = 'natas0'
passw = 'natas0' # this is given
url = 'http://%s.natas.labs.overthewire.org' % user

r = requests.get(url, auth=(user, passw))


# 1st step:  print the sourcecode
'''
#print(r.text)
'''
# OUTCOME:  it seems that the password is in the sourcecode in plaintext


# 2nd Step:  extract the password from the sourcecode
webPage = r.text
matchObject = re.search('[a-zA-Z0-9]{32}', webPage)  # we know that the password has length of 32 chars and consisting of alphanum
print(matchObject.group())