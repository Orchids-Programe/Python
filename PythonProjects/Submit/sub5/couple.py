def get_ans(str1, str2):
    c = str2[::-1]

    return str1 == c

def findCouple(filename):
    f = open(filename, "r", encoding="utf-8")
    # print(f.read())
    ls = f.read().split()
    for i in range(0, len(ls)):
        for j in range(i + 1, len(ls)):

            # print(ls[i], ls[j], "aaa" == "aaa")
            x = ls[j][::-1]
            y = ls[i][::-1]
            if ls[i] != y and ls[j] != x:
                if get_ans(ls[i], ls[j]):
                    # print("dcm")
                    if ls[i] > ls[j]: return ls[j], ls[i]
                    else: return ls[i], ls[j]
    return 'None', 'None'




# def findCouple(filename):
#     with open(filename,"r", encoding="utf8") as f:
#         x = f.read().split()
#     res1 = None
#     res2 = None
#     for i in range(len(x)):
#         for j in range(len(x)):
#             if(isreverse(x[i],x[j])):
#                 res1 = x[i]
#                 res2 = x[j]
#     if(res1.isnumeric()):
#         res11 = str(min((int)(res1),(int)(res2)))
#         res22 = str(max((int)(res1),(int)(res2)))
#     else:
#         if(res1 < res2):
#             res11 = res1
#             res22 = res2
#         else:
#             res11 = res2
#             res22 = res1
#     return res11,res22

# def isreverse(a,b):
#     flag = True
#     if(isContain(a,b)): return False
#     else:
#         a = a[::-1]
#         for i in range(len(a)):
#             if(a[i] != b[i]):
#                 flag = False
#                 break
#     return flag

# def isContain(a,b):
#     if(len(a) != len(b)): return False
#     else:
#         for i in range(len(a)):
#             if(a[i] != b[i]):
#                 return False
#     return True


# #print(isreverse("PYTHON", "NOHTYP"))