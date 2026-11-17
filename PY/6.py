patients = [
    {"name": "Alice", "age": 30, "vitals": (120, 80), "history": ["Cold", "Flu"]},
    {"name": "Bob", "age": 55, "vitals": (145, 95), "history": ["Diabetes"]},
    {"name": "Charlie", "age": 40, "vitals": (110, 70), "history": []}
]
h=0
people=[]
for i in patients:
    if i['age']>38:
        if 'Diabetes' in i['history']:
            
            x=i['vitals']
            for k in x:
                h=h+k
            if h>190:
                people.append(i['name'])
print(f'highly in danger people are {people}')
