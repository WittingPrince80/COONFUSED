
from tkinter import *
root= Tk()

root.title("Fibonacci")
root.geometry("400x200")

label_series = Label(root, text="Fibonacci Series:")
label_flower = Label(root)
label_spiral = Label(root)

enter_num = Entry(root)
enter_num.place(relx= 0.5,rely = 0.6, anchor = CENTER)

def Fibonacci():
   num = enter_num.get()
   FN = 0
   SN = 1
   sum = 0
   counter = 1
   while (counter <= num):
       label_series["text"] += str(sum) + " "
       counter = counter + 1 
       FN = SN
       SN = sum
       sum = FN + SN
   label_flower["text"] = "Flower is fully bloomed"
   
btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)

btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()