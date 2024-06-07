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
terms=['1','2','3','4']
answerdict={}
data=cgi.FieldStorage()
boxpair=0
numright=0
while boxpair<len(terms):
    pairnum=str(boxpair+1)
    searchanswer='answerdef'+pairnum
    if searchanswer in data:
        searchanswer=data[searchanswer].values
    else:
        searchanswer='q'
    if terms[boxpair]==searchanswer:
        numright+=1
    boxpair+=1
html+="<p> Number Correct: "+str(numright)+"!</p>"
html+= HTML_FOOTER
print(html)