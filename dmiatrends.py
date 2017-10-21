# ребята, я не забыл
# мож завтра еще пришлю =)

#1
def power_sum(l,r,p = 1.0):
    i = l
    mysum = 0
    while i <= r:
        mysum += i ** p
        i += 1
    return mysum

#2
def solve_equation(a,b,c):
	if a == 0 & b == 0 & c == 0:
		print('inf')
	else:
		D = b*b - 4*a*c
		if D > 0:
			return ((-b - D ** 0.5)/(2*a),
				(-b + D ** 0.5)/(2*a))
		elif D == 0:
			return -b / 2 / a
		else:
			return None

#3
