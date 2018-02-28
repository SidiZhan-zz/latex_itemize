'''
from indented text to latex itemize block
'''
import re
fil = open('itemize.txt','r')
text = fil.readlines()
begin = '\\begin{itemize}\n'
end = '\\end{itemize}\n'
item = '\\item '
par = ' \\par '
lis = [begin]
num0 = 0
for line in text:
    t = re.search('^\t*',line).group(0)
    num = len(re.findall('\t',t))
    if num0 == num:
        lis.append(t+'\t'+item+re.split('^\t*',line).pop() + par)
    elif num0 < num:
        lis.append(t+begin)
        lis.append(t+'\t'+item+re.split('^\t*',line).pop() + par)
    elif num0 > num:
        for i in range(num0,num,-1):
            nt = ''.join(['\t' for j in range(i)])
            lis.append(nt+end)
        lis.append(t+'\t'+item+re.split('^\t*',line).pop() + par)
    num0 = num
##    print line, t, num0, num, t+item+re.split('^\t*',line).pop()
for i in range(num0,-1,-1):
    nt = ''.join(['\t' for j in range(i)])
    lis.append(nt+end)
text1 = ''.join(lis)
print text1
