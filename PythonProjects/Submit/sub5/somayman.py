import math

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0: return False
    return True

def plus_digit_in_number(n):
    sn = 0
    for digit in str(n):
        sn += int(digit)
    return sn
#ktra co la so khong
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def findLuckyNumber(filename):
    f = open(filename, "r", encoding="utf-8")
    # print(f.read())
    number = f.read().split()
    for num in number:
        if is_number(num):
            # print(num)
            if is_prime(int(num)):
                # print(num, plus_digit_in_number(int(num)))
                if plus_digit_in_number(int(num)) % 5 == 0:
                    return int(num)
    return None



    # f = open(filename, "r", encoding="utf-8")
    # # print(f.read())
    # number = f.read().split()
    # res = 0
    # for num in number:
    #     if is_number(num):
    #         # print(num)
    #         if is_prime(int(num)):
    #             # print(num, plus_digit_in_number(int(num)))
    #             if plus_digit_in_number(int(num)) % 5 == 0:
    #                 res = int(num)
    # return res



#     import math


# def findLuckyNumber(filename):
#     with open(filename, "r", encoding="utf8") as f:
#         x = f.read().split()
#     res = -1
#     for i in range(len(x)):
#         if(x[i].isnumeric()):
#             if isPrime((int)(x[i])):
#                 if isLucky((int)(x[i])):
#                     res = (int)(x[i])
#     return res

# def isPrime(n):
#     if n < 2: return False
#     elif n == 2: return  True
#     else:
#         last = int(math.sqrt(n)) + 1
#         for i in range(2, last):
#             if n % i == 0: return False
#     return True

# def isLucky(n):
#     res = 0
#     while(n!=0):
#         res = res + n%10
#         n = n//10
#     if(res%5 == 0): return True
#     else: return False

# #print("1009".isnumeric())