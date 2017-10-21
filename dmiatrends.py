# ребята, я не забыл
# мож завтра еще пришлю =)

def power_sum(l,r,p = 1.0):
    i = l
    mysum = 0
    while i <= r:
        mysum += i ** p
        i += 1
    return mysum
