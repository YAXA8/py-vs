def maxf(a,b,c,d):
    if a>b:
        if a>c:
            if a>d:
                return a
            else:
                return d
        elif c>a:
            if c>d:
                return c
            else:
               return d
    elif b>a:
        if b>c:
            if b>d:
                return b
            elif d>b:
                return d
        elif c>b:
            if c>d:
                return c
            elif d>c:
                return d
a=float(input('    give a   '))
b=float(input('   give b     '))
c=float(input('    give c   '))
d=float(input('    give d    '))
print(maxf(a,b,c,d))