j = []
for i in range(1,100):
    if(i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))