import numpy as np
def cal(l1,l2,l3,l4,l5,l6,l7):
    sum=l1+l2+l3+l4+l5+l6+l7
    mean=sum/7
    maxim=np.max([l1,l2,l3,l4,l5,l6,l7])
    minim=np.min([l1,l2,l3,l4,l5,l6,l7])
    
    for i in ([l1,l2,l3,l4,l5,l6,l7]):
        if i>mean:
            h+=1
    if mean>5000000:
        print('great week of foroosh\n')
    elif 2000000<mean>5000000:
        print('normal week of foroosh\n')
    else:
        print('weak week of foroosh\n')

    
    print(f'majmooe forooshe shoma {sum} ast\n')
    print(f'miangine forooshe shoma dar haft rooze gozashte {mean} ast\n')
    print(f'bishtarin forooshe shoma {maxim} boode ast\n')
    print(f'kamtarin forooshe shoma {minim} boode ast\n')
    print(f'tedad rooz hayi ke az miangin forooshetan bishtar boode ast {h} ast')
cal()
        