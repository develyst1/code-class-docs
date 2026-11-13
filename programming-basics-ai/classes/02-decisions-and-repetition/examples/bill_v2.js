// โปรแกรมคิดเงิน รุ่นที่ 2 แบบ JavaScript (จบคลาส 02)
// ใช้ยอดรวมที่กำหนดไว้ในโค้ด แทนการพิมพ์รับค่า

let total = 600;
let discount;
if (total >= 1000) {
  discount = total * 10 / 100;
} else if (total >= 500) {
  discount = total * 5 / 100;
} else {
  discount = 0;
}
let pay = total - discount;
console.log(`ยอดรวม ${total.toFixed(2)} บาท · ส่วนลด ${discount.toFixed(2)} บาท · ต้องจ่าย ${pay.toFixed(2)} บาท`);

// การทำซ้ำด้วย for: นับ 1 ถึง 3
for (let i = 1; i <= 3; i++) {
  console.log(`ลูกค้าคนที่ ${i}`);
}
