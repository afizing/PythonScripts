# fibonacci numbers which are divisable by 2. 
def divbytwo(func):
    def divisableby(x):
        return [f for f in func(x) if f%2==0]
    return divisableby

# fibonacci function generates series of fibonacci numbers
@divbytwo
def fibonacci(x):
    # print("Hello")
    l =[1,1]
    if x<=1:
        return [1]
    if x<=2:
        return [1,1]
    if x>2:
        a,b=1,1
        for i in range(2,x):
            a, b = b, a+b
            l.append(b)
        return l



print(fibonacci(10))
            
            
    
    
