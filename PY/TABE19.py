def mohasebe(list):
    a=0
    b=0
    c=0
    for i in list:
        if i <3:
            a+=1
        elif 3<=i<10:
            b+=1
        elif i>10:
            c+=1
        else:
            return 'value is wrong please enter valid values'
    return f'kootah={a}  motevaset={b}  toolani={c}'
print(mohasebe([19,6,1,7]))
        