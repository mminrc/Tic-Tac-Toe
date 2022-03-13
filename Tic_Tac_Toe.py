from tkinter import*
from tkinter  import ttk
from tkinter import messagebox

GUI = Tk()

w = 500
h = 500

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()

x = (ws/2)-(w/2)
y = (hs/2)-(h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')
GUI.title("Tic Tac Toe By: Min Narongchai")
# x starts so true
clicked = True
count = 0

# disable all buttons
def disable_all_buttons():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)

# Check to see if someone won
def checkifwon():
	global winner
	winner = False

	if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" :
		b1.config(bg="red") 
		b2.config(bg="red") 
		b3.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","X Win")
		disable_all_buttons()
	elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" :
		b4.config(bg="red") 
		b5.config(bg="red") 
		b6.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","X Win")
		disable_all_buttons()
	elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" :
		b7.config(bg="red") 
		b8.config(bg="red") 
		b9.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","X Win")
		disable_all_buttons()
	elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" :
		b1.config(bg="red") 
		b4.config(bg="red") 
		b7.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","X Win")
		disable_all_buttons()
	elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" :
		b2.config(bg="red") 
		b5.config(bg="red") 
		b8.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","X Win")
		disable_all_buttons()
	elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" :
		b3.config(bg="red") 
		b6.config(bg="red") 
		b9.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","X Win")
		disable_all_buttons()
	elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" :
		b1.config(bg="red") 
		b5.config(bg="red") 
		b9.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","X Win")
		disable_all_buttons()
	elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" :
		b3.config(bg="red") 
		b5.config(bg="red") 
		b7.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","X Win")
		disable_all_buttons()
	# ตรวจสอบ O ชนะ
	elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" :
		b1.config(bg="red") 
		b1.config(bg="red") 
		b1.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","O Win")
		disable_all_buttons()
	elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" :
		b4.config(bg="red") 
		b5.config(bg="red") 
		b6.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","O Win")
		disable_all_buttons()
	elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" :
		b7.config(bg="red") 
		b8.config(bg="red") 
		b9.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","O Win")
		disable_all_buttons()
	elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" :
		b1.config(bg="red") 
		b4.config(bg="red") 
		b7.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","O Win")
		disable_all_buttons()
	elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" :
		b2.config(bg="red") 
		b5.config(bg="red") 
		b8.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","O Win")
		disable_all_buttons()
	elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" :
		b3.config(bg="red") 
		b6.config(bg="red") 
		b9.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","O Win")
		disable_all_buttons()
	elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" :
		b1.config(bg="red") 
		b5.config(bg="red") 
		b9.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","O Win")
		disable_all_buttons()
	elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" :
		b3.config(bg="red") 
		b5.config(bg="red") 
		b7.config(bg="red") 
		winner = True
		messagebox.showinfo("Tic Tac Toe","O Win")
		disable_all_buttons()

	elif count == 9 and winner == False:
		messagebox.showinfo('Tic Tac Toe',"Draw")
		disable_all_buttons()

def b_click(b):
	global clicked,count	
	if b["text"] == "" and clicked == True:
		b["text"] = "X"
		clicked = False
		count += 1
		checkifwon()
	elif b["text"] == "" and clicked == False:
		b["text"] = "O"
		clicked = True
		count += 1
		checkifwon()
	else:
		messagebox.showerror("Tic Tac Toe","ช่องนั้นถูกเลือกไปแล้ว\nกรุณาเลือกช่องใหม่")

# reset
def reset():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9
	global clicked, count
	clicked = True
	count = 0
	# สร้าง Button
	b1 = Button(GUI,text='',font=("Angsana New",20),height=4,width=9,padx=7,pady=10,bg='#654321',command=lambda: b_click(b1))
	b2 = Button(GUI,text='',font=("Angsana New",20),height=4,width=9,padx=7,pady=10,bg='#654321',command=lambda: b_click(b2))
	b3 = Button(GUI,text='',font=("Angsana New",20),height=4,width=9,padx=7,pady=10,bg='#654321',command=lambda: b_click(b3))

	b4 = Button(GUI,text='',font=("Angsana New",20),height=4,width=9,padx=7,pady=10,bg='#654321',command=lambda: b_click(b4))
	b5 = Button(GUI,text='',font=("Angsana New",20),height=4,width=9,padx=7,pady=10,bg='#654321',command=lambda: b_click(b5))
	b6 = Button(GUI,text='',font=("Angsana New",20),height=4,width=9,padx=7,pady=10,bg='#654321',command=lambda: b_click(b6))

	b7 = Button(GUI,text='',font=("Angsana New",20),height=4,width=9,padx=7,pady=10,bg='#654321',command=lambda: b_click(b7))
	b8 = Button(GUI,text='',font=("Angsana New",20),height=4,width=9,padx=7,pady=10,bg='#654321',command=lambda: b_click(b8))
	b9 = Button(GUI,text='',font=("Angsana New",20),height=4,width=9,padx=7,pady=10,bg='#654321',command=lambda: b_click(b9))

	# Grid our buttons to the screen
	b1.grid(row=0,column=0)
	b2.grid(row=0,column=1)
	b3.grid(row=0,column=2)

	b4.grid(row=1,column=0)
	b5.grid(row=1,column=1)
	b6.grid(row=1,column=2)

	b7.grid(row=2,column=0)
	b8.grid(row=2,column=1)
	b9.grid(row=2,column=2)

# สร้างปุ่มเมนู
my_menu = Menu(GUI)
GUI.config(menu=my_menu)

# สร้างตัวเลือกให้ปุ่ม
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label = "Options", menu=option_menu)
option_menu.add_command(label="Rest Game", command=reset)

reset()
GUI.mainloop()