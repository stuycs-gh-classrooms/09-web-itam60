#!/usr/bin/python3
print("Content-type: text/html\n")

from random import random
r=random()
print('''
<html>
<head><title>random w38</title></head>
<body style='background-color:springgreen';>
<p>
Lucky number: ''',r,'''
<a href="https://stuy.enschool.org">Click here!</a>
</p>
</body>
</html>''')