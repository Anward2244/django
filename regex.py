import re


a = '8302167307'

b = re.match(r"[89][0-9]{9}", a)

print(b)