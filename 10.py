def karatsuba(x, y):
    
    if x < 10 or y < 10:
        return x * y

  
    n = max(len(str(x)), len(str(y)))
    m = (n + 1) // 2  

   
    A = x // 10**m
    B = x % 10**m
    C = y // 10**m
    D = y % 10**m

    
    AC = karatsuba(A, C)
    BD = karatsuba(B, D)
    ADplusBC = karatsuba(A + B, C + D) - AC - BD

    
    result = AC * 10**(2 * m) + ADplusBC * 10**m + BD
    return result


x = 3456
y = 5678
print("Karatsuba result:", karatsuba(x, y))