from tkinter import *                   #Import tkinter library

first_num=second_num=operator=None

def get_digit(digit):
    current= result_label['text']
    new = current+str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_num,operator

    first_num = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_num,second_num,operator

    second_num=int(result_label['text'])

    if operator=='+':
        result_label.config(text=str(first_num+second_num))
    elif operator=='-':
        result_label.config(text=str(first_num-second_num))
    elif operator=='*':
        result_label.config(text=str(first_num*second_num))
    else:
        if second_num==0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_num/second_num,3))) 


root =Tk()                              #Create an instance of tkinter frame or window
root.title('CALCULATOR')                #Title of the object
root.geometry('300x330')                #size of the object     
root.resizable(0,0)                     #to fix the size of the object 
root.configure(background='black')      #background colour of the object 

result_label = Label(root,text='',bg="black",fg="white")
result_label.grid(row=0,column=0,columnspan=5,pady=(15,10),sticky='w')
result_label.config(font=('verdana',30,'bold'))

btn7 = Button(root,text="7",bg="blue",fg="white",width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=("verdana",14,'bold'))

btn8 = Button(root,text="8",bg="blue",fg="white",width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=("verdana",14,'bold'))

btn9 = Button(root,text="9",bg="blue",fg="white",width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=("verdana",14,'bold'))

btn_add = Button(root,text="+",bg="blue",fg="white",width=5,height=2,command=lambda:get_operator('+'))
btn_add.grid(row=1,column=4)
btn_add.config(font=("verdana",14,'bold'))

btn4 = Button(root,text="4",bg="blue",fg="white",width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=("verdana",14,'bold'))

btn5 = Button(root,text="5",bg="blue",fg="white",width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=("verdana",14,'bold'))

btn6 = Button(root,text="6",bg="blue",fg="white",width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=("verdana",14,'bold'))

btn_sub = Button(root,text="-",bg="blue",fg="white",width=5,height=2,command=lambda:get_operator('-'))
btn_sub.grid(row=2,column=4)
btn_sub.config(font=("verdana",14,'bold'))

btn1 = Button(root,text="1",bg="blue",fg="white",width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=("verdana",14,'bold'))

btn2 = Button(root,text="2",bg="blue",fg="white",width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=("verdana",14,'bold'))

btn3 = Button(root,text="3",bg="blue",fg="white",width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=("verdana",14,'bold'))

btn_mul = Button(root,text="*",bg="blue",fg="white",width=5,height=2,command=lambda:get_operator('*'))
btn_mul.grid(row=3,column=4)
btn_mul.config(font=("verdana",14,'bold'))

btn_clr = Button(root,text="C",bg="blue",fg="white",width=5,height=2,command=lambda:clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=("verdana",14,'bold'))

btn0 = Button(root,text="0",bg="blue",fg="white",width=5,height=2,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=("verdana",14,'bold'))

btn_eq = Button(root,text="=",bg="blue",fg="white",width=5,height=2,command=get_result)
btn_eq.grid(row=4,column=2)
btn_eq.config(font=("verdana",14,'bold'))

btn_div = Button(root,text="/",bg="blue",fg="white",width=5,height=2,command=lambda:get_operator('/'))
btn_div.grid(row=4,column=4)
btn_div.config(font=("verdana",14,'bold'))
root.mainloop()
