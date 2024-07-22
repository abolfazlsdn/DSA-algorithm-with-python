def sumOfDigit(n):
    assert int(n)==n and n>=0,"n number must be intiger and positive"
    if n==0:
        return 0 
    else:
        return int(n%10) + sumOfDigit(n/10)

print(sumOfDigit(1234))