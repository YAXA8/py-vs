
def passcheck(password):
    meow=0
    h=0
    k=0
    j=0
    if len(password)>8:
        j+=1
        for i in password:
            for x in range(0,10):
                if i==str(x):
                    k+=1
        if k!=len(password) and k!=0:
            j+=1
            h+=1
        if h==1:
            for v in password:
                for p in ['!','@','#','$','%']:
                    if v==p:
                        j+=1
                        meow=1
                        break
                if meow==1:
                    break
    if j==0:
        return('weak')
    elif j==1:
        return('medium')
    elif j==2:
        return('good')
    elif j==3:
        return('strong')





password=input('write your password')
print(f'your password is {passcheck(password)}')