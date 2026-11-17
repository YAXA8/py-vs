import numpy as np
def x(y):
    l=np.random.randint(1,y)
    m=0
    p=0
    h=y+1
    while l!=h:

            h=int(input('adad chie?'))
            if l>h:
                print('too low')
                m+=1
                if m%3==0:
                     if np.abs(l-h)>l/2:
                          print('you are far')
                     elif np.abs(l-h)<=l/2:
                          print('you are close')
            elif l<h:
                print('too high')
                m+=1
                if m%3==0:
                     if np.abs(l-h)>l/2:
                          print('you are far')
                     elif np.abs(l-h)<=l/2:
                          print('you are close')
            else:
                print('correct')
x(80)