#!/usr/bin/env python

import requests
import re

user = 'natas1'
passw = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'  # from previous level
url = 'http://%s.natas.labs.overthewire.org' % user

r = requests.get(url, auth=(user, passw))


# 1st step:  print the sourcecode
'''
#print(r.text)
'''
# OUTCOME:  it seems that the password is in the sourcecode in plaintext again

# 2nd Step:  extract the password from the sourcecode
webPage = r.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())


