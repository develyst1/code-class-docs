# โปรแกรมคิดเงิน รุ่นที่ 2 (จบคลาส 02)
# ① ถามราคา (0 = ปิด)  ② ถามจำนวน  ③ ยอดรวม  ④ คิดส่วนลด  ⑤ แสดงผล  ⑥ กลับไป ①

while True:                                        # ⑥ ทำซ้ำไปเรื่อย ๆ
    price = float(input("ราคาต่อชิ้น (บาท, 0 = ปิด): "))      # ①
    if price == 0:
        print("ปิดโปรแกรม")
        break
    qty = int(input("จำนวนชิ้น: "))                  # ②
    total = price * qty                            # ③
    if total >= 1000:                              # ④
        discount = total * 10 / 100
    elif total >= 500:
        discount = total * 5 / 100
    else:
        discount = 0
    pay = total - discount
    print(f"ยอดรวม {total:.2f} บาท · ส่วนลด {discount:.2f} บาท · ต้องจ่าย {pay:.2f} บาท")  # ⑤
