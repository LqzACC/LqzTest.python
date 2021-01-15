#！python3
import re
t=open('F:\\代码\\phonenumber.txt',encoding='utf-8')
x=t.read()
matches=[]
phoneindex=re.compile(r'''(
    \d{11}
    )''',re.VERBOSE)
phoneput=phoneindex.findall(x)
print(phoneput)

emailindex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    \.[a-zA-Z]{2,4}
    )''',re.VERBOSE)
#emailput=emailindex.findall(x)
#print(emailput)
for groups in emailindex.findall(x):
    matches.append(groups)
print(matches)
if len(matches)>0:
    #pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))
else:
    print("no")
