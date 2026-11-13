// คลาส 04 แบบ JavaScript: ข้อผิดพลาดสองแบบที่ JavaScript ต่างจาก Python

// กับดักที่ 1: แปลงข้อความที่ไม่ใช่ตัวเลข JavaScript ไม่ฟ้อง แต่ได้ NaN (Not a Number)
const price = Number("abc");
console.log(price);
if (Number.isNaN(price)) {
  console.log("กรุณาพิมพ์ตัวเลข");
}

// กับดักที่ 2: เรียกฟังก์ชันที่ไม่มีอยู่ (พิมพ์ชื่อผิด) แล้วจับข้อผิดพลาดด้วย try / catch
function calcDiscount(total) {
  if (total >= 500) {
    return total * 5 / 100;
  }
  return 0;
}

try {
  console.log(calcDiscont(600));
} catch (error) {
  console.log(`เกิดข้อผิดพลาด: ${error.message}`);
}

console.log(calcDiscount(600));
