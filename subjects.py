
schedule705day1 = ['Core',"Core","Français","Core","Core","Health/Art/Drama","Core","Core"]
schedule705day2= ['Core',"Français","Music","Core","Core","Core","Core","Physical Education"]
schedule705day3 = ['Core',"Core","Health/Art/Drama","Français","Core","Core","STEAM","Core"]
schedule705day4 = ['Core',"Français","Core","Core","Core","Physical Education","STEAM","Core"]
schedule705day5 = ['Core',"Music","Français","Core","Core","Core","Core","Health/Art/Drama"]

schedule805day1 = ['Math',"Math","Arts","Phys Ed.","Français","Science","Geography/Language Arts","Geography/Language Arts"]
schedule805day2 = ['Math',"Math","Français","Science","Language Arts","Music","Geography","Art"]
schedule805day3 = ['Math',"Math","Français","DPA","Language Arts","Music","STEAM","Geography/Language Arts"]
schedule805day4 = ['Math',"Math","Français","DPA","Language Arts","Core/Science","Core/Science","Phys Ed."]
schedule805day5 = ['Math',"Math","Français","Health","Language Arts","Core/Geography","Core/Geography","STEAM"]

def subdes(cls,day,period):
    if cls == '805':
        if day == '1':
            return schedule805day1[period-1]
        elif day == '2':
            return schedule805day2[period-1]
        elif day == '3':
            return schedule805day3[period-1]
        elif day == '4':
            return schedule805day4[period-1]
        else:
            return schedule805day5[period-1]
    else:
        if day == '1':
            return schedule705day1[period-1]
        elif day == '2':
            return schedule705day2[period-1]
        elif day == '3':
            return schedule705day3[period-1]
        elif day == '4':
            return schedule705day4[period-1]
        else:
            return schedule705day5[period-1]     

def sublist(cls,day):
    if cls == '805':
        if day == '1':
            return listtovar(schedule805day1) 
        elif day == '2':
            return listtovar(schedule805day2) 
        elif day == '3':
            return listtovar(schedule805day3) 
        elif day == '4':
            return listtovar(schedule805day4) 
        else:
            return listtovar(schedule805day5) 
    else:
        if day == '1':
            return listtovar(schedule705day1) 
        elif day == '2':
            return listtovar(schedule705day2) 
        elif day == '3':
            return listtovar(schedule705day3) 
        elif day == '4':
            return listtovar(schedule705day4)
        else:
            return listtovar(schedule705day5)  

def listtovar(input):
    txt = ""
    num = 1
    for item in input:
        txt += f"Period {num} : {item} \n"
        num += 1
    return txt
