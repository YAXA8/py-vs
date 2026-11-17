# Imagine, you have empty list
# you must write a program that take 5 values from user
# insert this value into list
# each value must power to 4 and multipy by 5
kj=[]
for i in range(5):
    kj.append((float(input('give a value'))))
for i in kj:
    print(i**4*5)

