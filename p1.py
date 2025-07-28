
filnam = "myfile.txt"
f1 = False

def load_file():
    try :
        with open(filnam , "r" , encoding="utf-8") as file :
            tasks = [line.strip() for line in file.readlines()]
            return tasks
    except FileNotFoundError :
        tasks = []
        return tasks


def add_task(tasks):
    v = input('لطفا وظیفه خود را وارد کنید: ')
    tasks.append(v)
    out = save_file(tasks)
    if out==True :
        print("وظیفه اضافه شد.")
    #return tasks

def delet_task(tasks):
    show_task(tasks)
    d = int(input("کدام گزینه حذف شود؟ "))
    if 0<= d < len(tasks):
        removed = tasks.pop(d-1)
        print(f"{removed} حذف شد!")
        print("کار های باقی مانده:")
        show_task(tasks)
        save_file(tasks)
            
    
def save_file(tasks):
    try :
        with open(filnam , "w" , encoding="utf-8") as file:
            for line in tasks:
                file.write(line + "\n")
            f1 = True
        return f1
    except Exception as e :           # ارور را نشون میده
        print("وظیفه ای برای ذخیره وجود ندارد.")
        return (print (f"i cant do {e}."))

def show_task(tasks):
    if not tasks :
        print("وظیفه ای وجود ندارد.")
    else:
        for i, j in enumerate(tasks,1):
            if j.strip():
                print(f"{i}. {j}")
        
    
def menu():
    while(True):
        vazife = load_file()
        print("1. افزودن ")
        print("2. نمایش ")
        print("3. حذف ")
        print("4. خروج ")
        
        g = input('گزینه موردنظر خود را وارد کنید: ')
        
        if g=='1' :
            vazife = add_task(vazife)
            #save_file(vazife)
                
                
        elif g=='2' :
            show_task(vazife)
                
                
        elif g=='3' :
            delet_task(vazife)
                
                
        elif g=='4' :
            break
            
            
        # elif g=='5' :


menu()



#########################################


import os
print(os.getcwd())






























# print("1. افزودن ")
# print("2. نمایش ")
# print("3. حذف ")
# print("4. ذخیره ")
# print("5. خروج ")

# g = input('گزینه موردنظر خود را وارد کنید: ')

# if g=='1' :
    
    
# elif g=='2' :
    
    
# elif g=='3' :
    
    
# elif g=='4' :
    
    
# elif g=='5' :
    
    

