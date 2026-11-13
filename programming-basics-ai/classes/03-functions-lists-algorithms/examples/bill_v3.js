// โปรแกรมคิดเงิน รุ่นที่ 3 แบบ JavaScript (จบคลาส 03)
// ใช้ยอดที่ต้องจ่ายของ 3 บิลที่กำหนดไว้ในโค้ด

const history = [570, 900, 120];

// ผลรวม: เริ่มที่ 0 แล้วบวกทีละบิล
let sum = 0;
for (const amount of history) {
  sum = sum + amount;
}

// ค่ามากสุด: จำบิลที่มากที่สุดที่เจอมา
let largest = 0;
for (const amount of history) {
  if (amount > largest) {
    largest = amount;
  }
}

console.log(`จำนวนบิล ${history.length} · รวม ${sum.toFixed(2)} บาท · บิลสูงสุด ${largest.toFixed(2)} บาท`);

// เรียงลำดับตัวเลข ต้องบอกวิธีเทียบ (a, b) => a - b
const sorted = history.slice().sort((a, b) => a - b);
console.log(`เรียงจากน้อยไปมาก: ${sorted.join(", ")}`);

// กับดัก: ถ้าไม่บอกวิธีเทียบ JavaScript จะเรียงตัวเลขแบบข้อความ
console.log([100, 20, 3].sort());
