inventory = {
    "Laptop": {"price": 1200, "stock": 5},
    "Mouse": {"price": 25, "stock": 0},
    "Monitor": {"price": 300, "stock": 3},
    'Pant':{'price':150,'stock':10},
    'Rtx5090':{'price':1200,'stock':50},
    'Rtx5080':{'price':800,'stock':40}
}
mosht=[]
mou=0
l=0
mo=0
p=0
rt8=0
rt9=0
sk=[]
bvuy=0
ls = ["Laptop, Mouse"]
while True:

    buy=input(f'what do you want from we have these right now{inventory}  type exit to exit     ')
    if buy=='exit':
        break
    elif buy not in ls:
        print("bullshit")
    else:
        count=int(input('how many     '))
        if buy.upper()=='LAPTOP':

            if inventory['Laptop']['stock']>count:
                inventory['Laptop']['stock']=inventory['Laptop']['stock']-count
                print('your purchase was successfull')
                mosht.append({buy:count})
                bvuy=bvuy+inventory['Laptop']['price']*count
            else:
                print('sorry we dont have enouph of that ')
        elif buy.upper()=='MONITOR':
            if inventory['Monitor']['stock']>count:
                inventory['Monitor']['stock']=inventory['Monitor']['stock']-count
                print('your purchase was successfull')
                mosht.append({buy:count})
                bvuy=bvuy+inventory['Monitor']['price']*count
            else:
                print('sorry we dont have enouph of that ')
        elif buy.upper()=='MOUSE':
            if inventory['Mouse']['stock']>count:
                inventory['Mouse']['stock']=inventory['Mouse']['stock']-count
                print('your purchase was successfull')
                mosht.append({buy:count})
                bvuy+=inventory['Mouse']['price']*count
            else:
                print('sorry we dont have enouph of that ')
        elif buy.upper()=='PANT':
            if inventory['Pant']['stock']>count:
                inventory['Pant']['stock']=inventory['Pant']['stock']-count
                print('your purchase was successfull')
                mosht.append({buy:count})
                bvuy+=inventory['Pant']['price']*count
            else:
                print('sorry we dont have enouph of that')
        elif buy.upper()=='RTX5080':
                if inventory['Rtx5080']['stock']>count:
                    inventory['Rtx5080']['stock']=inventory['Rtx5080']['stock']-count
                    print('your purchase was successfull')
                    mosht.append({buy:count})
                    bvuy+=inventory['Rtx5080']['price']*count
                else:
                    print('sorry we dont have enouph of that')
        elif buy.upper()=='RTX5090':
                if inventory['Rtx5090']['stock']>count:
                    inventory['Rtx5090']['stock']=inventory['Rtx5090']['stock']-count
                    print('your purchase was successfull')
                    mosht.append({buy:count})
                    bvuy+=inventory['Rtx5090']['price']*count
                else:
                    print('sorry we dont have enouph of that')
print(f'your total stuff are{mosht}')
print(f'and total price is {bvuy}')