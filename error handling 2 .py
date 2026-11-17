daily_calories=[1850,2100,1950,'undefined']
total=0
for day_num,cal in enumerate(daily_calories,start=1):
    try:
        total +=cal
    except TypeError as error_msg:
        print(f'{day_num}th day is invalid ')
        print(f'system error is: {error_msg}')
        print('this day got prevented')
print(f'sum of valid days calories:{total}')