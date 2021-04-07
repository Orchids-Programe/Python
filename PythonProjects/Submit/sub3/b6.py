text = 'lua nep la lua nep nuong lua len lop lop long nang lang lang'
# wordCount = {}
# for w in text.split(' '):
#     wordCount[w] = wordCount.get(w, 0)+1
count = [0]*256
max = -1
c = ' '
for i in text.split(' '):
    count[ord(i)] += 1
for i in text.split(' '):
    if max < count[ord(i)]:
        max = count[ord(i)]
        c = i
print(c, max)
print(wordCount)