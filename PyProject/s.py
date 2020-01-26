import re

x = '(time < 50) or (qty < 7)'
y = x.split(')')
print(y)

s = '(time < 50) or (qty < 7) and (abc > 10 )'
result = re.search('\((.*)\)', s)
print(result.group(1))


result2 = re.split('\(|\)',s)
str_list = list(filter(None, result2))
print(str_list )

