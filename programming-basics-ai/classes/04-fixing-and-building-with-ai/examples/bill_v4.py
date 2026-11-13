# โปรแกรมคิดเงิน รุ่นที่ 4 (จบคลาส 04) — ฉบับเสร็จ
# เพิ่มจากรุ่นที่ 3: พิมพ์ผิดแล้วถามใหม่ และหารบิลกับเพื่อน (ฟีเจอร์ที่สร้างร่วมกับ AI)
# พิมพ์ราคา 0 แล้วจะสรุปทุกบิลก่อนปิด


def ask_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("กรุณาพิมพ์ตัวเลข")


def calc_discount(total):
    if total >= 1000:
        return total * 10 / 100
    elif total >= 500:
        return total * 5 / 100
    else:
        return 0


def split_bill(pay, people):
    return pay / people


def my_sum(history):
    result = 0
    for amount in history:
        result = result + amount
    return result


def my_max(history):
    largest = 0
    for amount in history:
        if amount > largest:
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
    price = ask_number("ราคาต่อชิ้น (บาท, 0 = ปิด): ")
    if price == 0:
        summary(history)
        print("ปิดโปรแกรม")
        break
    qty = ask_number("จำนวนชิ้น: ")
    total = price * qty
    discount = calc_discount(total)
    pay = total - discount
    print(f"ยอดรวม {total:.2f} บาท · ส่วนลด {discount:.2f} บาท · ต้องจ่าย {pay:.2f} บาท")
    history.append(pay)
    people = ask_number("หารกี่คน (1 = ไม่หาร): ")
    if people > 1:
        print(f"คนละ {split_bill(pay, people):.2f} บาท")
