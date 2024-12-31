tiles=2550
row=60 # 3 piecs per row
total_row=tiles//row
remaining_tiles=tiles%row

print(total_row,remaining_tiles)

buy_more=row-remaining_tiles

print(f'Total_tiles:{tiles} แผ่น')
print(f'1 แถวปูกระเบื้องได้ {row} แผ่น')
print ('------ คำนวณ---------')
print ('ต้องปูกระเบื้องทั้งหมด {} แถว'.format(total_row))
print ('เหลือกระเบื้องที่ยังไม่ได้ปูเต็มแถว {}แผ่น'.format(remaining_tiles))
print ('ลูกค้าต้องซื้อกระเบื้องเพิ่ม{} แผ่น'.format(buy_more))
         



#ลูกค้าต้องซื้อกระเบื้องกี่แผ่าน



