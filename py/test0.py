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
<form action='test0.py' method='GET'>
"""
for x in scrambledict:
    html+="<input type='button' name='click0' value='"+x+"'>"
    html+="<input class='styled' type='button' name='click1' value='"+scrambledict[x]+"'>"
html+="<input type='submit' name='submit'>"
html+="</form>"

data=cgi.FieldStorage()
if ('click0' in data):
    click0 = data['click0'].value
else:
    click0='1'
if ('click1' in data):
    click1 = data['click1'].value
else:
    click1='a'
testdict={}
testdict[click0]=click1
if testdict[click0] in answerdict:
    html+='<p>Correct!</p>'

html+= '<br><a href="test0.html">Try Again</a>'
html+= HTML_FOOTER
print(html)
