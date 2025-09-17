

def palidrome(s):
    i1 = 0
    i2 = len(s) - 1

    while i1 < i2:
        if s[i1] != s[i2]:
            return False
        i1 += 1
        i2 -= 1
        
    return True

s = "kevin"
print(palidrome(s))