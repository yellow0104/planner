#이 코드는 위정우가 심심해서 만든것입니다.(뉴비가)

from tkinter import *
from datetime import datetime

time = datetime.now()
year = time.year
month = time.month
day = time.day

a = f"{year}-{month}-{day}"

root = Tk()
root.geometry("650x800+600+0")
root.resizable(False, False)
root.title("planner")
label_day = Label(root, text=f"{a} 작성", font=("궁서체", 10))
label_day.pack()
label = Label(root, text="플래너", font=("궁서체", 30))
label.pack()
label_made = Label(root, text="위정우 제작", font=("나눔명조", 10))
label_made.pack()
label_made.place(x="450")
txt = Text(root)
txt.pack()
txt.insert(END, f"1.아침에 할것:\n\n\n\n2.점심에할것:\n\n\n\n3.저녁에할것\n\n\n\n{a}작성")
def click_1():    
    t = txt.get("1.0", END)
    
    with open("plan.txt", "w", encoding="utf-8") as f:
        f.write(t)

def click_2():
    with open("plan.txt", "r", encoding="utf-8") as f:
        read = f.read()
        print(f"오늘할일\n{read}")
        label2.config(text=read)

label2 = Label(root, text="(내용)", font=("나눔고딕", 10))
label2.pack()
save = Button(root, text="눌러서 저장", command=click_1)
save.pack()

r = Button(root, text="눌러서 확인", command=click_2)
r.pack()

save.place(x=10, y=10)
r.place(x=100, y=10)


root.mainloop()
