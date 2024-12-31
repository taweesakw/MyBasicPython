money = 200
style = 'japanese'

def checkstyle(style,money):
    stylecheck = ['japanes','thai','chainese']
    if money >=200 and style in stylecheck:
        print ('คุณสามารถเข้าร้านได้จร้า')
    elif style not in stylecheck and money >=300:
        print (' คุณต้องซื้อชุดของร้านเราในราคา 100 บาท ถึงจะเข้าได้')
    else:
        print ('ขออภัยค่ะ ทางร้านไม่สามารถให้เข้าได้')

checkstyle ('thai',500)
คุณสามารถเข้าร้านได้จร้า
