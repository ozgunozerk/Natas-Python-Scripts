#!/usr/bin/env python

import requests
import re

user = 'natas8'
passw = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'  # from previous level
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

#encodedSecret = "3d3d516343746d4d6d6c315669563362"
#bin2hex(strrev(base64_encode($secret)))
#a = "==QcCtmMml1ViV3b"[::-1]  # hex to string
#[print(a)]  # base64 decode
# a = "oubWYf2kBq"


# 3rd step:  submit the secret and get password

r = requests.post(url, auth=(user, passw), data= {"secret": "oubWYf2kBq", "submit":"submit"})
webPage = r.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())

