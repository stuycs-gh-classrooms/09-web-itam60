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


data = cgi.FieldStorage()
if ('terms' in data):
    terms = data['terms'].value
else:
    terms='a,b,c,d'
if ('definitions' in data):
    definitions = data['definitions'].value
else:
    definitions='1,2,3,4'
html=HTML_HEADER
#html+= guess
#html+= """
#</title>
#</head>
#"""
html+="<h1>Quiz below</h1>"+"\n"
termslist=terms.split(',')
deflist=definitions.split(',')
e=0
answerdict={}
while e<len(termslist):
    answerdict[termslist[e]]=deflist[e]
    e+=1
i0=0
i1=0
scrambledict={}
while len(termslist)>0:
    i0=random.randint(0,len(termslist)-1)
    i1=random.randint(0,len(deflist)-1)
    scrambledict[termslist.pop(i0)]=deflist.pop(i1)
html+="""
<form action='test1.py' method='GET'>
"""

for x in scrambledict:
    html+="<h2>Term:"+x
    html+="<input type='text' name='"+x+"'><br>"
html+="<input type='submit' name='submit'>"
html+="</form>"

html+= '<br><a href="test0.html">Try Again</a>'
html+= HTML_FOOTER
print(html)
