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
<title>"""+guess+"""
</title>
</head>
"""

HTML_FOOTER = """
</body>
</html>
"""


data = cgi.FieldStorage()
guess="form?!"
if ('guess' in data):
    guess = data['guess'].value
faveanimal="fish"
if ('faveanimal' in data):
    faveanimal = data['faveanimal'].value

html= HTML_HEADER
#html+= '<body style="background-color: '
#html+= bgcolor + ';">'
html+= '<h1>Hello ' + faveanimal + '</h1>'
html+= '<br><a href="test0.html">Try Again</a>'
html+= HTML_FOOTER
print(html)
