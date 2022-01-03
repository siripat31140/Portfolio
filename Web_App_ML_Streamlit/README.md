<h1 align="center">ผลลัพธ์การสร้าง Penguins Species Prediction App</h1>
<h3 >
    ในงานชิ้นนี้เป็นการประยุกต์การนำ Machine Learning มาสร้างเป็น Web App ในการทำนาย Penguins Species โดยสร้างเเบบ Online คือ การทำนายเป็นรายตัว Penguins เเละเเบบ Batch คือการอัปโหลดไฟล์ csv ที่เกือบตัวอย่าง Featue ของ Penguins มาหลายรายการ

<br>

## เเบบ Online
การทำนายเป็นรายตัว Penguins โดยจะกำหนดเเต่ละ Feature หลังจากนั้นกด  Predict จากนั้นผลลัพธ์การจะเเสดงผลตามตัวอย่าง

- Feature คือ **island=Dream, bill_length_mm=58.22, bill_depth_mm=20.8, flipper_length_mm=231, boby_mass=6300 ,sex= male**

- output คือ **Chinstrap**

<p align="center">
<img src="image\online.jpeg" width=100% alt="" srcset="">

<br>
<br>

## เเบบ Batch
การอัปโหลดไฟล์ penguins.csv ที่เก็บตัวอย่าง Featue ของ Penguins มาหลายรายการจากนั้นผลลัพธ์การจะเเสดงผลตามภาพตัวอย่าง

- label คือ Penguins Species ที่ถูก model ทำนาย 
- Score คือ ความน่าจะเป็นที่ model ทำนาย Penguins Species ที่คาดว่าจะถูกต้อง

<p align="center">
<img src="image\batch.jpeg" width=100% alt="" srcset="">