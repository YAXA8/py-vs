# imagine you have empty list again
# get 5 scores from student and caculate the average
ok=[]
for i in range(5):
    ok.append(float(input('give your score')))
    
x=0
for i in ok:
    x=i+x
l=len(ok)
z=x/l
print(z)
