#!/usr/bin/env python

import requests
import re

user = 'natas11'
passw = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'  # from previous level
url = 'http://%s.natas.labs.overthewire.org' % user


# 1st step:  print the sourcecode
'''
r = requests.get(url, auth=(user, passw))
print(r.text)
'''

session1 = requests.Session()
# 2nd step: Let's look at the cookies
'''
r = session1.get(url, auth=(user, passw))
print(r.cookies.get_dict())
'''


# 3rd step: Let's post something using the form
'''
r = session1.post(url, auth=(user, passw), data={"bgcolor":"#fffabc"})
print(r.cookies.get_dict())
'''


# 4th step: Inspect the sourcecode
'''
r = session1.get(url + '/index-source.html', auth=(user, passw))
print(r.text)
'''
#include the diagram in here


import base64
# 5th step: xor'ing input and output
'''
key = ""
plaintext = '{"showpassword":"no","bgcolor":"#ffffff"}'
ciphertext = base64.b64decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=').decode()
for c1, c2 in zip(ciphertext, plaintext):
    key += chr( ord(c1) ^ ord(c2) )
print(key)
'''
# key is qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq


# 6th step: crafting the necessary cookie and getting the password
'''
key = ""
plaintext = '{"showpassword":"yes","bgcolor":"#ffffff"}'
ciphertext = "qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8J" # expand the key a little bit more, just to be safe ('yes' is longer than 'no')
for c1, c2 in zip(ciphertext, plaintext):
    key += chr( ord(c1) ^ ord(c2) )
print(base64.b64encode(key.encode()).decode())
'''
#cookie to set = ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK


#7th step:
'''
cooky = dict(data='ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK')
r = session1.post(url, auth=(user, passw), cookies = cooky)
webPage = r.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())
'''
