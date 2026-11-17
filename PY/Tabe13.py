def mk(city,price):
    if float(price)>500000:
        print('hazine ersal = raygan')
    elif city.lower()=='tehran':
        print('hazine ersal = 30000')
    elif city.lower()=='karaj':
        print('hazine ersal = 40000')
    else:
        print('hazine ersal = 60000')
mk('tehran',400000000)