# โปรแกรมคิดเงิน รุ่นที่ 3 (จบคลาส 03)
# เหมือนรุ่นที่ 2 แต่แบ่งเป็นฟังก์ชัน และเก็บยอดที่ต้องจ่ายของทุกบิลไว้ใน history
# พิมพ์ราคา 0 แล้วจะสรุปทุกบิลก่อนปิด


def calc_discount(total):
    if total >= 1000:
        return total * 10 / 100
    elif total >= 500:
        return total * 5 / 100
    else:
        return 0


def my_sum(history):
    result = 0                      # เริ่มที่ 0
    for amount in history:
        result = result + amount    # บวกทีละบิล
    return result


def my_max(history):
    largest = 0                     # เงินไม่ติดลบ จึงเริ่มที่ 0 ได้
    for amount in history:
        if amount > largest:        # เจอบิลที่มากกว่า ก็จำบิลนี้แทน
            largest = amount
    return largest


def summary(history):
    print(f"จำนวนบิล {len(history)} · รวม {my_sum(history):.2f} บาท · บิลสูงสุด {my_max(history):.2f} บาท")
    parts = []
    for amount in sorted(history):
        parts.append(f"{amount:.2f}")
    print("เรียงจากน้อยไปมาก: " + ", ".join(parts))


history = []
while True:
    price = float(input("ราคาต่อชิ้น (บาท, 0 = ปิด): "))
    if price == 0:
        summary(history)
        print("ปิดโปรแกรม")
        break
    qty = int(input("จำนวนชิ้น: "))
    total = price * qty
    discount = calc_discount(total)
    pay = total - discount
    print(f"ยอดรวม {total:.2f} บาท · ส่วนลด {discount:.2f} บาท · ต้องจ่าย {pay:.2f} บาท")
    history.append(pay)
