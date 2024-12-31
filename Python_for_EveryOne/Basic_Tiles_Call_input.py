tilecolor={'Red':100,'Gold':150,'White':95,'Grey':90}

print (' ----- ราคากระเบื้อง -------')
for c,t in tilecolor.items():
    print('สี:{} ราคา: {}'.format(c,t))

print (' ----- โปรแกรมคำนวณกระเบื้อง Ver.2 By Ken -------')


try : 

    tiles= int(input('คุณต้องการปูกระเบื้องกี่แผ่น:'))
    row=int(input ('1 แถวต้องการปูกระเบื้องกี่แผ่น:')) # 3 piecs per row
    color = input('กระเบื้องสีอะไร? [Red / Gold/ White/ Grey]:')
    
except :
    print ('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!')
    tiles= int(input('คุณต้องการปูกระเบื้องกี่แผ่น:'))
    row=int(input ('1 แถวต้องการปูกระเบื้องกี่แผ่น:')) # 3 piecs per row
    color = input('กระเบื้องสีอะไร? [Red / Gold/ White/Grey]:')

    
    
print (' ----------- Calculate--------')

total_row=tiles//row
remaining_tiles=tiles%row

print(total_row,remaining_tiles)

buy_more=row-remaining_tiles

print(f'Total_tiles:{tiles} แผ่น')
print(f'1 แถวปูกระเบื้องได้ {row} แผ่น')
print ('------ คำนวณ---------')
print ('ต้องปูกระเบื้องทั้งหมด {} แถว'.format(total_row))
print ('เหลือกระเบื้องที่ยังไม่ได้ปูเต็มแถว {}แผ่น'.format(remaining_tiles))
print ('ลูกค้าต้องซื้อกระเบื้องเพิ่ม {} แผ่น'.format(buy_more))
print ('ยอดรวมทั้งหมดที่ต้องซื้อกระเบื้องเพิ่ม: {} บาท'.format(buy_more*tilecolor[color]))
         
print (' ----------- End--------')


#ลูกค้าต้องซื้อกระเบื้องกี่แผ่าน
