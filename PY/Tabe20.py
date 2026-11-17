

def fraud(list):
    A=[]
    a=0
    B=[]
    b=0
    c=a+b
    variz=0
    jamvariz=0
    bardasht=0
    jambardasht=0
    meow=0
    vaziat=''
    for i in list:
        if 0<=i['hour']<=5:
            if -10000000<i['amount']>-500000:
                A.append(i)
                a+=1
        elif i['amount'] >=10000000:
            B.append(i)
            b+=1
        if i['amount']>0:
            variz+=1
            jamvariz+=i['amount']
        elif i['amount']<0:
            bardasht+=1
            jambardasht+=i['amount']
    if a+b==0:
        vaziat='safe'
    elif a+b<=2:
        'warning'
    elif a+b>2:
        vaziat='locked'
   
    print(f'vaziate hesab={vaziat}, tedade kole variz ha={variz}, majmooe mabaleghe varizi={jamvariz}, tedade kole bardasht ha ={bardasht}, majmooe mabaleghe bardasht ha ={jambardasht}, tedade tarakonesh haye mashkook={c} be tafkike {a} ta a va {b} ta b ke daghigh hastand : A= {A}      B={B}')
fraud([
    {"amount": -50000, "hour": 14},
    {"amount": 200000, "hour": 10},{"amount": -8000000, "hour": 3}, {"amount": -4000000, "hour": 2}, {"amount": 10000, "hour": 18},{"amount": -15000000, "hour": 15}])