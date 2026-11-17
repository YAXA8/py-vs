3:
def taraz(ln):
    gh=0
    k=0
    h=0

    for i in ln:
        if i>=10:
            gh+=1
    maxclass=max(ln)    
    print(gh)
    print(maxclass)
    mr=len(ln)-gh
    minclass=min(ln)
    print(minclass)
    
    for i in ln:
        h=i+h    
    miangin=h/len(ln)
    print(miangin)
    return gh, maxclass, mr, minclass, miangin
taraz([3,22,14,2,432,5,6,7,8,9,10,11,12,13,14,15])