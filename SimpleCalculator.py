from tkinter import *
import tkinter as tk
import tkinter.font as ft

# Root Title, Icon, Color and Size 
root = Tk()
root.maxsize(408,518)
icon = PhotoImage(file = "calculator.png")
root.iconphoto(True,icon)
root.title("Simple Calculator")
# Root.geometry("420x600")
root.configure(bg = "#000000")
# Root is ready

# Defining my font that I am going to Use throughout the code
myFont = ft.Font(weight = "bold")
# Done



# Display of Calculator is an Entry
displayScreeenEntry = Entry(root,width = 22, borderwidth = 5, bg= "#303030", fg = "#ffffff",font=myFont)
displayScreeenEntry.grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5,ipady=5)
#Put it onto the root Screen using GRID

# Commands of the buttons

# Clear the screen
def clrClick():
	displayScreeenEntry.delete(0,END)

# Pressing the numbers will do this 
def numberButton(number):
	#GET() input and Save the number in "old" 
	old = displayScreeenEntry.get()
	#delete everything in the  screen 
	# If you don't delete what's on the screen the same string will be there and the insert function will add it again on the screen
	# Try commenting the next line: You will understand
	displayScreeenEntry.delete(0,END)
	#insert it in the screen
	displayScreeenEntry.insert(0,str(old)+str(number))

# When you press a number and then press an operator like +, -, *, /,REM the following things will happen
def operatorClick(st):

	# The parameter st will contain a string depending upon which operator is pressed
	# The value of st is stored in a global 
	global math
	math = st
	# GET() the number on the screen in a variable "first"
	first = displayScreeenEntry.get()
	global f
	# Assign the value of "first" in a global variable "f" so that we can use the value in eqlClick() function
	f = float(first)
	# Clear the screen to enter the next number
	# Then you press another number and numberButton
	displayScreeenEntry.delete(0,END)




def pntClick():
	old = displayScreeenEntry.get()
	displayScreeenEntry.delete(0,END)
	new = str(old) + "."
	displayScreeenEntry.insert(0,new)

def eqlClick():
	second = displayScreeenEntry.get()
	s = float(second)
	displayScreeenEntry.delete(0,END)
	if math== "ADD":
		result = f+s
		if result-int(result)==0:
			result=int(result)
		print("{}+{} = {}".format(f,s,result))
		displayScreeenEntry.insert(0,result)
	elif math == "SUB":
		result = f-s
		if result-int(result)==0:
			result=int(result)
		print("{}-{} = {}".format(f,s,result))
		displayScreeenEntry.insert(0,result)
	elif math == "MUL":
		result = f*s
		if result-int(result)==0:
			result=int(result)
		print("{}*{} = {}".format(f,s,result))
		displayScreeenEntry.insert(0,result)
	elif math == "DIV":
		if second==0:
			print("Divide_By_Zero")
			displayScreeenEntry.insert(0,0)
		else: 
			result = f/s
			if result-int(result)==0:
				result=int(result)
			print("{}/{} = {}".format(f,s,result))
			displayScreeenEntry.insert(0,result)
	elif math == "REM":
		result = f%s
		if result-int(result)==0:
			result=int(result)
		print("{}/{} gives {} as remainder".format(f,s,result))
		displayScreeenEntry.insert(0,result)
	elif math == "PER":
		result = f/100*s
		if result-int(result)==0:
			result=int(result)
		print("{}% of {} = {}".format(f,s,result))
		displayScreeenEntry.insert(0,result)

# Now we need Buttons 0-9
# Normally in 'command' attribute we cannot use '()' while calling a function
# Using lambda we can use the "()" and also pass parameters in the function
# Activebackground changes the color of the button when pressed
# State can have DISABLED/NORMAL values only
Button_1 = Button(root, text = "1",height=5,width=13, command =lambda: numberButton(1), bg="#080808",fg="#ffffff", activebackground = "#606060", state = DISABLED)
Button_2 = Button(root, text = "2", height=5,width=13, command =lambda: numberButton(2), bg="#080808",fg="#ffffff", activebackground = "#606060", state = DISABLED)
Button_3 = Button(root, text = "3", height=5,width=13, command =lambda: numberButton(3), bg="#080808",fg="#ffffff", activebackground = "#606060", state = DISABLED)
Button_4 = Button(root, text = "4", height=5,width=13, command =lambda: numberButton(4), bg="#080808",fg="#ffffff", activebackground = "#606060", state = DISABLED)
Button_5 = Button(root, text = "5", height=5,width=13, command =lambda: numberButton(5), bg="#080808",fg="#ffffff", activebackground = "#606060", state = DISABLED)
Button_6 = Button(root, text = "6", height=5,width=13, command =lambda: numberButton(6), bg="#080808",fg="#ffffff", activebackground = "#606060", state = DISABLED)
Button_7 = Button(root, text = "7", height=5,width=13, command =lambda: numberButton(7), bg="#080808",fg="#ffffff", activebackground = "#606060", state = DISABLED)
Button_8 = Button(root, text = "8", height=5,width=13, command =lambda: numberButton(8), bg="#080808",fg="#ffffff", activebackground = "#606060", state = DISABLED)
Button_9 = Button(root, text = "9", height=5,width=13, command =lambda: numberButton(9), bg="#080808",fg="#ffffff", activebackground = "#606060", state = DISABLED)
Button_0 = Button(root, text = "0", height=5,width=13, command =lambda: numberButton(0), bg="#080808",fg="#ffffff", activebackground = "#606060", state = DISABLED)

Button_pnt = Button(root, text = ". ", height=5,width=13, command =lambda: pntClick(), activebackground = "#606060",bg = "#404040", state = DISABLED)
Button_eql = Button(root, text = "=", height=5,width=28, command =lambda: eqlClick(), activebackground = "#606060",bg = "#20B2AA", state = DISABLED)


Button_pls = Button(root, text = "+", height=5,width=13, command =lambda: operatorClick("ADD"), activebackground = "#606060",bg = "#404040", state = DISABLED)
Button_sub = Button(root, text = "-", height=5,width=13, command =lambda: operatorClick("SUB"), activebackground = "#606060",bg = "#404040", state = DISABLED)
Button_div = Button(root, text = "/", height=5,width=13, command =lambda: operatorClick("DIV"), activebackground = "#606060",bg = "#404040", state = DISABLED)
Button_mul = Button(root, text = "X", height=5,width=13, command =lambda: operatorClick("MUL"), activebackground = "#606060",bg = "#404040", state = DISABLED)

Button_rem = Button(root, text = "Rem", height=5,width=13, command =lambda: operatorClick("REM"), activebackground = "#606060",bg = "#404040", state = DISABLED)
Button_per = Button(root, text = "%", height=5,width=13, command =lambda: operatorClick("PER"), activebackground = "#606060",bg = "#404040", state = DISABLED)
Button_clr = Button(root, text = "CLEAR", height=5,width=13, command =lambda: clrClick(), activebackground = "#606060",bg = "#404040", state = DISABLED)




#Put it ontothe screen using GRID
Button_7.grid(row = 2,column = 0)
Button_8.grid(row = 2,column = 1)
Button_9.grid(row = 2,column = 2)

Button_4.grid(row = 3,column = 0)
Button_5.grid(row = 3,column = 1)
Button_6.grid(row = 3,column = 2)

Button_1.grid(row = 4,column = 0)
Button_2.grid(row = 4,column = 1)
Button_3.grid(row = 4,column = 2)

Button_0.grid(row = 5, column = 0)
Button_pnt.grid(row = 5, column = 1)
Button_eql.grid(row = 5, column = 2, columnspan = 2)
# Columnspan joins a said number of columns
# We can also use rawspan to join rows
Button_pls.grid(row = 4, column = 3)
Button_sub.grid(row = 3, column = 3)
Button_mul.grid(row = 2, column = 3)

Button_clr.grid(row = 1, column = 2)
Button_div.grid(row = 1, column = 3)
Button_per.grid(row = 1, column = 0)
Button_rem.grid(row = 1, column = 1)

# The power function Enables/Disables all the buttons
def power():
	displayScreeenEntry.delete(0,END)
	if Button_eql['state'] == tk.DISABLED:
		Button_eql['state'] = tk.NORMAL
	elif Button_eql['state'] == tk.NORMAL:
		Button_eql['state'] = tk.DISABLED

	if Button_pls['state'] == tk.DISABLED:
		Button_pls['state'] = tk.NORMAL
	elif Button_pls['state'] == tk.NORMAL:
		Button_pls['state'] = tk.DISABLED

	if Button_sub['state'] == tk.DISABLED:
		Button_sub['state'] = tk.NORMAL
	elif Button_sub['state'] == tk.NORMAL:
		Button_sub['state'] = tk.DISABLED

	if Button_mul['state'] == tk.DISABLED:
		Button_mul['state'] = tk.NORMAL
	elif Button_mul['state'] == tk.NORMAL:
		Button_mul['state'] = tk.DISABLED

	if Button_div['state'] == tk.DISABLED:
		Button_div['state'] = tk.NORMAL
	elif Button_div['state'] == tk.NORMAL:
		Button_div['state'] = tk.DISABLED

	if Button_clr['state'] == tk.DISABLED:
		Button_clr['state'] = tk.NORMAL
	elif Button_clr['state'] == tk.NORMAL:
		Button_clr['state'] = tk.DISABLED

	if Button_rem['state'] == tk.DISABLED:
		Button_rem['state'] = tk.NORMAL
	elif Button_rem['state'] == tk.NORMAL:
		Button_rem['state'] = tk.DISABLED

	if Button_per['state'] == tk.DISABLED:
		Button_per['state'] = tk.NORMAL
	elif Button_per['state'] == tk.NORMAL:
		Button_per['state'] = tk.DISABLED

	if Button_pnt['state'] == tk.DISABLED:
		Button_pnt['state'] = tk.NORMAL
	elif Button_pnt['state'] == tk.NORMAL:
		Button_pnt['state'] = tk.DISABLED

	if Button_1['state'] == tk.DISABLED:
		Button_1['state'] = tk.NORMAL
	elif Button_1['state'] == tk.NORMAL:
		Button_1['state'] = tk.DISABLED

	if Button_2['state'] == tk.DISABLED:
		Button_2['state'] = tk.NORMAL
	elif Button_2['state'] == tk.NORMAL:
		Button_2['state'] = tk.DISABLED

	if Button_3['state'] == tk.DISABLED:
		Button_3['state'] = tk.NORMAL
	elif Button_3['state'] == tk.NORMAL:
		Button_3['state'] = tk.DISABLED

	if Button_4['state'] == tk.DISABLED:
		Button_4['state'] = tk.NORMAL
	elif Button_4['state'] == tk.NORMAL:
		Button_4['state'] = tk.DISABLED

	if Button_5['state'] == tk.DISABLED:
		Button_5['state'] = tk.NORMAL
	elif Button_5['state'] == tk.NORMAL:
		Button_5['state'] = tk.DISABLED

	if Button_6['state'] == tk.DISABLED:
		Button_6['state'] = tk.NORMAL
	elif Button_6['state'] == tk.NORMAL:
		Button_6['state'] = tk.DISABLED

	if Button_7['state'] == tk.DISABLED:
		Button_7['state'] = tk.NORMAL
	elif Button_7['state'] == tk.NORMAL:
		Button_7['state'] = tk.DISABLED

	if Button_8['state'] == tk.DISABLED:
		Button_8['state'] = tk.NORMAL
	elif Button_8['state'] == tk.NORMAL:
		Button_8['state'] = tk.DISABLED

	if Button_9['state'] == tk.DISABLED:
		Button_9['state'] = tk.NORMAL
	elif Button_9['state'] == tk.NORMAL:
		Button_9['state'] = tk.DISABLED

	if Button_0['state'] == tk.DISABLED:
		Button_0['state'] = tk.NORMAL
	elif Button_0['state'] == tk.NORMAL:
		Button_0['state'] = tk.DISABLED
# Creating the Power Button
powerButton = Button(root,text = "ON/OFF", height = 5, width = 13, command = lambda: power(), bg = "#EA3C53")
powerButton.grid(row = 0, column = 3)

root.mainloop()