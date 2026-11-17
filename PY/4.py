
# داده‌ها: (ID, (X, Y), Speed)
traffic_data = [
    (101, (12.5, 45.0), 85),
    (102, (13.0, 44.5), 110),
    (103, (12.8, 45.2), 40),
    (104, (14.2, 46.0), 130)
]
id=[]
for i in traffic_data:
    if i[2]>100:
        id.append(i[0])
print(id)
