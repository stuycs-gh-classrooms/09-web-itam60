#!/usr/bin/python
print('Content-type: text/html\n')

import random
import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Quiz time!</title>
</head>
<body>
"""
HTML_FOOTER = """
</body>
</html>
"""
html=HTML_HEADER
answerdict={'1':'a','2':'b','3':'c','4':'d'}

data=cgi.FieldStorage()
if ('click0' in data):
    click0 = data['click0'].value
else:
    click0='1'
if ('click1' in data):
    click1 = data['click1'].value
else:
    click1='a'
#testdict={}
#testdict[click0]=click1
#if testdict[click0] in answerdict:
    #html+='<p>Correct!</p>'
html+=str(data)
html+= HTML_FOOTER
print(html)