import re
value = []
items = [x for x in input('Nhap mat khau : ').split(' ')]

for p in items:
    if len(p) < 8 or len(p) > 100:
        continue
    else:
        pass
    if not re.search('[a-z]', p):
        continue
    elif not re.search('[0-9]',p):
        continue
    elif not re.search('[A-Z]',p):
        continue
    elif not re.search('[~!@#$%^&*]',p):
        continue
    elif re.search('\s',p):
        continue
    else:
        pass
    value.append(p)
print(' '.join(value))