def land(width,long,price=999888):
    cal = width * long
    cal_wa  = cal /4
    print('ที่ดินผืนนี้กว้าง : {}  เมตร ยาว: {} เมตร' .format (width,long))
    print('ที่ดินผืนนี้มีพื้นที่ : {}, ตารางเมตร'.format(cal))
    print ('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
    calprice = cal_wa * price
    return 'ที่ดินผืนนี้มีราคา: {:,.2f} บาท' .format(calprice)


def land (w,h):

    print (f'ที่ดินกว้าง: {w} เมตร ยาว {h}')
    
