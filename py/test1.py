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

data = cgi.FieldStorage()
if ('terms' in data):
    terms = data['terms'].value
else:
    terms='a,b,c,d'
if ('definitions' in data):
    definitions = data['definitions'].value
else:
    definitions='1,2,3,4'
    
termslist=terms.split(',')
deflist=definitions.split(',')
e=0
answerdict={}
while e<len(termslist):
    answerdict[termslist[e]]=deflist[e]
    e+=1

data=cgi.FieldStorage()
boxpair=0
numright=0
while boxpair<len(termslist):
    searchanswer=termslist[boxpair]
    if searchanswer in data:
        searchanswer=data[searchanswer].value
    else:
        searchanswer='q'
    if answerdict[termslist[boxpair]]==searchanswer:
        numright+=1
    boxpair+=1
html+=str(termslist)
html+="<p> Number Correct: "+str(numright)+"!</p>"
html+= HTML_FOOTER
print(html)