name=input('name of the student    ')
score=float(input('score of 20   '))
with open("exam_results.txt","w+",encoding="utf-8") as file:
    file.write(f"{name} {score}\n")
    file.readlines()
    print(file.read())
if score >=10:
    print('accepted')
else:
    print('need more training')