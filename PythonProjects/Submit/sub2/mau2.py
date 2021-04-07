#Đếm số số từ trong văn bản
def wordCount(s):
    token = s.split(' ')
    w = []
    c = []
    for t in token:
        if t not in w:
            w.append(t)
            c.append(count(t, token))
    return w,c
def count(w, token):
    count = 0
    for t in token:
        if w == t:
            count += 1
    return count
text = 'Lua nep la lua nep lang lua len lop lop long nang lang lang'
words, counts = wordCount(text)
for i in range(0, len(words)):
    print(words[i],':',counts[i])