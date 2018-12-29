# ===========================================
# 利用tkinter英里和公里转换 时分秒转换,求速度

# class Conversion:

# 	def __init__(self, km, mi, li):
# 		self.km = km
# 		self.mi = mi
# 		self.li = li


# 	def mi_to_km(self):
# 		"""接受英里参数得到公里"""
# 		s = 1/1.62
# 		return self.mi*s

# 	def km_to_mi(self):
# 		'''1英里 = 1.62公里
# 			接收公里参数得到英里'''
# 		return self.km*1.62

# 	def km_to_li(s):
# 		"""接受公里得到里"""
# 		return self.km*2

# 	def li_to_km(s):
# 		"""接受里得到公里"""
# 		return self.km/2


# class Timeconversion:

# 	def __init__(self, hours, minutes, seconds):
		
# 		self.hours = hours
# 		self.minutes = minutes
# 		self.seconds = seconds

# 	def get_hours(self):
# 		"""接受参数换算成小时"""
# 		m = 1/60 # 1分钟等多1/60小时
# 		s = 1/3600 # 1秒等于1/3600小时
# 		return self.hours+self.minutes*m+self.seconds*s

# 	def get_minutes(self):
# 		"""接受参数换算成分"""
# 		h = 60
# 		s = 1/60
# 		return self.hours*h+self.minutes+self.seconds*s

# 	def get_seconds(self):
# 		"""接受参数换算成秒"""
# 		h = 3600
# 		m = 60
# 		return self.hour*h+self.minutes*m+self.seconds

# from tkinter import *


# def root_1():

	
# 	root1 = Tk()
# 	root1.title("主页面")
# 	root1.geometry("300x300")

# 	root_lable = Label(root1, text="欢迎使用公里转换\n计算平均速度软件")
# 	root_lable.pack(side=TOP,fill=X)
# 	root_lable.config(height=5,bg="pink",font=("",20,""))


# 	# root1.update()
# 	print(root1.winfo_x(),root1.winfo_y())

# 	huansuan = Button(root1,text="换算",command=(lambda:root_2(root1)))
# 	huansuan.pack(fill=X)
# 	huansuan.config(font=("",16,""))

# 	jisuan = Button(root1, text="计算")
# 	jisuan.pack(fill=X)
# 	jisuan.config(font=("",16,""))
# 	root1.mainloop()


# def back(top1,root1):
# 	top1.destroy() 	# 关闭top1窗口
# 	root1.geometry("300x300") # 将主重开从"0x0"设置会"300x300"


# def make_lmk(top1,root1):
# 	top1.destroy()
# 	top2 = Toplevel()
# 	top2.geometry("300x300")
# 	top2.config(bg="white")

# 	var = IntVar()
# 	var_entry_label = StringVar()

# 	top2.columnconfigure(0,weight=1) # 横列居中
# 	top2.rowconfigure(0,weight=1) # 竖列居
# 	top2.rowconfigure(1,weight=1) # 竖列居
# 	top2.rowconfigure(2,weight=1) # 竖列居
# 	top2.rowconfigure(3,weight=1) # 竖列居
# 	top2.rowconfigure(4,weight=1) # 竖列居
# 	top2.rowconfigure(5,weight=1) # 竖列居
# 	f0 = Frame(top2)
# 	Label(f0,text="请输入数值\n并选择填入数值的单位", font=20,bg="pink").grid(row=0)
# 	f0.grid(row=0)

# 	f1 = Frame(top2)
# 	Entry(f1,text="", textvariable=var).grid(row=1, column=0)
# 	var.set(0)
# 	Label(f1,text="", textvariable=var_entry_label,width=10).grid(row=1,column=1)
# 	var_entry_label.set("单位")
# 	f1.grid(row=1)




# 	f2 = Frame(top2)
# 	f2_b1 = Button(f2,text="英里(MI)")
# 	f2_b2 = Button(f2,text="公里(KM)")
# 	f2_b3 = Button(f2,text="里(LI)")

# 	f2_b1.config(command=(lambda:make_label_to_kml("MI",f2_b1,f2_b2,f2_b3)))
# 	f2_b2.config(command=(lambda:make_label_to_kml("KM",f2_b1,f2_b2,f2_b3)))
# 	f2_b3.config(command=(lambda:make_label_to_kml("LI",f2_b1,f2_b2,f2_b3)))
	
# 	f2_b1.grid(row=2,column=0)
# 	f2_b2.grid(row=2,column=1)
# 	f2_b3.grid(row=2,column=2)
# 	f2.grid(row=2)
	



# 	f3 = Frame(top2)
# 	Label(f3,text="请选择得到的结果单位", font=20,bg="pink").grid(row=3)
# 	f3.grid(row=3)
	



# 	f4 = Frame(top2)
	
# 	f4_b1 = Button(f4,text="英里(MI)")
# 	f4_b2 = Button(f4,text="公里(KM)")
# 	f4_b3 = Button(f4,text="里(LI)")
# 	var_f4_button = StringVar()
# 	var_f4_button
# 	f4_b1.config(command=(lambda:make_label_to_kml(args="MI",button_1=f4_b1,button_2=f4_b2,button_3=f4_b3,var=var,var_entry_label=var_entry_label,var_f4_button=var_f4_button)))
# 	f4_b2.config(command=(lambda:make_label_to_kml(args="KM",button_1=f4_b1,button_2=f4_b2,button_3=f4_b3)))
# 	f4_b3.config(command=(lambda:make_label_to_kml(args="LI",button_1=f4_b1,button_2=f4_b2,button_3=f4_b3)))

# 	f4_b1.grid(row=4,column=0)
# 	f4_b2.grid(row=4,column=1)
# 	f4_b3.grid(row=4,column=2)
# 	f4.grid(row=4)
	





# 	f5 = Frame(top2)
# 	Button(f5,text="确认").grid(row=5, column=0)
# 	Button(f5,text="取消").grid(row=5,column=1)
# 	Button(f5,text="重置").grid(row=5,column=2)
# 	f5.grid(row=5)
	
# def make_label_to_kml(args,button_1,button_2,button_3,var_entry_label="", var="",var_f4_button=""):
# 	"""点击按钮让文本变成按钮的单位"""
# 	if args == "MI":
# 		if not var_entry_label:
# 			button_1.config(bg="red")
# 			button_2.config(bg="white")
# 			button_3.config(bg="white")			
# 		else:
# 			var_entry_label.set("MI(英里)")
# 			button_1.config(bg="red")
# 			button_2.config(bg="white")
# 			button_3.config(bg="white")
# 			var_f4_button.set("MI(英里)")
# 			judg_var(var,var_entry_label,var_f4_button)




# 	elif args == "KM":
# 		if not var_entry_label:
# 			button_1.config(bg="white")
# 			button_2.config(bg="red")
# 			button_3.config(bg="white")		
# 		else:
# 			var_entry_label.set("KM(公里)")
# 			button_1.config(bg="white")
# 			button_2.config(bg="red")
# 			button_3.config(bg="white")		
# 			judg_var(var,var_entry_label,var_f4_button)
# 	elif args == "LI":
# 		if not var_entry_label:
# 			button_1.config(bg="white")
# 			button_2.config(bg="white")
# 			button_3.config(bg="red")
# 		else:
# 			var_entry_label.set("LI(里)")
# 			button_1.config(bg="white")
# 			button_2.config(bg="white")
# 			button_3.config(bg="red")
# 			judg_var(var,var_entry_label,var_f4_button)
# 	else:
# 		pass

# def judg_var(var,var_entry_label,var_f4_button):
# 	"""判断文本输入变量"""
# 	r = var.get()
# 	if r:
# 		print(r)
# 		print(var_entry_label.get())
# 		print(var_f4_button.get())
# 	else:
# 		print("no")




# def root_2(root1):	
# 	root1.geometry("0x0")  
# 	top1 = Toplevel(root1)
# 	top1.geometry("300x300")
	

# 	Button(top1, text="公里,英里,里",font=("",24,""), command=(lambda:make_lmk(top1,root1))).pack(fill=BOTH)
# 	Button(top1, text="时间,分,秒",font=("",24,"")).pack(fill=BOTH)
# 	Button(top1, text="返回",font=(("",24,"")), command=(lambda:back(top1,root1))).pack()
# 	top1.protocol("WM_DELETE_WINDOW",(lambda:back(top1,root1))) # 点叉执行函数
# 	top1.focus_set()
# 	top1.grab_set()
# 	top1.wait_window() #暂停调用直到top1被销毁


	
# root_1()


# ===========================================













# =========================================================
# 计算球体积
# from tkinter import *
# from tkinter.messagebox import showinfo

# class Make_label(Frame):

# 	def __init__(self,parent,text="",row=0,column=0):
# 		super().__init__(parent)
# 		self.row = row
# 		self.column = column
# 		self.grid(row=self.row,column=self.column)
# 		self.text = text
# 		self.fill_both(parent)

# 	def fill_both(self, parent):
# 		parent.columnconfigure(self.column, weight=1)
# 		parent.rowconfigure(self.row,weight=1)

# 	def make_label(self):
# 		l = Label(self, text=self.text)
# 		l.grid()


# class Make_entry(Frame):

# 	def __init__(self,parent,row=0,column=0):
# 		super().__init__(parent)
# 		self.row = row
# 		self.column = column
# 		self.var = IntVar()		
# 		self.grid(row=self.row,column=self.column)
# 		self.fill_both(parent)

# 	def fill_both(self, parent):
# 		parent.columnconfigure(self.column, weight=1)
# 		parent.rowconfigure(self.row,weight=1)

# 	def make_entry(self):
# 		e = Entry(self,textvariable=self.var)
# 		e.grid()



# class Make_button(Frame):

# 	def __init__(self,parent, row=0,column=0):
# 		super().__init__(parent)
# 		self.row = row
# 		self.column = column		
# 		self.grid()
# 		self.fill_both(parent)

# 	def fill_both(self, parent):
# 		parent.columnconfigure(self.column, weight=1)
# 		parent.rowconfigure(self.row,weight=1)

	
# 	def make_button1(self,text="", w_row=0, w_column=0,func=None):
# 		b = Button(self, text=text)
# 		b.config(command=self.get_var)
# 		b.grid(row=w_row,column=w_column)

# 	def make_button2(self,text="", w_row=0, w_column=0,func=None):
# 		b = Button(self, text=text)
# 		b.config(command=self.quit)
# 		b.grid(row=w_row,column=w_column)

# 	def get_var(self):
# 		r = e.var.get()
# 		r3 = get_circle_v(r)
# 		showinfo("球的体积","球的体积为:\n%d"%r3)

# import math
# def get_circle_v(r):
# 	"""球的体积公式 (4/3)πr**3"""
# 	return (4/3)*math.pi*r**3


# root = Tk()

# l = Make_label(root,"请输入球的半径", row=0)
# l.make_label()

# e = Make_entry(root, row=1)
# e.make_entry()


# b1 = Make_button(root, row=2)
# b1.make_button1("确定",2,0)
# b1.make_button2("取消",2,1)

# root.mainloop()
# =========================================================



# ==============================================
# listbox插入列表

# from tkinter import *

# class My_listbox(Listbox):
# 	# 定义列表组件类

# 	def __init__(self,parent):
# 		super().__init__(parent)
# 		self.grid()
# 		self.var = StringVar()


# 	def make_listbox(self):
# 		# 创建列表组件
# 		l = Listbox(self,listvariable=self.var)
# 		l.grid()

# 	def insert_to_listbox(self):
# 		# 像列表组件中插入数据
# 		for i in range(1,6):
# 			l.insert(END,str(i))


# root = Tk()

# l = My_listbox(root)
# l.insert_to_listbox()

# root.mainloop()
# ==============================================



# ==============================================
# 双端队列deque与tkinter

# from tkinter import *
# from collections import deque

# class My_label(Frame):

# 	def __init__(self,parent):
# 		super().__init__(parent)
# 		self.grid()
# 		self.label1 = StringVar()
# 		self.label2 = StringVar()
		
# 	def make_label1(self):
# 		l1 = Label(self,textvariable=self.label1,bg="yellow")
# 		self.label1.set("双端队列deque与tkinter")
# 		l1.grid()
	
# 	def make_label2(self):
# 		l2 = Label(self,textvariable=self.label2, bg="pink")
# 		self.label2.set("输入数值,点击下列按钮进行操作")
# 		l2.grid()


# class My_entry(Frame):

# 	def __init__(self,parent):
# 		super().__init__(parent)
# 		self.grid()
# 		self.entry_value = StringVar()

# 	def make_entry(self):
# 		e = Entry(self, textvariable=self.entry_value)
# 		e.grid()

# 	def get_var(self):
# 		print(e.entry_value.get())


# class My_button(Frame):

# 	def __init__(self,parent):
# 		super().__init__(parent)
# 		self.grid()

# 	def make_button(self,text="", func=None):
# 		b = Button(self,text=text,command=func) 
# 		b.grid()



# class My_deque(deque):

# 	def __init__(self):
# 		super().__init__()

# 	def d_append(self):
		
# 		self.append(e.entry_value.get())
# 		l.label1.set("向队列中末尾添加了元素: %s"%e.entry_value.get())
# 		l.label2.set("队列中元素现在为: %r"%d)

# 	def d_appendleft(self):
# 		self.appendleft(e.entry_value.get())
# 		l.label1.set("向队列中最前面添加了元素: %s"%e.entry_value.get())
# 		l.label2.set("队列中元素现在为: %r"%d)		

# 	def d_pop(self):
# 		self.pop()
# 		l.label1.set("删除了队列中末尾的元素")
# 		l.label2.set("队列中元素现在为: %r"%d)
# 	def d_popleft(self):
# 		self.popleft()
# 		l.label1.set("删除了队列中最前面的元素")
# 		l.label2.set("队列中元素现在为: %r"%d)


# root = Tk()

# d = My_deque() 

# l = My_label(root)
# l.make_label1()
# l.make_label2()

# e = My_entry(root)
# e.make_entry()


# b = My_button(root)
# b.make_button("append",d.d_append)
# b.make_button("appendleft",d.d_appendleft)
# b.make_button("pop", d.d_pop)
# b.make_button("popleft", d.d_popleft)

# b.make_button("退出",l.quit)


# root.mainloop()


# ==============================================