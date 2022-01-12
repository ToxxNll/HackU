import re

A=int(input())
ar=[]
for i in range(A):
    ar.append(input())

for number in ar:
    if 15>=len(str(number))>=2:
        if re.match(r'[7-9]',number):
            print ('Yes')
        else:
            print ('No')
    else:
        print('Kosyak') 
