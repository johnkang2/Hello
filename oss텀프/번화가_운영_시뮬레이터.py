#건설시스템공학과 18100694 강형석

import tkinter as tk  #from tkinter import * 은 왜 안되지?
import turtle, time, random
from os import path

days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
spawntable = [[20,20,25,25,20,15,15,15,10,5,3,0],[20,20,25,25,20,15,15,15,10,5,3,0],[20,20,25,25,20,15,15,15,10,5,3,0],
           [25,25,30,30,25,20,15,15,10,5,3,3],[25,35,35,35,30,25,20,20,10,5,5,5], [25,35,35,35,30,25,20,20,10,5,5,5],[25,25,30,30,25,20,15,15,10,5,3,3]]
staytimes=[[1,4],[1,4],[1,4],[1,6],[1,10],[1,10],[1,6]]
hour2check=[17,18,19,20,21,22,23,0,1,2,3,4]
currentdayspawntable=[]
streets=[]
stores=[]
humans=[]
createdhuman=0   #디버깅시 numdisplay 에 쓰이는것
livehuman=0

class Simulator :
    def __init__(self, root) :
        self.root = root
        self.root.title('번화가 운영 시뮬레이터  [ 제출자 : 건설시스템공학과 18100694 강형석 ]')
        self.root.minsize(1320,920)
        self.root.resizable(False, False)   #창크기 x, y 변경 불가
        self.canvas = turtle.Canvas(master=self.root, width=1302, height=802)  #딱 1300x800으로 하면 선이 잘린다
        self.canvas.place(x = 7, y = 100)    #gui의 좌표계와 터틀에서 좌표계는 다르다
        self.t = turtle.RawTurtle(self.canvas)     #맵 그리는 터틀
        self.t.speed('fastest')
        self.dayindex = 0
        self.day = 1
        self.hour=17
        self.min=0
        self.sec=5
        self.hour2checkindex=0
        self.earn=0
        self.earntotal=0
        self.pastrecord=[]
        self.counting =False
        self.min12checked =False
        self.min24checked=False
        self.min36checked=False
        self.min48checked=False
        self.start=False
        self.hiding=False
        self.goodtocount=True
        self.read()  #.csv읽어오기
        self.drawMap()
        self.drawGUI()
        self.streetInitialize()
        self.storeInitialize()
        self.drawStore()  #drawstore까지 끝난후 bt1활성화
    
    def drawMap(self) :
        self.t.color('black')
        self.t.hideturtle()
        self.t.speed('fastest')
        self.t.penup()
        #배경   Canvas는 배경색을 어떻게 설정하지?
        self.t.setpos(-650,400)
        self.t.pendown()
        self.t.fillcolor('beige')
        self.t.begin_fill()
        self.t.setpos(650,400)
        self.t.setpos(650,-400)
        self.t.setpos(-650,-400)
        self.t.setpos(-650,400)
        self.t.end_fill()
        self.t.penup()
        #블록1
        self.t.setpos(-650, 400)
        self.t.pendown()
        self.t.fillcolor('dimgray')
        self.t.begin_fill()
        self.t.setpos(-270, 400)
        self.t.setpos(-270, 180)
        self.t.setpos(-650, 180)
        self.t.setpos(-650, 400)
        self.t.end_fill()
        self.t.penup()
        #블록2
        self.t.setpos(-210, 400)
        self.t.pendown()
        self.t.fillcolor('dimgray')
        self.t.begin_fill()
        self.t.setpos(-30, 400)
        self.t.setpos(-30, 180)
        self.t.setpos(-210, 180)
        self.t.setpos(-210, 400)
        self.t.end_fill()
        self.t.penup()
        #블록3
        self.t.setpos(30, 400)
        self.t.pendown()
        self.t.fillcolor('dimgray')
        self.t.begin_fill()
        self.t.setpos(210, 400)
        self.t.setpos(210, 180)
        self.t.setpos(30, 180)
        self.t.setpos(30, 400)
        self.t.end_fill()
        self.t.penup()
        #블록4
        self.t.setpos(270, 400)
        self.t.pendown()
        self.t.fillcolor('dimgray')
        self.t.begin_fill()
        self.t.setpos(650, 400)
        self.t.setpos(650, 180)
        self.t.setpos(270, 180)
        self.t.setpos(270, 400)
        self.t.end_fill()
        self.t.penup()
        #블록5
        self.t.setpos(-650, 120)
        self.t.pendown()
        self.t.fillcolor('dimgray')
        self.t.begin_fill()
        self.t.setpos(-270, 120)
        self.t.setpos(-270, -120)
        self.t.setpos(-650, -120)
        self.t.setpos(-650, 120)
        self.t.end_fill()
        self.t.penup()
        #블록6
        self.t.setpos(-210, 120)
        self.t.pendown()
        self.t.fillcolor('dimgray')
        self.t.begin_fill()
        self.t.setpos(210, 120)
        self.t.setpos(260, -30)
        self.t.setpos(-210, -120)
        self.t.setpos(-210, 120)
        self.t.end_fill()
        self.t.penup()
        #블록6 내부
        self.t.setpos(-60,50)
        self.t.pendown()
        self.t.fillcolor('darkolivegreen')
        self.t.begin_fill()
        self.t.setpos(70,50)
        self.t.setpos(85,5)
        self.t.setpos(-60,-20)
        self.t.setpos(-60,50)
        self.t.end_fill()
        self.t.penup()
        #블록7
        self.t.setpos(270, 120)
        self.t.pendown()
        self.t.fillcolor('dimgray')
        self.t.begin_fill()
        self.t.setpos(650, 120)
        self.t.setpos(650, -30)
        self.t.setpos(320, -30)
        self.t.setpos(270, 120)
        self.t.end_fill()
        self.t.penup()
        #블록8
        self.t.setpos(-650, -180)
        self.t.pendown()
        self.t.fillcolor('dimgray')
        self.t.begin_fill()
        self.t.setpos(-270, -180)
        self.t.setpos(-270, -400)
        self.t.setpos(-650, -400)
        self.t.setpos(-650, -180)
        self.t.end_fill()
        self.t.penup()
        #블록9
        self.t.setpos(-210, -180)
        self.t.pendown()
        self.t.fillcolor('dimgray')
        self.t.begin_fill()
        self.t.setpos(260, -90)
        self.t.setpos(260, -400)
        self.t.setpos(-210, -400)
        self.t.setpos(-210, -180)
        self.t.end_fill()
        self.t.penup()
        #블록10
        self.t.setpos(320, -90)
        self.t.pendown()
        self.t.fillcolor('dimgray')
        self.t.begin_fill()
        self.t.setpos(650, -90)
        self.t.setpos(650, -400)
        self.t.setpos(320, -400)
        self.t.setpos(320, -90)
        self.t.end_fill()
        self.t.penup()
    
    def drawGUI(self) :
        #버튼들
        self.bt1text = tk.StringVar()
        self.bt1text.set("시뮬레이터 시작")
        self.bt1 = tk.Button(self.root, textvariable=self.bt1text, command=lambda :[self.timeProceed(), self.checkHour()])  #람다식에는 함수명뒤에 () 붙여야함
        self.bt1.place(x=10,y=10)
        self.bt1["state"]=tk.DISABLED
        self.bt2 = tk.Button(self.root, text="일시정지", command=self.timePause)
        self.bt2.place(x=120, y=10)
        self.bt2["state"]=tk.DISABLED
        self.bt3 = tk.Button(self.root, text="INFO", command=self.showInfo)
        self.bt3.place(x=190, y=10)
        #표시창
        self.lb1 = tk.Label(self.root, text=f"Day {self.day}", font=("Consolas",15))
        self.lb1.place(x=1150, y=10)
        self.lb2 = tk.Label(self.root, text="00 : 00 : 00", font=("Consolas",15))
        self.lb2.place(x=1150, y=40)
        self.lb3 = tk.Label(root, text=f"누적 수익 : {self.earntotal:,} 원", font=("Consolas",15))   
        self.lb3.place(x=300, y=40)
        self.lb4 = tk.Label(self.root, text="",font=("Consolas",15))    #수익표시용
        self.lb4.place(x=300, y=10)
        self.lb5 = tk.Label(self.root, text="")   #5초세는용
        self.lb5.place(x=10, y=40)
        self.lb6=tk.Label(self.root, text = " 시           분           초", font=("",8))
        self.lb6.place(x=1152,y=65)
        self.lb7 = tk.Label(self.root,text="",font=("Consolas",15))   #평가용
        self.lb7.place(x=580,y=10)
        self.lb8 = tk.Label(self.root,text="")   #인원표시용
        self.lb8.place(x=10,y=80)
        self.lb9 = tk.Label(self.root, text="     라이선스 : GPL v3     ", font=("",11))
        self.lb9.config(fg='red',bg='yellow')
        self.lb9.place(x=1130,y=82)
    
    def streetInitialize(self) :
        global streets
        
        st1 = self.Street(-270,-210,180,400)
        st2=self.Street(-30,30,180,400)
        st3=self.Street(210,270,180,400)
        st4=self.Street(-650,650,120,180)
        st5=self.Street(-270,-210,-400,120)
        st6=self.Street(-650,-270,-180,-120)
        st7=self.Street(-210,260,-180,-30)
        st8=self.Street(210,320,-30,120)
        st9=self.Street(260,330,-400,-30)
        st10=self.Street(320,650,-90,-30)
        streets.extend([st1,st2,st3,st4,st5,st6,st7,st8,st9,st10])
    
    class Street :
        def __init__(self, x1,x2,y3,y2) :   #y3,y2로 한 이유는 random.randint 때문
            self.x1=x1
            self.y2=y2
            self.x2=x2
            self.y3=y3
            self.pay=0
            self.outx=(x1+x2)/2
            self.outy=(y2+y3)/2
            
    def storeInitialize(self) :
        global stores
        
        s1 = self.Store("짱분식나라",-640,390,-400,390,-400,190,-640,190,-450,160,10000)
        s2 = self.Store("맛나야채곱창",-390,390,-280,390,-280,190,-390,190,-320,160,11200)
        s3 = self.Store("베이커리",-200,390,-40,390,-40,260,-200,260,-240,330,8000)
        s4 = self.Store("도깨비포차",-200,250,-40,250,-40,190,-200,190,-240,210,7300)
        s5 = self.Store("인계동껍데기",40,390,200,390,200,190,40,190,0,290,9000)
        s6 = self.Store("불타는돼지",280,390,450,390,450,240,280,240,240,310,14000)
        s7 = self.Store("밀크뮤직타운",460,390,640,390,640,190,460,190,500,160,13300)
        s8=self.Store("카페베네",-640,110,-400,110,-400,-110,-640,-110,-550,140,7500)
        s9=self.Store("이탈리아미슐랭",-390,70,-280,70,-280,-110,-390,-110,-350,140,22000)
        s10=self.Store("포장마차",-200,110,-180,110,-180,50,-200,50,-230,80,5500)
        s11=self.Store("불막창",330,110,460,110,460,-20,330,-20,390,-50,18900)
        s12=self.Store("아지트포차",470,110,640,110,640,-20,470,-20,600,140,13500)
        s13=self.Store("아이디헤어",-640,-190,-380,-190,-380,-390,-640,-390,-510,-150,25400)
        s14=self.Store("노래방",-370,-250,-280,-250,-280,-390,-370,-390,-240,-320,8400)
        s15=self.Store("와인바",-200,-190,-60,-190,-60,-390,-200,-390,-110,-140,19800)
        s16=self.Store("보스나이트",-50,-190,250,-190,250,-390,-50,-390,150,-80,50000)
        s17=self.Store("선화꽃집",330,-130,420,-130,420,-250,330,-250,290,-190,8300)
        s18=self.Store("게임랜드",430,-100,640,-100,640,-390,430,-390,290,-280,23500)
      
        stores.extend([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18])   #여러개를 한번에 리스트에 추가할때 
        
    class Store :
        def __init__(self,name, x1,y1,x2,y2,x3,y3,x4,y4,outx,outy,pay) :
            self.name=name
            self.x1=x1
            self.y1=y1
            self.x2=x2
            self.y2=y2
            self.x3=x3
            self.y3=y3
            self.x4=x4
            self.y4=y4
            self.outx=outx
            self.outy=outy
            self.pay=pay
        
    def drawStore(self) :  
        global stores
        
        for s in stores:
            self.t.color('lightgray')
            self.t.setpos(s.x1,s.y1)
            self.t.pendown()
            self.t.fillcolor('lightgray')
            self.t.begin_fill()
            self.t.setpos(s.x2,s.y2)
            self.t.setpos(s.x3,s.y3)
            self.t.setpos(s.x4,s.y4)
            self.t.setpos(s.x1,s.y1)
            self.t.end_fill()
            self.t.penup()
            self.t.color('black')
            self.t.setpos(s.x1+5,s.y1-15)
            self.t.write(f'{s.name} {s.pay}원')
            
        s19=self.Store("공원",-170,120,210,120,210,-30,-170,-30,20,0,0)
        stores.append(s19)  #공원은 경계선을 안그린다.
        self.t.color('white')
        self.t.setpos(s19.x1+165,s19.y1-25)
        self.t.write(f'{s19.name}')
        self.bt1['state']=tk.NORMAL
        
    def spawn(self,time) :
        global streets,humans,createdhuman,livehuman
        
        createdhuman+=1
        livehuman+=1
        h = self.Human(self.canvas,time,createdhuman)
        
        h.color('blue')
        h.shape('arrow')
        h.speed('fastest') 
        h.penup()
        spawnpos = random.randint(0,9)
        #블록별로 스폰 위치가 다르다.
        h.setpos(random.randint(streets[spawnpos].x1, streets[spawnpos].x2), random.randint(streets[spawnpos].y3, streets[spawnpos].y2))
            
        #print(f'staytime = {h.staytime}')
        humans.append(h)
        
    
    def spawnManager(self):   #dayindex 가 아닌 day를 기준으로 한다. 
        #처음에는 spawnManager를 timeProceed에 연결시키려했으나, Human객체 생성속도가 after를 못따라가서 시뮬레이터 시계속도가 왔다갔다한다. 이는 설정된 타이밍을 맞추기위함으로 보인다.
        global spawntable, currentdayspawntable, staytimes
        
        currentdayspawntable = spawntable[(self.day -1) %7]    #사실 day바뀔때마다만 하면 된다.
            
        if self.hour>= 17 and self.hour<=23 : 
            currenthourspawn = currentdayspawntable[self.hour-17]   
        elif self.hour>=0 and self.hour<=4 :
            currenthourspawn = currentdayspawntable[self.hour+7]
        else:  #hour 가 5일때 spawnmanager가 호출이 되는지 안되는지 확실하지않다, 혹시모르니 경우를 만들어두자
            currenthourspawn=0
            
        print(f'(시뮬레이터 요일과 혼동하지 말자)\n요일 = {days[(self.day-1)%7]} 시간 = {self.hour} 스폰수 = {currenthourspawn}')   
        
        for i in range(currenthourspawn) :
            self.spawn(random.randint(staytimes[(self.day-1)%7][0], staytimes[(self.day-1)%7][1]))
        
    class Human(turtle.RawTurtle) :
        def __init__(self,canvas,time,createdhuman) :
            super().__init__(canvas)
            self.staytime=time  #맵에 머무르는 시간
            self.togolist=[]
            self.togoindex=0
            self.num = createdhuman
            self.paydisplay=tk.Label(canvas, text="")
            self.paydisplay.place(x=200,y=-25)  #아직은 화면에안보이게, 라벨이 위치한곳이 캔버스(turtle) 이어도 라벨은 tkinter 여서 tk좌표를 따라가나보다
            #self.numdisplay=tk.Label(canvas,text="")
            #self.numdisplay.place(x=-100,y=-100)
            self.saydisplay=tk.Label(canvas,text="")
            self.saydisplay.place(x=200,y=-25)
            ###self.saydisplay.config(bg='black')
            self.life = 1
            self.new=True
            self.scheduler()
            
        def scheduler(self) :
            global streets,stores
            #tmparr = streets 이렇게하면 안된다. 내용복사가아닌 뭔가 포인터처럼 작동하는것 같다.
            tmparr=[]
            tmparr.extend(streets)
            tmparr.extend(stores)
            random.shuffle(tmparr)
            for i in range(self.staytime) :
                self.togolist.append(tmparr[i])
        
    def timeProceed(self) :   #초는 쭉 0이다, day랑 dayindex 구분 잘하자
        global days,humans,livehuman
        
        self.goodtocount=True
        self.start=True
        self.lb8.config(text=f'현재인원 {livehuman} 명')
        self.lb7.config(text="")
        self.lb5.config(text="시뮬레이션 중...")
        self.bt1text.set("시뮬레이터 재개")
        self.bt1["state"]=tk.DISABLED   #!!!!!오류방지를 위해 버튼이 클릭되면 비활성화되게 하자!!!!!
        self.bt2["state"]=tk.NORMAL
        self.lb4.config(text=f"오늘 수익 : {self.earn:,} 원")
        self.lb3.config(text=f"누적 수익 : {self.earntotal:,} 원")
        self.lb1.config(text=f"Day {self.day:3d}  {days[self.dayindex % 7]}")
        self.min +=1
        if self.min==60 :
            self.min=0
            self.hour +=1
            self.min12checked=False
            self.min24checked=False
            self.min36checked=False
            self.min48checked=False
            if self.hour==24 :
                self.dayindex +=1
                self.lb1.config(text=f"Day {self.day:3d}  {days[self.dayindex % 7]}")
                self.hour=0
                self.min=0
            #####elif self.hour == 5 : #####
                #######self.timePause() 이렇게 하면 정지가 안된다. 왜지?
                #### self.root.after_cancel(self.taskid1) 이것도 안된다 
                # 이유를 알았다. 왜 안되나면 after_cancel 은 return 의 개념이 아니다. 여기서 cancel 해도 아래로 내려가서 다시 after를 만나버린다.
                # after_cancel은 맨 아래에 놓자. 이게 해당함수가 완료되기전까지는 after를 만나도 다시실행을 보류해놓는가보다
        
        self.lb2.config(text=f"{self.hour:02d} : {self.min:02d} : 00")
        #gui를 쓰는 프로그램에선 time.sleep을 쓰면 안된다. 5초간 정지시킬 다른 방법을 찾아보자. 터틀에 ontimer 가 있다면 tkinter 에는 after가 있다. 
        self.taskid1 = self.root.after(333,self.timeProceed)  #실험시에도 너무 빠르게하면 checkHour가 건너뛰는시간이 있을수 있다
        
        if self.hour==5 :
            self.root.after_cancel(self.task_a)  #4시48분이후 재개됬을때를 위하여
            self.hour2checkindex=0
            self.hour = 17 
            self.min=0
            self.root.after_cancel(self.taskid1)  #timePause 를 안쓰는 이유는 timePause를 하면 bt1 이 활성화되기 때문이다.
            self.pastrecord.append([self.day,self.earn])
            if self.day>=8:
                past=self.pastrecord[self.day-8][1]   #7이아니라 8을빼는 이유는 인덱스이기때문
                if self.earn>= past:
                    self.lb7.config(text=f"<금일 전주 대비 + {self.earn-past:,} 원 증가 !!>")
                else :
                    self.lb7.config(text=f"<금일 전주 대비 {past-self.earn:,} 원 감소>")
            else :
                self.lb7.config(text="day8 이상일때 평가를 시작합니다...")
            
            self.write()
            self.earn=0    
            self.day+=1
            self.lb5.config(text="번화가 영업종료. 미귀가자 귀가처리중...")
            self.hiding=True
            for i in humans :   #여기다가 위치시키는 이유는 이 과정은 좀 시간이 걸리기때문에 after_cancel 다음에두자
                #i.numdisplay.place(x=-100,y=-100)
                i.hideturtle()
            humans=[]     #이렇게 해도 메모리 어딘가에 turtle 객체가 남아있나보다. 윈도우 작업관리자에서 메모리가 계속 증가한다. 한번에 day100정도까지가 최대인듯하다. 그다음은 엑셀에 저장하고 더   
            livehuman=0   #del humans 등등 해도 마찬가지.터틀, 스크린을 동시에 지워버리는 명령어는 있어도 터틀만 지우는건 없는것같다, 메모리해제 명령어 없나?
            self.lb8.config(text=f'현재인원 {livehuman} 명')
            self.hiding=False
            if self.goodtocount==True:
                self.currentsec = time.time()
                self.count5()  #함수이름도 counting으로 하면 아나콘다ide가 bool변수 counting이랑 헷갈려한다.
            
    def checkHour(self):   #timeProceed 보다 먼저 끝나야한다.
        global hour2check,humans,livehuman
        
        #아무리 이렇게 경고메세지가 안뜨게 안전장치를 많이 달아도 미세한 시간 사이에 가끔 after가 해당 task id가 없다는 경고가 뜬다. 프로그램 작동에는 문제가없다.
        #명령어로 반복, 종료하는게 아니라, 해당 태스크의 id를 찾아서 종료하고 새로운 반복태스크를 만들고 이런방식이라 그런가?
        #tkinter의 여러 위젯에는 사용자 작업에대해 알려주는 콜백이 없어서 사용자가 직접 실시간으로 추적해야한다고 한다.
        #아니면 tkinter가 single thread 에서 작동해서 그런가?
        #반복시간을 10ms에서 7ms로 줄여보면 그 미세한 시간차이도 극한으로 사라지지않을까
        #프로그램을 시작하고 시뮬레이터시작버튼을 안눌러도 경고가뜨는걸 보면 파이썬이 프로그램실행전에 미리 함수들을 한번씩 실행시켜보나?
        self.task_a=self.root.after(7,self.checkHour)  #이렇게하면 spawnManager실행 이전에 task_a가 실행된다. after는 return이 아닌 실행예약 개념이 맞는거같다. 근데 함수가 완벽히 종료후 재실행되는게 아닌것같다?
        
        if self.hour == hour2check[self.hour2checkindex] :  #hour 체크
            self.hour2checkindex+=1   
            if self.hour2checkindex == 12 :  #여기서 바로 ==12 해버리면 out of index 에러가 안뜬다(떠도 잘 돌아가긴함). 아무래도 after는 해당함수가 완전히 종료후 재실행되는게 아닌거같다.
                self.hour2checkindex =1  #왜 바로 0으로 안만드냐하면 만약 4시48분 이후에 일시정지 후 재개를 하면 checkHour 가 다시 작동하고 5시가 되는순간 spawnManager가 작동하기 때문이다. 만에하나 timeProceed에 종료식보다 빠를수도 있다.
            self.spawnManager()
            #self.displayStatus()     
            for h in humans :
                if h.life==1:
                    if h.new==True:
                        h.saydisplay.place(x=h.xcor()+653,y=-(h.ycor())+413)
                        h.saydisplay.config(text="안녕하세요 ~")
                        h.new=False
# =============================================================================
#             for h in humans :     #디버깅용
#                 if h.life==1 :
#                     h.numdisplay.place(x=h.xcor()+653,y=-(h.ycor())+413)####
#                     h.numdisplay.config(text=f'번호 {h.num}번')####
# =============================================================================            
        elif self.min == 12 :
            if self.min12checked==False : 
                self.min12checked=True
                for h in humans :
                    if h.life==1:
                        #print(h.togolist[h.togoindex].x1)   #random.randint(,) 에는 작은수가 앞에와야한다. 큰수먼저오면 에러
                        h.color('hotpink4')
                        h.setpos(random.randint(h.togolist[h.togoindex].x1,h.togolist[h.togoindex].x2), random.randint(h.togolist[h.togoindex].y3,h.togolist[h.togoindex].y2))
                        h.togoindex+=1
                        h.saydisplay.config(text="")   #멀리 보내는게아니라 이렇게 내용을 지우고 탭에 숨기자. 메모리점유가 많이 올라가면 윈도우상에 라벨이 떠다닌다.
                        h.saydisplay.place(x=200,y=-25)
# =============================================================================
#                         h.numdisplay.place(x=h.xcor()+653,y=-(h.ycor())+413)####
#                         h.numdisplay.config(text=f'번호 {h.num}번')####
# =============================================================================
        elif self.min == 24 :
            if self.min24checked==False:
                self.min24checked=True
                for h in humans :
                    if h.life==1:
                        bill=h.togolist[h.togoindex-1].pay
                        self.earn+=bill
                        self.earntotal+=bill
                        h.paydisplay.place(x=h.xcor()+653,y=-(h.ycor())+370)   #tk와 터틀의 좌표는 다르다
                        h.paydisplay.config(text=f'+ {bill} 원')      
        elif self.min==36:
            if self.min36checked==False:
                self.min36checked=True
                for h in humans:
                    if h.life==1:
                        place = h.togolist[h.togoindex-1]
                        h.paydisplay.config(text="")
                        h.paydisplay.place(x=200,y=-25) #다시 저멀리
                        if h.togoindex == h.staytime :
                            h.setpos(place.outx,place.outy)
                            h.saydisplay.place(x=h.xcor()+653,y=-(h.ycor())+413)
                            h.saydisplay.config(text="집에가자 ~")
                            h.color('orange')
# =============================================================================
#                         h.numdisplay.place(x=h.xcor()+653,y=-(h.ycor())+413)####
#                         h.numdisplay.config(text=f'번호 {h.num}번')#####
# =============================================================================
        elif self.min==48:
            if self.min48checked==False:
                self.min48checked=True
                for h in humans :
                    if h.life==1:
                        if h.togoindex==h.staytime :
                            #h.numdisplay.place(x=-100,y=-100)######
                            h.saydisplay.config(text="")
                            h.saydisplay.place(x=200,y=-25)
                            h.hideturtle()
                            h.life=0
                            livehuman-=1
                #self.displayStatus()
                if self.hour==4 :
                    self.root.after_cancel(self.task_a)
                         
    def timePause(self) :  #일시정지하고 해당min 또는 hour의 터틀이동이 다 안끝났는데 다시 resume해도 괜찮다.
        self.bt1["state"]=tk.NORMAL
        self.bt2["state"]=tk.DISABLED
        
        if self.counting==False and self.hiding==False:
            self.root.after_cancel(self.taskid1)  #after를 종료하는 방법이다. 
            self.root.after_cancel(self.task_a)
        elif self.hiding==True:
            self.goodtocount=False
            self.lb5.config(text="")
        else :  #이때는 counting = true
            self.sec=5
            self.counting=False
            self.lb5.config(text="")
            self.root.after_cancel(self.taskid4)
  
    def count5(self) :  
        self.counting=True
        self.lb5.config(text=f"{self.sec}초 뒤에 Day{self.day} 으로 넘어갑니다... ")
        self.sec-=1
        self.taskid4=self.root.after(1000,self.count5)
        if abs(time.time() - self.currentsec - 5) < 0.3 :
            self.counting=False
            self.sec=5
            self.lb5.config(text="")
            self.root.after_cancel(self.taskid4)
            self.timeProceed()
            self.checkHour()
           
# =============================================================================
#     def displayStatus(self) :   #디버깅용
#         print('-'*10)
#         for h in humans :
#             print(f'번호 = {h.num} life={h.life} ')
#         print('-'*10)
# =============================================================================

    def showInfo(self) :   #Message 가 아닌 messagebox를 쓰는 이유는 turtle이 움직일때 새로운 Tk()를 하면 움직이던게 멈춰버린다.
        if self.start==True:
            self.timePause()  #Tk()와 다르게 터틀움직이는게 멈췃다가 다시 재개되지만 그래도 멈추긴하므로
        tk.messagebox.showinfo(message="사용설명서 : https://www.absdadsfjdsifhadoishfoiudashgagag.com")
        
    def read(self) :
        if path.exists('record.csv')==True:
            with open('record.csv','r') as f:
                for line in f.readlines():
                    tmp=[int(i) for i in line.split(',')]
                    self.day=tmp[0]+1
                    self.dayindex=self.day-1
                    self.earntotal+=tmp[1]
                    self.pastrecord.append(tmp)
        else :
            print('신규 유저입니다.')
                     
    def write(self) :
        if path.exists('record.csv')==True:
            with open('record.csv','a') as f:
                f.write(f'{self.day}, {self.earn}\n')
        else :
            print('저장파일이 손상되었습니다. 재기록을 실시합니다')
            with open('record.csv','w') as f:
                for p in self.pastrecord:
                    f.write(f'{p[0]}, {p[1]}\n')
    
if __name__ == '__main__':
    root = tk.Tk()
    simulator = Simulator(root)
    
    root.mainloop()
        
