ls = [1,2,1,3,4,5,6,4,"mehrshad", 7.4]
print(ls)
print(type(ls))

# Order
print(ls[1])
print(ls[3])
print(ls[2])
print(ls[-1])
print(ls[-6])
print(ls[1:5])
print(ls[5:1:-1])

# Contain duplicate
ls = [1,2,1,3,4,5,6,4,"mehrshad", 7.4, 2, 2, 2]

# changable - the most lovely feature in list character
ls[1] = "yashar"
ls[-1] = "benz"
ls.append("taghi")
ls.insert(3, "mamad")
ls2 = ls.copy()
ls.count(2)
ls.index("mehrshad")
ls.pop()
ls.pop(4)
ls.clear()
del ls
#
# for and while 
ls2 = [5,3,2,54,6]
for i in ls2:
    print(i, i * 2 , i ** 2)
for i in range(len(ls2)):
    res = ls2[i] * 9

# All the features mentioned above are the same for tuple except changeablity
# dictionary
# Keys and values
# Dic has changeabilty feature except orders
# dictinary uses {} as its sign
# Tuple uses (), list use []
# Keys must be unique
# values can be any type --- 
# keys can be any type too
# Keys and values together called --- pair
#For and while are able to walk inside
# Take care --- for and while walk in keys only. 
# If you want to walk in values. you have to give keys to dict to show their value
dic1 = {"name":"yashar", "age":19, "city":"bandar torkman"}
dic2 = {"cloth":[19, 2000], "hat":[20, 1000]}

for i in dic1:
    print(i, dic1[i])

# 
# Imagine, you have empty list
# you must write a program that take 5 values from user
# insert this value into list
# each value must power to 4 and multipy by 5

# imagine you have empty list again
# get 5 scores from student and caculate the average

# Take how many hours, wage, basic salary as input for 5 worker
# U must write this formula for each one to calculate final
# (hours - 20) * wage - basic
# Then you must insert final salary in a list for each one
# and provide the highest.


