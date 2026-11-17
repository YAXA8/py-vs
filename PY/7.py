def ave(a,b,c):
    average = (a + b+ c)/3
    minn= min(a,b,c)
    maxx = max(a,b,c)
    return average, minn, maxx
a = ave(12,13,14)
print(a)