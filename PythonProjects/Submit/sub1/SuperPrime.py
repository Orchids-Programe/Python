from math import sqrt
n = int(input())
def Prime(n):
    if n < 2:
        return False
    for i in range (2, int(sqrt(n)+1)):
        if(n % i == 0):
            return False
    return True

    if Prime(n):
        if n < 10:
            print("True")
        else:
            if Prime(int(n/10)):
                print("True")
            else:
                print("False")
    else:
        print("False")
