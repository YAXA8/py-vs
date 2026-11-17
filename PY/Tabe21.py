def cargo(x):

    kamiyoon=0
    Kamiyoon=0
    Kamiyoonet=0
    kamiyoonet=0
    Vanet=0
    vanet=0
    outoflimit=0
    sensorerror=0
    for i in x:
        if 0<i<=2:
            vanet+=1
            Vanet+=i
        elif 2<i<=6:
            kamiyoonet+=1
            Kamiyoonet+=i
        elif 6<i<=10:
            Kamiyoon+=i
            kamiyoon+=1
        elif i>10:
            outoflimit+=1
        elif i<=0:
            sensorerror+=1
    vaziat=''
    if sensorerror>2:
        vaziat='System Failure'
    elif sensorerror<=2:
        vaziat='Operational'
    
    print(f'vazait= {vaziat}, tedade tarkhisiye vanet={vanet},vazne kole tarkhisi vanet={Vanet}, tedade tarkhisiye kamiyoonet={kamiyoonet}, vazne kole tarkhisiye kamiyoonet={Kamiyoonet},tedade tarkhisiye kamiyoon={kamiyoon},vazne kole tarkhisiye kamiyoon={Kamiyoon}')
cargo_weights = [1.2, 5.5, 9.0, 12.4, -0.5, 4.0, 0, 8.2]
cargo(cargo_weights)