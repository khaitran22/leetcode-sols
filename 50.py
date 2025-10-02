# %%
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n < 0:
        return round(1 / myPow(x, -n), 5)
    else:
        first_pow = n // 2
        result = myPow(x, first_pow)
        return myPow(x, first_pow) * myPow(x, n -  first_pow)

print(myPow(2.00000, 10))

# %%
import math
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    elif n == 1:
        return x
 
    neg = False if n > 0 else True
    if neg:
        n =-n

    out = x
    num_power = math.floor(math.log2(n))
    num_times = 1
    for i in range(num_power):
        out = out * out
        num_times = num_times + num_times
    
    out = out * myPow(x, n - num_times)
    
    if out != 0:
        if neg and out != 0:
            out = 1 / out

        return out

    return 0

print(myPow(0.25519, -6))
# %%
import math
math.floor(math.log2(2147483647))
# %%
