#sinxTaylor
def sinTaylor(x, e):
    result = a
    a = x
    i = 1
    while(a > e):
        a = a * (pow(x,2) / (2*i*(2*i+1)))
        result += a
        i += 1
    a = a * (pow(x,2) / (2*i*(2*i+1)))
    result += a
    print(result)
sinTaylor(x,e)
