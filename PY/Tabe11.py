def auth(username,password):
    if username =='arthor':
        if password =='1234':
            j='successfull'
            return j
        else :
            d='unsuccessfull'
            return d
    else :
        d='unsucessfull'
        return d
username=input('enter username     ')
password=input('    enter password    ')
print(auth(username,password))
