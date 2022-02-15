<h1 align="center">ผลลัพธ์การวิเคราะห์ Classifying Dropout for Undergraduate Students</h2>

[ไฟล์ผลงานนำเสนอ](/รูปเล่ม.pdf)

## **วัตถุประสงค์ของการวิจัย**

- สร้างแบบจำลองการจำแนกประเภทสำหรับการพ้นสภาพของนักศึกษาระดับปริญญาตรี
สาขาวิชาสถิติ คณะวิทยาศาสตร์โดยใช้วิธีการเรียนรู้แบบเดี่ยวและแบบรวมกลุ่ม
- เปรียบเทียบประสิทธิภาพการจำแนกประเภทสำหรับการพ้นสภาพของนักศึกษาระดับ
ปริญญาตรี สาขาวิชาสถิติ คณะวิทยาศาสตร์ โดยใช้วิธีการเรียนรู้แบบเดี่ยวและแบบรวมกลุ่ม
- ศึกษาปัจจัยที่ส่งผลต่อการผลสภาพของนักศึกษาระดับ
ปริญญาตรี สาขาวิชาสถิติ คณะวิทยาศาสตร์

## **ผลกระบวนการจัดเตรียมข้อมูลและการสำรวจข้อมูลเบื้องต้น**
### **1. ผลลัพธ์จากการสำรวจข้อมูลเบื้องต้น**
<p align="center">
<img src="img\ประเภทการพ้นสภาพ.png" width=70% alt="" srcset="">

ประเภทการพ้นสภาพของนักศึกษาแบ่งออกเป็น พ้นสภาพเนื่องจากลาออก 
พ้นสภาพเนื่องจากไม่ชำระค่าต่อทะเบียนนักศึกษา พ้นสภาพเนื่องจากตกออก พ้นสภาพเนื่องจากไม่
ลงทะเบียนตามเวลากำหนด ลาพักการเรียน พบว่า นักศึกษาที่สำเร็จการศึกษามีสัดส่วนอยู่ที่ร้อยละ
38.44% นักศึกษาในปัจจุบันที่มีสถานะปกติมีสัดส่วนอยู่ที่ร้อยละ 38.44% พ้นสภาพเนื่องจากลาออกมี
สัดส่วนอยู่ที่ร้อยละ 11.07% พ้นสภาพเนื่องจากไม่ชำระค่าต่อทะเบียนนักศึกษามีสัดส่วนอยู่ที่ร้อยละ
5.37% พ้นสภาพเนื่องจากตกออกมีสัดส่วนอยู่ที่ร้อยละ 3.42% พ้นสภาพเนื่องจากไม่ลงทะเบียนตาม
เวลากำหนดมีสัดส่วนอยู่ที่ร้อยละ 2.93% ลาพักการเรียนมีสัดส่วนอยู่ที่ร้อยละ 0.33% จากจำนวน
ทั้งหมด 614 คน

### **2. ผลลัพธ์จากกระบวนการจัดเตรียมข้อมูล**
#### **2.1 ข้อมูลการพ้นสภาพกรณีที่ 1**
- สถานะการพ้นสภาพของนักศึกษาประกอบไปด้วย พ้นสภาพเนื่องจากลาออก พ้นสภาพเนื่องจาก
ไม่ชำระค่าต่อทะเบียนนักศึกษา พ้นสภาพเนื่องจากตกออก และพ้นสภาพเนื่องจากไม่ลงทะเบียนตาม
เวลากำหนด โดยมีข้อมูลพ.ศ. 2558 – 2563 มีจำนวน 586 รายการ 39 คุณลักษณะ และมีข้อมูลพ.ศ. 
2564 มีจำนวน 103 รายการ 38 คุณลักษณะ

#### **2.2 ข้อมูลการพ้นสภาพกรณีที่ 2**
- สถานะการพ้นสภาพของนักศึกษาประกอบไปด้วย พ้นสภาพเนื่องจากไม่ชำระค่าต่อทะเบียน
นักศึกษา และพ้นสภาพเนื่องจากไม่ลงทะเบียนตามเวลากำหนด โดยมีข้อมูลพ.ศ. 2558 – 2563 มีจำนวน
500 รายการ 27 คุณลักษณะ และมีข้อมูลพ.ศ. 2564 มีจำนวน 99 รายการ 26 คุณลักษณะ

#### **2.3 ข้อมูลการพ้นสภาพกรณีที่ 3**
- สถานะการพ้นสภาพของนักศึกษาประกอบไปด้วย พ้นสภาพเนื่องจากลาออก และพ้นสภาพ
เนื่องจากตกออก โดยมีข้อมูลพ.ศ. 2558 – 2563 มีจำนวน 555 รายการ 49 คุณลักษณะ และมีข้อมูล
พ.ศ. 2564 มีจำนวน 103 รายการ 48 คุณลักษณะ

## **เปรียบเทียบผลลัพธ์ของประสิทธิภาพความถูกต้องในการจำแนกประเภท**

### **ข้อมูลการพ้นสภาพกรณีที่ 1**
<p align="center">
<img src="img\การวัดประสิทธิภาพความถูกต้อง1.png" width=70% alt="" srcset="">

- การใช้การจำแนกประเภทแบบรวมกลุ่มที่ใช้DT เป็น
อัลกอริทึมพื้นฐานสำหรับการเรียนรู้ให้ประสิทธิภาพมากกว่าการใช้การจำแนกประเภทแบบเดี่ยวโดยใช้
อัลกอริทึม DT ในทางตรงกันข้ามการใช้การจำแนกประเภทแบบรวมกลุ่มที่ใช้SVM เป็นอัลกอริทึม
พื้นฐานสำหรับการเรียนรู้ให้ประสิทธิภาพไม่แตกต่างจากการใช้การจำแนกประเภทแบบเดี่ยวโดยใช้
อัลกอริทึม SVM อัลกอริทึมที่มีประสิทธิภาพในการจำแนกประเภทการพ้นสภาพดีที่สุด คือ Random
Forest และ Boosting Model (SVM Base Model) ซึ่งให้ค่าประสิทธิภาพไม่แตกต่างกันโดยมีค่าความ
ถูกต้อง (Accuracy) อยู่ที่ 99% ค่าความแม่นยำ (Precision) อยู่ที่ 99% ค่าความครบถ้วน (Recall) อยู่
ที่ 99% ค่าความถ่วงดุล (f1-score) อยู่ที่ 99% และค่า AUC พื้นที่ใต้เส้นโค้ง ROC อยู่ที่ 99% สำหรับ
การจำแนกประเภทการพ้นสภาพของนักศึกษา แสดงในตารางที่ 47

<p align="center">
<img src="img\ปัจจัยที่ส่งผลต่อการพ้นสภาพ1.png" width=70% alt="" srcset="">

- การพ้นสภาพกรณีที่ 1 โดยใช้
อัลกอริทึม Random Forest พบว่า ปัจจัยที่สำคัญต่อการพ้นสภาพของนักศึกษาประกอบด้วย เกรดเฉลี่ย
, เกรดเฉลี่ยระดับมัธยม, รายได้บิดา, รายได้มารดา, อายุมารดา, อายุบิดา, เกรด F รายวิชา STATISTICAL 
ANALYSIS I, ELEMENTARY PHYSICS, GENERAL CHEMISTRY LABORATORY, จ ำ น ว น พ ี ่ น ้ อ ง
ตามลำดับ แสดงในรูปที่ 19

### **ข้อมูลการพ้นสภาพกรณีที่ 2**
<p align="center">
<img src="img\การวัดประสิทธิภาพความถูกต้อง2.png" width=70% alt="" srcset="">

- การใช้การ
จำแนกประเภทแบบรวมกลุ่มที่ใช้DT และ SVM เป็นอัลกอริทึมพื้นฐานสำหรับการเรียนรู้ให้ประสิทธิภาพ
ไม่แตกต่างจากการใช้การจำแนกประเภทแบบเดี่ยวโดยใช้อัลกอริทึม DT และ SVM อัลกอริทึมที่มี
ประสิทธิภาพในการจำแนกประเภทการพ้นสภาพดีที่สุด คือ Random Forest ซึ่งให้ค่าประสิทธิภาพมีค่า
ความถูกต้อง (Accuracy) อยู่ที่ 99% ค่าความแม่นยำ (Precision) อยู่ที่ 99% ค่าความครบถ้วน (Recall)
อยู่ที่ 99% ค่าความถ่วงดุล (f1-score) อยู่ที่ 99% และค่า AUC พื้นที่ใต้เส้นโค้ง ROC อยู่ที่ 100%
สำหรับการจำแนกประเภทการพ้นสภาพของนักศึกษา แสดงในตารางที่ 48

<p align="center">
<img src="img\ปัจจัยที่ส่งผลต่อการพ้นสภาพ1.png" width=70% alt="" srcset="">

- งการพ้นสภาพกรณีที่ 2 โดยใช้
อัลกอริทึม Random Forest พบว่า ปัจจัยที่สำคัญต่อการพ้นสภาพของนักศึกษาประกอบด้วย เกรดเฉลี่ย
, เกรดเฉลี่ยระดับมัธยม, อายุบิดา, อายุมารดา,เกรด F รายวิชา ELEMENTARY PHYSICS, รายได้มารดา,
รายได้บิดา, เกรด F รายว ิช า INTRODUCTION TO INFORMATION AND COMMUNICATION 
TECHNOLOGY, GENERAL PHYSICAL LABORATORY, CALCULUS FOR PHYSICAL SCIENCE I,
จำนวนพี่น้อง ตามลำดับ แสดงในรูปที่ 20

### **ข้อมูลการพ้นสภาพกรณีที่ 3**
<p align="center">
<img src="img\การวัดประสิทธิภาพความถูกต้อง3.png" width=70% alt="" srcset="">

- การใช้การจำแนกประเภทแบบรวมกลุ่มที่ใช้DT และ 
SVM เป็นอัลกอริทึมพื้นฐานสำหรับการเรียนรู้ให้ประสิทธิภาพไม่แตกต่างจากการใช้การจำแนกประเภท
แบบเดี่ยวโดยใช้อัลกอริทึม DT และ SVM อัลกอริทึมที่มีประสิทธิภาพในการจำแนกประเภทการพ้น
สภาพดีที่สุด คือ Random Forest ซึ่งให้ประสิทธิภาพค่าความถูกต้อง (Accuracy) อยู่ที่ 99% ค่าความ
แม่นยำ (Precision) อยู่ที่ 99% ค่าความครบถ้วน (Recall) อยู่ที่ 99% ค่าความถ่วงดุล (f1-score) อยู่ที่ 
99% และค่า AUC พื้นที่ใต้เส้นโค้ง ROC อยู่ที่ 99% สำหรับการจำแนกประเภทการพ้นสภาพของ
นักศึกษา แสดงในตารางที่ 49

<p align="center">
<img src="img\ปัจจัยที่ส่งผลต่อการพ้นสภาพ3.png" width=70% alt="" srcset="">

- การพ้นสภาพกรณีที่ 3 โดยใช้
อัลกอริทึม Random Forest พบว่า ปัจจัยที่สำคัญต่อการพ้นสภาพของนักศึกษาประกอบด้วย เกรดเฉลี่ย
, เกรดเฉลี่ยระดับมัธยม, รายได้บิดา, รายได้มารดา, อายุบิดา, อายุมารดา, เกรด F รายวิชา STATISTICAL 
ANALYSIS I, ELEMENTARY PHYSICS, CALCULUS FOR PHYSICAL SCIENCE II, GENERAL 
CHEMISTRY LABORATORY ตามลำดับ แสดงในรูปที่ 21

## **ทำนายการพ้นสภาพของนักศึกษาปีการศึกษา 2564**
ผลลัพธ์จากการเลือกแบบจำลองที่ดีที่สุดโดยใช้อัลกอริทึม Random Forest สำหรับการเรียนรู้ 
ข้อมูลการพ้นสภาพของนักศึกษาปีการศึกษา 2564 โดยทำการแบ่งชุดข้อมูลออกเป็น 3 กลุ่มตัวอย่าง เพื่อ
ทำการจำแนกประเภทหรือทำนายการพ้นสภาพของนักศึกษาปีการศึกษา 2564 ดังนี้

### **ข้อมูลการพ้นสภาพกรณีที่ 1**

<p align="center">
<img src="img\การทำนายการพ้นสภาพนักศึกษา1.png" width=70% alt="" srcset="">

-ผลลัพธ์จากการใช้งานใช้อัลกอริทึม Random Forest สำหรับการเรียนรู้ข้อมูลการพ้นสภาพของ
นักศึกษาปีการศึกษา 2564 ของข้อมูลการพ้นสภาพกรณีที่ 1 มีจำนวน 103 คน โดยที่สถานะการพ้น
สภาพของนักศึกษาประกอบไปด้วย พ้นสภาพเนื่องจากลาออก พ้นสภาพเนื่องจากไม่ชำระค่าต่อทะเบียน
นักศึกษา พ้นสภาพเนื่องจากตกออก และพ้นสภาพเนื่องจากไม่ลงทะเบียนตามเวลากำหนด พบว่า 
นักศึกษาที่ถูกทำนายว่าไม่พ้นสภาพมีจำนวน 95 คนคิดเป็น 92.23% และนักศึกษาที่ถูกทำนายว่าพ้น
สภาพนักศึกษามีจำนวน 8 คนคิดเป็น 7.77% แสดงในรูปที่22


### **ข้อมูลการพ้นสภาพกรณีที่ 2**
<p align="center">
<img src="img\การทำนายการพ้นสภาพนักศึกษา2.png" width=70% alt="" srcset="">

- ผลลัพธ์จากการใช้งานใช้อัลกอริทึม Random Forest สำหรับการเรียนรู้ข้อมูลการพ้นสภาพของ
นักศึกษาปีการศึกษา 2564 ของข้อมูลการพ้นสภาพกรณีที่ 1 มีจำนวน 9 คน โดยที่สถานะการพ้นสภาพ
ของนักศึกษาประกอบไปด้วย พ้นสภาพเนื่องจากไม่ชำระค่าต่อทะเบียนนักศึกษา และพ้นสภาพเนื่องจาก
ไม่ลงทะเบียนตามเวลากำหนด พบว่า นักศึกษาที่ถูกทำนายว่าไม่พ้นสภาพมีจำนวน 97 คนคิดเป็น
97.98% และนักศึกษาที่ถูกทำนายว่าพ้นสภาพนักศึกษามีจำนวน 2 คนคิดเป็น 2.02% แสดงในรูปที่23


### **ข้อมูลการพ้นสภาพกรณีที่ 3**
<p align="center">
<img src="img\การทำนายการพ้นสภาพนักศึกษา3.png" width=70% alt="" srcset="">

- ผลลัพธ์จากการใช้งานใช้อัลกอริทึม Random Forest สำหรับการเรียนรู้ข้อมูลการพ้นสภาพของ
นักศึกษาปีการศึกษา 2564 ของข้อมูลการพ้นสภาพกรณีที่ 1 มีจำนวน 103 คน โดยที่สถานะการพ้น
สภาพของนักศึกษาประกอบไปด้วย พ้นสภาพเนื่องจากลาออก และพ้นสภาพเนื่องจากตกออก พบว่า 
นักศึกษาที่ถูกทำนายว่าไม่พ้นสภาพมีจำนวน 95 คนคิดเป็น 92.23% และนักศึกษาที่ถูกทำนายว่าพ้น
สภาพนักศึกษามีจำนวน 8 คนคิดเป็น 7.77% แสดงในรูปที่24
