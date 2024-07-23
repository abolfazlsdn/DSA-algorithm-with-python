def decimalToBinery(n):
    assert int(n)==n ,"n must be intiger only"
    if n == 0:
        return 0 
    else: 
         return n%2 +10*decimalToBinery(int(n/2))

print(decimalToBinery(-10.6))