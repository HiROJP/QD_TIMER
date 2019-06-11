import math
import datetime
from tkinter import *
from tkinter import ttk

#TEST
#TEST
#QD_Drive定義表
Siren = 50511320
Goliath = 39337480
Drift = 42000700
Expedition = 43704980
Rush = 44123050
Beacon = 45958490
Eos = 46681120
Bolon = 70759160
Odyssey = 73686030
Crossfield = 84187440
Kama = 99314530
Pontes = 133904700

#船の選択------------------------------------------------------
def Select_Ship():

    global QD_Time
    global Select_Match_QD

    #Prospector/315p (.getじゃないとTkinker側で選択された船の名前を反映出来ない)
    if Check_Ship.get() == "Prospector" or Check_Ship.get() == "315p" or Check_Ship.get() == "Reliant Sen":
        QD_Time = Goliath
        #一度消す
        Label_QD(Output_QD_None)
        Output_QD = "Goliath"
        Label_QD(Output_QD)
    #Sabre/Razor EX
    elif Check_Ship.get() == "Sabre" or Check_Ship.get() == "Razor EX" or Check_Ship.get() == "Reliant Mako":
        QD_Time = Drift
        Label_QD(Output_QD_None)
        Output_QD = "Drift"
        Label_QD(Output_QD)
    #Avenger/Hurricane/Herald/300i
    elif Check_Ship.get() == "Avenger" or Check_Ship.get() == "Hurricane" or Check_Ship.get() == "Herald" or Check_Ship.get() == "300i":
        QD_Time = Expedition
        Label_QD(Output_QD_None)
        Output_QD = "Expedition"
        Label_QD(Output_QD)
    #Hawk/Mustang/Buccaneer/Razor/Razor LX/Reliant Kore/m50/Blade
    elif Check_Ship.get() == "Hawk" or Check_Ship.get() == "Mustang" or Check_Ship.get() == "Buccaneer" or Check_Ship.get() == "Razor" or Check_Ship.get() == "Razor LX" or Check_Ship.get() == "Reliant Kore" or Check_Ship.get() ==  "m50" or Check_Ship.get() == "Blade":
        QD_Time = Rush
        Label_QD(Output_QD_None)
        Output_QD = "Rush"
        Label_QD(Output_QD)
    #Eclipse/Gladius/Gladiator/325a/85X/Glaive/Scythe
    elif Check_Ship.get() == "Eclipse" or Check_Ship.get() == "Gladius" or Check_Ship.get() == "Gladiator" or Check_Ship.get() == "325a" or Check_Ship.get() == "85X" or Check_Ship.get() == "Reliant Tana" or Check_Ship.get() == "Glaive" or Check_Ship.get() == "Scythe":
        QD_Time = Beacon
        Label_QD(Output_QD_None)
        Output_QD = "Beacon"
        Label_QD(Output_QD)
    #Hornet/Terrapin/Cutlass/350r/Aurora/Constellation/Scout
    elif Check_Ship.get() == "Hornet" or Check_Ship.get() == "Terrapin" or Check_Ship.get() == "Cutlass" or Check_Ship.get() == "350r" or Check_Ship.get() == "Aurora" or Check_Ship.get() == "Constellation" or Check_Ship.get() == "Scout":
        QD_Time = Eos
        Label_QD(Output_QD_None)
        Output_QD = "Eos"
        Label_QD(Output_QD)
    #Caterpillar
    elif Check_Ship.get() == "Caterpillar":
        QD_Time = Bolon
        Label_QD(Output_QD_None)
        Output_QD = "Bolon"
        Label_QD(Output_QD)
    #600i/Freelancer\Freelancer MAX/Freelancer DUR/Valkyrie
    elif Check_Ship.get() == "600i" or Check_Ship.get() == "Freelancer" or Check_Ship.get() == "Freelancer DUR" or Check_Ship.get() == "Freelancer MAX" or Check_Ship.get() == "Valkyrie":
        QD_Time = Odyssey
        Label_QD(Output_QD_None)
        Output_QD = "Odyssey"
        Label_QD(Output_QD)
    #Retaliator/Vanguard/Freelancer MIS
    elif Check_Ship.get() == "Retaliator" or Check_Ship.get() == "Vanguard" or Check_Ship.get() == "Freelancer MIS":
        QD_Time = Crossfield
        Label_QD(Output_QD_None)
        Output_QD = "Crossfield"
        Label_QD(Output_QD)
    #Hammerhead/Reclaimer/Starfarer
    elif Check_Ship.get() == "Hammerhead" or Check_Ship.get() == "Reclaimer" or Check_Ship.get() == "Starfarer":
        QD_Time = Kama
        Label_QD(Output_QD_None)
        Output_QD = "Kama"
        Label_QD(Output_QD)
    #Starfarer Gemini
    elif Check_Ship.get() == "Starfarer Gemini":
        QD_Time = Pontes
        Label_QD(Output_QD_None)
        Output_QD = "Pontes"
        Label_QD(Output_QD)
    #機体からQDを選択すると表示画面が被るのでそれ対策
    #Label_QD(Output_QD)
    Label_Speed(QD_Time)
    #QDドライブの選択def
    Select_QD_Drive()
    #確認用
    print("--Check for test--")
    print(Check_Ship.get())


#QDドライブの選択------------------------------------------------------
def Select_QD_Drive():
    global QD_Time
    #Siren
    if Check_QD.get() == "Siren (50511320 m/s)":
        QD_Time = Siren
        Label_QD(Output_QD_None)
        Output_QD = "Siren"
        Label_QD(Output_QD)
    #Goliath
    if Check_QD.get() == "Goliath (39337480 m/s)":
        QD_Time = Goliath
        Label_QD(Output_QD_None)
        Output_QD = "Goliath"
        Label_QD(Output_QD)
    #Drift
    if Check_QD.get() == "Drift (42000700 m/s)":
        QD_Time = Drift
        Label_QD(Output_QD_None)
        Output_QD = "Drift"
        Label_QD(Output_QD)
    #Expedition
    if Check_QD.get() == "Expedition (43704980 m/s)":
        QD_Time = Expedition
        Label_QD(Output_QD_None)
        Output_QD = "Expedition"
        Label_QD(Output_QD)
    #Rush
    if Check_QD.get() == "Rush (44123050 m/s)":
        QD_Time = Rush
        Label_QD(Output_QD_None)
        Output_QD = "Rush"
        Label_QD(Output_QD)
    #Beacon
    elif Check_QD.get() == "Beacon (45958490 m/s)":
        QD_Time = Beacon
        Label_QD(Output_QD_None)
        Output_QD = "Beacon"
        Label_QD(Output_QD)
    #Eos
    elif Check_QD.get() == "Eos (46681120 m/s)":
        QD_Time = Eos
        Label_QD(Output_QD_None)
        Output_QD = "Eos"
        Label_QD(Output_QD)
    #Bolon
    elif Check_QD.get() == "Bolon (70759160 m/s)":
        QD_Time = Bolon
        Label_QD(Output_QD_None)
        Output_QD = "Bolon"
        Label_QD(Output_QD)
    #Odyssey
    if Check_QD.get() == "Odyssey (73686030 m/s)":
        QD_Time = Odyssey
        Label_QD(Output_QD_None)
        Output_QD = "Odyssey"
        Label_QD(Output_QD)
    #Crossfield
    elif Check_QD.get() == "Crossfield (84187440 m/s)":
        QD_Time = Crossfield
        Label_QD(Output_QD_None)
        Output_QD = "Crossfield"
        Label_QD(Output_QD)
    #Kama
    elif Check_QD.get() == "Kama (99314530 m/s)":
        QD_Time = Kama
        Label_QD(Output_QD_None)
        Output_QD = "Kama"
        Label_QD(Output_QD)
    #Pontes
    elif Check_QD.get() == "Pontes (133904700 m/s)":
        QD_Time = Pontes
        Label_QD(Output_QD_None)
        Output_QD = "Pontes"
        Label_QD(Output_QD)
    Label_Speed(QD_Time)
    #場所の選択
    Start_End_Distance()

#距離データ----------
#POからArcCorp: 42313076
#PO,Del: 1917188
#PO,micro: 57470075


#場所の選択------------------------------------------------------
def Start_End_Distance():

    QD_Start_Distance = Check_Start_Distance.get()
    QD_End_Distance = Check_End_Distance.get()

    global QD_Distance

    #POからHur
    if QD_Start_Distance == "Port Olisar" and QD_End_Distance == "Hurston":
        QD_Distance = 31922889
    #POからArc
    elif QD_Start_Distance == "Port Olisar" and QD_End_Distance == "ArcCorp":
        QD_Distance = 42313076
    #POからDel
    elif QD_Start_Distance == "Port Olisar" and QD_End_Distance == "Delamar":
        QD_Distance = 1917188   
    #POからmicro
    elif QD_Start_Distance == "Port Olisar" and QD_End_Distance == "microTech":
        QD_Distance = 57470075  
    #DelamarからHur
    elif QD_Start_Distance == "Delamar" and QD_End_Distance == "Hurston":
        QD_Distance = 38975676
    #DelamarからPO
    elif QD_Start_Distance == "Delamar" and QD_End_Distance == "Port Olisar":
        QD_Distance = 1917188
    #DelamarからArc
    elif QD_Start_Distance == "Delamar" and QD_End_Distance == "ArcCorp":
        QD_Distance = 43879844
    #Delamarからmicro
    elif QD_Start_Distance == "Delamar" and QD_End_Distance == "microTech":
        QD_Distance = 59043169
    #HurstonからDel
    elif QD_Start_Distance == "Hurston" and QD_End_Distance == "Delamar":
        QD_Distance = 38975676
    #HurstonからPO
    elif QD_Start_Distance == "Hurston" and QD_End_Distance == "Port Olisar":
        QD_Distance = 31922889
    #HurstonからArc
    elif QD_Start_Distance == "Hurston" and QD_End_Distance == "ArcCorp":
        QD_Distance = 22882850
    #Hurstonからmicro
    elif QD_Start_Distance == "Hurston" and QD_End_Distance == "microTech":
        QD_Distance = 38409115
    #ArcからPO
    elif QD_Start_Distance == "ArcCorp" and QD_End_Distance == "Port Olisar":
        QD_Distance = 42313076
    #ArcからHurston
    elif QD_Start_Distance == "ArcCorp" and QD_End_Distance == "Hurston":
        QD_Distance = 22882850
    #ArcからDal
    elif QD_Start_Distance == "ArcCorp" and QD_End_Distance == "Delamar":
        QD_Distance = 43879844
    #Arcからmicro
    elif QD_Start_Distance == "ArcCorp" and QD_End_Distance == "microTech":
        QD_Distance = 59463792
    #microからPO
    elif QD_Start_Distance == "microTech" and QD_End_Distance == "Port Olisar":
        QD_Distance = 57470075
    #microからHur
    elif QD_Start_Distance == "microTech" and QD_End_Distance == "Hurston":
        QD_Distance = 38409115
    #microからArc
    elif QD_Start_Distance == "microTech" and QD_End_Distance == "ArcCorp":
        QD_Distance = 59463792
    #microからDel
    elif QD_Start_Distance == "microTech" and QD_End_Distance == "Delamar":
        QD_Distance = 59043169
    Label_Distance(QD_Distance_None)
    Label_Distance(QD_Distance)
    Calculation()
    
#速度データ（実施）
#PO - Del
#Eos - 55s (理論値の約75%)
#Rush - 55s (理論値の約78%)
#Beacon - 54s (理論値の約76%)
#PO - Hur
#Beacon - 12:00  (理論値の約97%)

def Calculation():
    #QD式 ((距離 / (速度 * 3.6)) * 60 ²) = 時間
    QD_Second = ((QD_Distance / (QD_Time * 3.6)) * 60 * 60)

    print((str(math.ceil(QD_Second))) + "s")

    QD_Second02 = datetime.timedelta(seconds = QD_Second)
    print(str(QD_Second02))
    Label_Time(QD_Second02)

#所要時間表示
def Label_Time(x):
    Label_Time1 = ttk.Label(frame1, font=("",18),text=x, foreground='#ff0000', background='#ffaacc')
    Label_Time1.grid(row = 1, column = 5)
    Label_Time1.grid_configure(padx=5, pady=5)

#距離表示
def Label_Distance(x):
    Label_Distance1 = ttk.Label(frame1, font=("",18),text=(x), foreground='#ff0000', background='#ffaacc')
    Label_Distance1.grid(row = 2, column = 5)
    Label_Distance1.grid_configure(padx=5, pady=5)

#速度表示
def Label_Speed(x):
    Label_Speed1 = ttk.Label(frame1, font=("",18),text=(x), foreground='#ff0000', background='#ffaacc')
    Label_Speed1.grid(row = 3, column = 5)
    Label_Speed1.grid_configure(padx=5, pady=5)

#QD表示
def Label_QD(x):
    Label_QD1 = ttk.Label(frame1, font=("",18),text=(x), foreground='#0000cd', background='#6495ed')
    Label_QD1.grid(row = 4, column = 5)
    Label_QD1.grid_configure(padx=5, pady=5)

#更新確認用表示
def Check_Select(x):
    Check_Select1 = ttk.Label(frame1, font=("",8),text=x,background="#dcdcdc")
    Check_Select1.grid(row = 0, column = 3)
    Check_Select1.grid_configure(padx=0, pady=0)

#コンボボックス用:サイズ
def cb_selected0(event):
    Check_Ship_Size_Change()

#コンボボックス用:機体
def cb_selected1(event):
    print('Check = %s' % Check_Ship.get())
    #Label_QD(Output_QD_None)
    Select_Ship()
    QD_Size_Change()
    Check_Select(Output01)
    Check_Select(Check_Ship.get())

#コンボボックス用:QD
def cb_selected2(event):
    print('Check = %s' % Check_QD.get())
    #Label_QD(Output_QD_None)
    Select_Ship()
    Check_Select(Output01)
    Check_Select(Check_QD.get())
    
#コンボボックス用:出発星系場所
def cb_selected3a(event):
    print('Check = %s' % Check_Start_Star.get())
    Select_Star()

#コンボボックス用:到着星系場所
def cb_selected4a(event):
    print('Check = %s' % Check_End_Star.get())
    Select_End_Star()

#コンボボックス用:出発場所
def cb_selected3(event):
    print('Check = %s' % Check_Start_Distance.get())
    #Check_Selectは最初に呼び出さないとGUIが更新されない
    Check_Select(Output01)
    Check_Select(Check_Start_Distance.get())
    Select_Ship()

#コンボボックス用:到着場所
def cb_selected4(event):
    print('Check = %s' % Check_End_Distance.get())
    #Check_Selectは最初に呼び出さないとGUIが更新されない
    Check_Select(Output01)
    Check_Select(Check_End_Distance.get())
    #機体選択def---1
    Select_Ship()


if __name__ == '__main__':
    root = Tk()
    root.title('QD時間測定ちゃん_v1.1（対応バージョン: Alpha 3.5.0 1479378）')
    root.configure(bg='gray')
    # Frame
    frame1 = ttk.Frame(root, padding=23)
    frame1.grid()

    #初期起動def
    Output01 = "--------------------"
    Check_Select(Output01)
    QD_Second02 = "0:00:00.000000"
    Label_Time(QD_Second02)
    QD_Distance_None = "　　　---　　　"
    Label_Distance(QD_Distance_None)
    QD_Time = "　　　---　　　"
    Label_Speed(QD_Time)
    Output_QD_None = "　　　---　　　"
    Label_QD(Output_QD_None)

    # Combobox------------------------------
    #機体サイズ選択
    Check_Ship_Size = StringVar()
    # コンボボックスの作成(frame1に作成、stateで編集不可)
    cb0 = ttk.Combobox(frame1, state='readonly', textvariable = Check_Ship_Size,width=4)
    cb0.bind('<<ComboboxSelected>>', cb_selected0)
    cb0['values']=('小型', '中型', '大型',"キャピタル")
    cb0.set('小型')
    cb0.grid(row=1,column=2)
    cb0.grid_configure(padx=5, pady=5)

    Ship_Small_List = ["Prospector","Sabre","Avenger","Hurricane","Herald","300i","315p","325a","350r","85X","Hawk","Aurora","Mustang","Buccaneer","Razor","Razor LX","Razor EX","Reliant Kore","Reliant Mako","Reliant Sen","Reliant Tana","m50","Blade","Eclipse","Gladius","Gladiator","Hornet","Terrapin","Glaive","Scythe","Scout"]
    Ship_Medium_List = ["Cutlass","Constellation","Freelancer","Freelancer DUR","Freelancer MAX","Freelancer MIS","Valkyrie","Vanguard"]
    Ship_Large_List = ["600i","Retaliator","Hammerhead","Reclaimer","Starfarer","Starfarer Gemini"]

    Ship_QD_Small_List = ["Prospector","Sabre","Avenger","Hurricane","Herald","300i","315p","325a","350r","85X","Hawk","Aurora","Mustang","Buccaneer","Razor","Razor LX","Razor EX","Reliant Kore","Reliant Mako","Reliant Sen","Reliant Tana","m50","Blade","Eclipse","Gladius","Gladiator","Hornet","Terrapin","Glaive","Scythe","Scout","Cutlass","Constellation"]
    Ship_QD_Medium_List = ["600i","Retaliator","Freelancer","Freelancer DUR","Freelancer MAX","Freelancer MIS","Valkyrie","Vanguard"]
    Ship_QD_Large_List = ["Hammerhead","Reclaimer","Starfarer","Starfarer Gemini"]

    #機体選択
    Check_Ship = StringVar()
    # コンボボックスの作成(frame1に作成、stateで編集不可)
    cb1 = ttk.Combobox(frame1, state='readonly', textvariable = Check_Ship)
    cb1.bind('<<ComboboxSelected>>', cb_selected1)
    def Check_Ship_Size_Change():
        if Check_Ship_Size.get() == "小型":
            cb1['values']=(Ship_Small_List)
            cb1.set("Prospector")
        elif Check_Ship_Size.get() == "中型":
            cb1['values']=(Ship_Medium_List)
            cb1.set("Cutlass")            
        elif Check_Ship_Size.get() == "大型":
            cb1['values']=(Ship_Large_List)
            cb1.set("600i")
    #初期起動用: ないとデフォルトで機体が表示されない
    Check_Ship_Size_Change()
    cb1.grid(row=1,column=3)
    cb1.grid_configure(padx=5, pady=5)


    #QD選択
    Check_QD = StringVar()
    # コンボボックスの作成(frame1に作成、stateで編集不可)
    cb2 = ttk.Combobox(frame1, state='readonly', textvariable = Check_QD)
    cb2.bind('<<ComboboxSelected>>', cb_selected2)
    cb2['values']=("カスタマイズ時のみ選択")
    cb2.set("カスタマイズ時のみ選択")
    def QD_Size_Change():
        #for文でリストを繰り返さないとif文で一つづつ読み取れない
        for small in Ship_QD_Small_List:
            if Check_Ship.get() == small:
                cb2['values']=("デフォルト","Goliath (39337480 m/s)","Drift (42000700 m/s)","Expedition (43704980 m/s)","Rush (44123050 m/s)","Beacon (45958490 m/s)","Eos (46681120 m/s)","Siren (50511320 m/s)")
                cb2.set("デフォルト")
        for Medium in Ship_QD_Medium_List:     
            if Check_Ship.get() == Medium:
                cb2['values']=("デフォルト","Bolon (70759160 m/s)","Odyssey (73686030 m/s)","Crossfield (84187440 m/s)")
                cb2.set("デフォルト")
        for Large in Ship_QD_Large_List:  
            if Check_Ship.get() == Large:
                cb2['values']=("デフォルト","Kama (99314530 m/s)","Pontes (133904700 m/s)")
                cb2.set("デフォルト")
    cb2.grid(row=2,column=3)
    cb2.grid_configure(padx=5, pady=5)

    #出発星系選択
    Check_Start_Star = StringVar()
    # コンボボックスの作成(frame1に作成、stateで編集不可)
    cb0 = ttk.Combobox(frame1, state='readonly', textvariable = Check_Start_Star,width=4)
    cb0.bind('<<ComboboxSelected>>', cb_selected3a)
    cb0['values']=('Stanton')
    cb0.set('Stanton')
    cb0.grid(row=3,column=2)
    cb0.grid_configure(padx=5, pady=5)

    #出発場所選択
    Check_Start_Distance = StringVar()
    # コンボボックスの作成(frame1に作成、stateで編集不可)
    cb3 = ttk.Combobox(frame1, state='readonly', textvariable = Check_Start_Distance)
    def Select_Star():
        if Check_Start_Star.get() == "Stanton":
            cb3.bind('<<ComboboxSelected>>', cb_selected3)
            cb3['values']=("Port Olisar", "Delamar","Hurston","ArcCorp","microTech")
            cb3.set("Port Olisar")
    #初期起動用: ないとデフォルトで機体が表示されない
    Select_Star()
    cb3.grid(row=3,column=3)
    cb3.grid_configure(padx=5, pady=5)

    #到着星系選択
    Check_End_Star = StringVar()
    # コンボボックスの作成(frame1に作成、stateで編集不可)
    cb0 = ttk.Combobox(frame1, state='readonly', textvariable = Check_End_Star,width=4)
    cb0.bind('<<ComboboxSelected>>', cb_selected4a)
    cb0['values']=('Stanton')
    cb0.set('Stanton')
    cb0.grid(row=4,column=2)
    cb0.grid_configure(padx=5, pady=5)

    #到着場所選択
    Check_End_Distance = StringVar()
    # コンボボックスの作成(frame1に作成、stateで編集不可)
    cb4 = ttk.Combobox(frame1, state='readonly', textvariable = Check_End_Distance)
    cb4.bind('<<ComboboxSelected>>', cb_selected4)
    def Select_End_Star():
        if Check_End_Star.get() == "Stanton":
            cb4['values']=("Port Olisar","Delamar","Hurston","ArcCorp","microTech")
            cb4.set("Delamar")
    #初期起動用: ないとデフォルトで機体が表示されない
    Select_End_Star()
    cb4.grid(row=4,column=3)
    cb4.grid_configure(padx=5, pady=5)


    # 入力画面ラベルの設定------------------------------
    #使用する機体
    label1 = ttk.Label(frame1, font=("",12),text="使用する機体")
    label1.grid(row = 1, column = 1)
    label1.grid_configure(padx=5, pady=5)

    #QD選択
    label2 = ttk.Label(frame1, font=("",12),text="クアンタムドライブ")
    label2.grid(row = 2, column = 1)
    label2.grid_configure(padx=5, pady=5)

    #出発場所
    label3 = ttk.Label(frame1, font=("",12),text="出発予定地")
    label3.grid(row = 3, column = 1)
    label3.grid_configure(padx=5, pady=5)

    #到着場所
    label4 = ttk.Label(frame1, font=("",12),text="到着予定地",)
    label4.grid(row = 4, column = 1)
    label4.grid_configure(padx=5, pady=5)
    
    #時間
    label5 = ttk.Label(frame1, font=("",18),text="所要時間:",)
    label5.grid(row = 1, column = 4)
    label5.grid_configure(padx=5, pady=5)

    #計算式
    label6 = ttk.Label(frame1, font=("",8),text="(距離÷(速度×3.6))×60²",)
    label6.grid(row = 0, column = 5)
    label6.grid_configure(padx=0, pady=0)

    #距離
    label7 = ttk.Label(frame1, font=("",18),text="距離(km):",)
    label7.grid(row = 2, column = 4)
    label7.grid_configure(padx=5, pady=5)

    #速度
    label8 = ttk.Label(frame1, font=("",18),text="速度(m/s):",)
    label8.grid(row = 3, column = 4)
    label8.grid_configure(padx=5, pady=5)

    #使用QD
    label8 = ttk.Label(frame1, font=("",18),text="QD:",)
    label8.grid(row = 4, column = 4)
    label8.grid_configure(padx=5, pady=5)

    #　画像表示
    pngfile=PhotoImage(file="Wiki-wordmark.png")
    cv=Canvas(bg="black",width=680-1,height=38-1)
    cv.create_image(0,0,image=pngfile,anchor=NW)
    cv.grid(row=2, column=0)

    root.mainloop()


