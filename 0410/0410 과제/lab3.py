# 함수를정의한다. 
def f(x):
    return(x**2-x-1)
def bisection_method(a, b, error):
    if f(a)*f(b) > 0:
        print("구간에서근을찾을수없습니다.")
    else:
        while(b -a)/2.0> error: # 오차를계산한다. 
            midpoint = (a + b)/2.0 # 중점을계산한다. 
            if f(midpoint) == 0:
                return(midpoint) 
            elif f(a)*f(midpoint) < 0: 
                    b = midpoint
            else:
                a = midpoint
        return(midpoint)
answer = bisection_method(1, 2, 0.0001)

print("x**2-x-1의근:", answer)
