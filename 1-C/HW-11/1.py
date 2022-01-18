import re

s = re.split(r'\W' , '100,000,000.000' )
for i in s:
    print(i)