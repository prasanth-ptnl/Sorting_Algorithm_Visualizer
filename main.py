from tkinter import *
import random
from tkinter import ttk
from bubbles import bubble_sort
from merges import merge_sort
from quicks import quick_sort

root = Tk()
root.title("Sorting Algorithms Vizulizer")
root.geometry("900x600+200+80")
root.config(bg="#082A46")
data = []

def startalgo():
	global data
	if algo_menu.get() == 'Quick Sort':
		quick_sort(data,0,len(data)-1,drawdata,Speed_Scale.get())
		drawdata(data,['green' for i in range(len(data))])
	elif algo_menu.get() == 'Bubble Sort':
		bubble_sort(data,drawdata,Speed_Scale.get())
	elif algo_menu.get() == 'Merge Sort':
		merge_sort(data,drawdata,Speed_Scale.get())
	
	drawdata(data,['red' for x in range(len(data))])

def Generate():
	global data
	minival = int(min_val.get())
	maxival = int(max_val.get())
	sizeval = int(size_val.get())
	data = []
	for i in range(sizeval):
		data.append(random.randrange(minival,maxival))
	
	drawdata(data,['red' for x in range(len(data))])

def drawdata(data,colorArray):
	canvas.delete("all")
	canvas_height = 450
	canvas_width = 870
	x_width = canvas_width/(len(data) +1)
	offset = 10
	spacing_bet_rect = 10
	normalized = [i/max(data) for i in data]

	for i,height in enumerate(normalized):
		x0 = i*x_width + offset + spacing_bet_rect
		y0 = canvas_height - height*400
		x1 = (i+1)*x_width
		y1 = canvas_height

		canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
		canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]),font=("Helvetica",12,"bold"),fill="orange")
	
	root.update_idletasks()

selected_algorithm = StringVar()

mainLabel = Label(root,text="Algorithm",font=("Helvetica",16,"bold"),bg="#05897a",width=10,fg="black",relief=GROOVE,bd=5)
mainLabel.place(x=0,y=0)

algo_menu = ttk.Combobox(root,width=15,font=("Helvetica",12,"bold"),textvariable=selected_algorithm,values=['Bubble Sort','Merge Sort','Quick Sort'])
algo_menu.place(x=145,y=0)

algo_menu.current(0)

randomgenerate = Button(root,text="Generate",bg="#2dae9a",font=("Helvetica",16,"bold"),relief=SUNKEN,activebackground="#05945b",activeforeground="white",bd=5,width=10,command=Generate)
randomgenerate.place(x=750,y=60)

size_valLabel = Label(root,text="Size",height=2,font=("Helvetica",12,"bold"),bg="#0e6da5",width=10,fg="black",relief=GROOVE,bd=5)
size_valLabel.place(x=0,y=60)

size_val = Scale(root,from_=0,to=20,resolution=1,orient=HORIZONTAL,font=("Helvetica",12,"bold"),relief=GROOVE,bd=2,width=10)
size_val.place(x=120,y=60)

min_valLabel = Label(root,text="Min Value",height=2,font=("Helvetica",12,"bold"),bg="#0e6da5",width=10,fg="black",relief=GROOVE,bd=5)
min_valLabel.place(x=250,y=60)

min_val = Scale(root,from_=0,to=20,resolution=1,orient=HORIZONTAL,font=("Helvetica",12,"bold"),relief=GROOVE,bd=2,width=10)
min_val.place(x=370,y=60)

max_valLabel = Label(root,text="Max Value",height=2,font=("Helvetica",12,"bold"),bg="#0e6da5",width=10,fg="black",relief=GROOVE,bd=5)
max_valLabel.place(x=500,y=60)

max_val = Scale(root,from_=20,to=50,resolution=1,orient=HORIZONTAL,font=("Helvetica",12,"bold"),relief=GROOVE,bd=2,width=10)
max_val.place(x=620,y=60)



startbtn = Button(root,text="Start",bg="#c45b09",font=("Helvetica",16,"bold"),relief=SUNKEN,activebackground="#05945b",activeforeground="white",bd=5,width=10,command=startalgo)
startbtn.place(x=750,y=0)

speedvalLabel = Label(root,text="Speed",height=2,font=("Helvetica",12,"bold"),bg="#0e6da5",width=10,fg="black",relief=GROOVE,bd=5)
speedvalLabel.place(x=400,y=0)


Speed_Scale = Scale(root,from_=0.1,to=5.0,resolution=1,orient=HORIZONTAL,font=("Helvetica",12,"bold"),relief=GROOVE,bd=2,width=10,length=200)
Speed_Scale.place(x=520,y=0)

canvas =Canvas(root,width=870,height=450,bg="black")
canvas.place(x=10,y=130)

root.mainloop()