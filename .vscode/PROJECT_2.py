import tkinter as tk
root = tk.Tk()
root.geometry("430x200")
root.title("Group3_Project#2")
root.configure(bg='#372A28')
font1=['Calibri',14, 'bold']
font2=['Georgia',13, 'normal']

lb1=tk.Label(root,text= ' Numbers:', font= font1, bg='#FFC61A', fg='black')
lb1.grid(row=1,column=1)
e1_str=tk.StringVar()
e1=tk.Entry(root,width=20,bg='#FFF4EA',font=font1,textvariable=e1_str)
e1.grid(row=1,column=2)

b1=tk.Button(root,text='Submit ',font=font1,command=lambda:my_upd(), bg='#FFD964')
b1.grid(row=1,column=3,padx=5,pady=10)

lb2=tk.Label(root,text='Sum, Mean \nand Number of Elements \nCalculator by Group 3', height=4, font=font2,anchor='center',justify='center',width=40,bg='#FFF4EA')
lb2.grid(row=2,column=1,padx=10,columnspan=3,sticky='w')

def my_upd():
    my_str=e1_str.get().split(',')
    my_list=list(map(int,my_str))
    #my_list= list(map(int,e1_str.get().split(',')))
    str1='No. of Elements : ' + str(len(my_list))
    str1=str1+ "\nSum of Elements : " + str(sum(my_list))
    str1=str1+ "\nAverage : " + str(sum(my_list)/len(my_list))
    lb2.config(text=str1)
root.mainloop()
