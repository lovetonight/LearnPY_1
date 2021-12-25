import re
regex1=re.compile(r'anh (.*) dep')
demo='''anh Luan dep trai
anh Linh dep trai nua
anh Hoan dep trai nua'''
kq=regex1.findall(demo)
#name=kq.group(0)
print(kq[1:3])