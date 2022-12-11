# <br> Open Source Software TERM PROJECT <br>
#### Student ID : 건설시스템공학과 18100694 강형석<br>
#### License : GPL v3
### 1. Title<br>
**번화가 시뮬레이터<br>**
### 2. Team<br>
**Individual**<br>
### 3. What is this program for?<br>
**This program simulates the profits comming from the main street**<br>
**Now you are the owner of the main street !**<br> 
**All profits comming from the stores are yours !**<br>
**The Main steet's open hour is 5PM ~ next day 5AM**<br>
**Enjoy watching the profits you earned that day!**<br>
### 4. Demo Capture
![header](https://github.com/johnkang2/Hello/blob/main/oss%ED%85%80%ED%94%84/%EC%8B%A4%ED%96%89%EC%BA%A1%EC%B2%981.JPG?raw=true)
![header](https://github.com/johnkang2/Hello/blob/main/oss%ED%85%80%ED%94%84/%EC%8B%A4%ED%96%89%EC%BA%A1%EC%B2%982.JPG?raw=true)
### 5. How to use<br>
* **Press '시뮬레이터 시작' button to start simulator**<br>
* **Your record will be saved in 'record.csv'**<br>
* **'record.csv' will be created Automatically in same directory with '18100694_번화가_운영_시뮬레이터.py'**<br>
* **Given .csv file has record of 56 Days I have already runned**<br>
* **Place it to same directory with .py to resume or leave it to start NEW simulator**<br>
* **Press '일시정지' button to pause**<br>
* **Press '시뮬레이터 재개' button to resume** <br>
* **When the day ends, Today & Accrue profit will be shown and saved**<br>
* **Unless you pause, Next day will begin after 5 seconds**<br>
* **The price next to store's name means usage fee**<br>
### 6. For those who want to know more<br>
* 1 min of simulator time equals 1/3sec of actual time<br>
* Blue triangle indicates people who are now here, Purple indicates people who are already playing<br>
* And yellow indicates people who will go home.
* This program uses Python tkinter and turtle.
* If you keep running it , someday the program may stop because of 'OUT OF MEMORY'.<br>
* It's because I failed to find the way to remove turtle object.<br>
* So I used only .hideturtle() and memory usage is constantly increasing.<br>
* My PC RAM is 16G and it stopped at day87.<br>
* This is the human spawn chart<br>

| HOUR | MON | TUE | WED | THU | FRI | SAT | SUN |
| --- | --- | --- | --- | --- | --- | --- | --- |
|17-18|20|20|20|25|25|25|25|
|18-19|20|20|20|25|35|35|25|
|19-20|25|25|25|30|35|35|30|
|20-21|25|25|25|30|35|35|30|
|21-22|20|20|20|25|30|30|25|
|22-23|15|15|15|20|25|25|20|
|23-0|15|15|15|15|20|20|15|
|0-1|15|15|15|15|20|20|15|
|1-2|10|10|10|10|10|10|10|
|2-3|5|5|5|5|5|5|5|
|3-4|3|3|3|3|5|5|3|
|4-5|0|0|0|3|5|5|3|

# <br> Thank You Very Much!!<br><br>