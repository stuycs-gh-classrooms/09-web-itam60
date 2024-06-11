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
    terms = data.getvalue('terms')
else:
    terms='a,b,c,d'
if ('definitions' in data):
    definitions = data.getvalue('definitions')
else:
    definitions='1,2,3,4'

termslist=terms.split(',')
deflist=definitions.split(',')
e=0
answerkey={}
while e<len(termslist):
    answerkey[termslist[e]]=deflist[e]
    e+=1

data=cgi.FieldStorage()
answerdict={}
ignore=['submit','terms','definitions']

for x in data:
    if x not in ignore:
        answerdict[x]=data.getvalue(x)
wrongdict={}
numright=0
for x in answerkey:
    if answerkey[x]==answerdict[x]:
        numright+=1
    else:
        wrongdict[x]=answerkey[x]
print(wrongdict)
#html+=str(data)+'<br>'+str(answerdict)+'<br>'+str(answerkey)
html+="<p> Number Correct: "+str(numright)+"!</p><br><p>Keep Practicing:</p>"
html+= HTML_FOOTER
print(html)