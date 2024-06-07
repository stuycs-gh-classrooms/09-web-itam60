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
boxpair=1
while boxpair<4:
    pairnum=str(boxpair)
    tempterm='term'+pairnum
    if tempterm in data:
        tempterm=data['term'+pairnum].value
    else:
        tempterm=pairnum
    tempdef='def'+pairnum
    if tempdef in data:
        tempdef=data['def'+pairnum].value
    else:
        tempterm=answerdict[pairnum]
    answerdict[tempterm]=tempdef
    boxpair+=1
        
#testdict={}
#testdict[click0]=click1
#if testdict[click0] in answerdict:
    #html+='<p>Correct!</p>'
html+=str(answerdict)
html+= HTML_FOOTER
print(html)