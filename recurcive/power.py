def power(base,exp):
    assert int(exp)==exp and exp>=0,"the exponnet must be positive and intiger only! " 
    if exp ==0:
        return 1
    if exp ==1:
        return base
    return base * power(base,exp-1)

print(power(2,3))