#!/usr/bin/python
print('Content-type: text/html\n')

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
terms='a,b,c,d'
definitions='1,2,3,4'

data = cgi.FieldStorage()
#guess="form?!"
#if ('guess' in data):
#    guess = data['guess'].value
#faveanimal="fish"
#if ('faveanimal' in data):
#    faveanimal = data['faveanimal'].value
html=HTML_HEADER
#html+= guess
#html+= """
#</title>
#</head>
#"""
html+="<h1>Quiz below</h1>"+"\n"
termslist=terms.split(',')
deflist=definitions.split(',')
i=0
while i<len(termslist):
    html+=termslist[i]+': '+deflist[i]+'\n'
    i+=1
html+= '<br><a href="test0.html">Try Again</a>'
html+= HTML_FOOTER
print(html)
