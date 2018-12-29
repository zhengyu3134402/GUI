
# ===========================================
# Tkinter  GUI编程
# ===========================================

# ===========================================
# tkinter编码基础
# 1 从tkinter模块中加载一个组件类
# 2 创建组件类的实例为标签类
# 3 在父组件中打包新标签
# 4 调用主循环,显示窗口, 同时开始tkinter的事件循环
# ===========================================


# ===========================================
# # tkinter编码基础实例
# from tkinter import *
# root = Tk()    # 父组件
# widget = Label(root, text="hello 1111") # 组件
# widget.pack()		# 几何管理器
# root.mainloop()	
# ===========================================



# ===========================================
# Tk属性
# win.geometry("像素x像素")	设置tk大小
# ===========================================



# ===========================================
# 组件分类
# BUtton		按钮
# Canvas		绘图形组件,可以在其中绘制图形
# Checkbutton	复选框
# Entry 		文本框
# Frame 		框架,将几个组件组成一组
# Label 		标签,可以现实文字或者图片
# Listbox 	列表框
# Menu 		菜单
# Menubutton	Menubutton的ginseng完全可以使用Menu替代
# Message 	与Label组件类似,但可以根据自身大小将文本换行
# Radiobutton 单选框
# Scale 		滑块
# Scrollbal 	滚动条
# Text		文本框多行
# Toplevel 	用来创建子窗口容器组件
# ===========================================



# ===========================================
# 组件布局
# pack方法的参数布局
# after		将组件置于其他组件之后
# anchor 		组件对其的方式n,s,w,e
# before 		将组件置于其他组件之前
# side 		组件在主窗口的位置,top,bottom,left,right
# column 		组件所在的列起始位置
# columnspam 	组件的列宽
# row 		组件所在行起始位置
# rowspam 	组件的行宽

# place方法参数布局
# anchor 		组件对齐的方式
# x 			组件左上角x坐标
# y 			组件左上角y坐标
# relx 		组件相对于窗口的x坐标,应为0~1之间的小数
# rely 		组件相对于窗口的y坐标,应为0~1之间的小数
# width 		组件的宽度
# height 		组件的高度
# relwidth 	组件相对于窗口的宽度,应为0~1之间的小数
# relheight	组件相对于窗口的高度,应为0~1之间的小数
# ===========================================



# ===========================================
# 按钮的参数
# anchor 		指定按钮上文本的位置
# bg 			指定按钮的背景色
# bitmap 		指定按钮上显示的位图
# bd 			指定按钮边框的宽度
# command 	指定按钮消息的回调函数
# cursor 		指定鼠标移动到按钮上的指针样式
# font 		指定按钮上文本的字体
# fg 			指定按钮的前景色
# height 		指定按钮的高度
# image 		指定按钮上现实的图片
# state 		指定按钮的状态 DISABLED禁用状态
# text 		指定按钮上现实的文本
# width 		指定按钮的宽度
# ===========================================



# ===========================================
# 文本框参数Entry和Text
# bg 					指定文本框的背景色
# bd 				 	指定文本框的宽度
# font				指定文本框的字体
# fg 					指定文本框的前景色
# selectbackground	指定选定文本框的背景色
# selectforeground	指定选定文本框的前景色
# show 	指定文本框的中现实字符,若为"*", 表示文本框为秘密框
# state 	指定文本框的状态 DISABLED禁用状态
# width 	指定文本框的宽度
# ===========================================



# ===========================================
# 标签参数Label
# anchor 		指定标签的文本位置
# bg 			指定标签的背景色
# bd 			指定标签的边框宽度
# bitmap 		指定标签中的位图
# font 		指定标签中文本的字体
# fg 			指定标签的前景色
# height 		指定标签的高度
# image 		指定标签中的图片
# justify 	指定标签中多行文本的对齐方式 LEFT,RIGHT,CENTER
# text 		指定标签的文本,可以使用"\n"表示换行
# width 		指定标签的宽度
# ===========================================



# ===========================================
# 单选框和复选框参数
# anchor 		指定文本位置
# bg 			指定背景色
# db 			指定边框的宽度
# bitmap 		指定组件中的位图
# font 		制定组件中的文本的字体
# fg 			指定组件的前景色
# height 		指定组件的高度
# image 		指定组件中的图片
# justify 	制定组件中多行文本的对齐方式
# text 		指定组件的文本,可使用"\n" 表示换行
# value 		制定组件被选中后关联变量的值
# variable 	制定组件所关联的变量
# width 		制定组件的宽度
# ===========================================





# ===========================================
# 组件尺寸调整
# from tkinter import *
# root =Tk()
# widget = Label(root, text="hei")
# widget.pack(expand=YES, fill=BOTH)
# root.mainloop()
# expand=YES 
	# 允许标签随父组件扩展,可以让组件居中并显示在扩展的空间中
# fill 可用来拉伸组件,使其充满分配的空间
	# fill = Y 垂直拉伸
	# fill = X 水平拉伸
	# fill = BOTH 两者都拉伸
# ===========================================



# ===========================================
# 添加按钮和回调函数(实现点击按钮退出功能)

# root.quit 
	#标准Tk对象方法,用于关闭GUI界面并结束程序
# from tkinter import *
# root = Tk()
# widget = Button(root)
# widget.config(text="按钮", command=root.quit)
# widget.pack()
# root.mainloop()
# ===========================================



# ===========================================
# 添加自定义的回调函数
# from tkinter import *
# def test():
# 	print("我是自定义函数!!")
# root = Tk()
# widget = Button(root)
# widget.config(text="点我触发函数", command=test)
# widget.pack()
# root.mainloop()

# ===========================================



# ===========================================
# lambda回调处理器
# from tkinter import * 
# root = Tk()
# widget = Button(root)
# widget.config(text="lambda回调处理器", command=(lambda:print("haha")))
# widget.pack()
# root.mainloop()

# ===========================================



# ===========================================
# 用lambdas表达式和对象引用来延迟调用
# 延迟的必要性在于,如果按钮创建函数中编写处理器调用,
# 而没有采用lambda或其他中间函数,回调发生在按钮创建
# 时,而不是之后按钮被按下时候

# from tkinter import *

# def test(a,b):
# 	print(a+b)

# root = Tk()
# widget = Button(root)
# widget.config(text="lambda函数的延迟调用", command=(lambda:test(1,2)))
# widget.pack()
# root.mainloop()
# ===========================================



# ===========================================
# 回调作用域的问题
# lambda的延迟调用,带来了一次额有关作用域的的争议

# 强制记住i的值,原因在于默认参数与外部作用域引用不同,
# 他在函数创建时定制而不是调用时定值.它可以记录函数创建
# 时封闭作用域内的名字的值,而不是封闭作用域内某个地方
# 最后分配的值,当函数的封闭作用域是一个模块而不是另一个函数
# 时,也是如此:

# def test1():
# 	li = []
# 	for i in "123456":
# 		li.append(lambda:i)
# 	return li
# def test2(s):
# 	for i in s:
# 		print(i())
# s = test1()
# test2(s)


# def test1():
# 	li = []
# 	for i in "123456":
# 		li.append(lambda i=i:i)
# 	return li
# def test2(s):
# 	for i in s:
# 		print(i())
# s = test1()
# test2(s)
# ===========================================



# ===========================================
# Bound方法的回调处理器(类方法) 
# 既可以记录事件发送的目标实例也可以记录
# 相关方法的调用实例

# from tkinter import *
# import sys
# class Test:
# 	def __init__(self):
# 		root = Tk()
# 		widget = Button(root)
# 		widget.config(text="类方法函数回调处理器", command=self.quit)
# 		widget.pack()

# 	def quit(self):
# 		print("退出!")
# 		sys.exit()

# Test()
# mainloop()
# ===========================================



# ===========================================
# 组件的尺寸调整:裁切
# 打包组件的顺序决定了屏幕缩小时哪些组件会被挤出屏幕
# ===========================================



# ===========================================
# 为框架添加组件
# 通过将组件依附于框架,在将框架依附于其他框架
# ===========================================



# ===========================================
# 布局:打包顺序和边的依附关系
# packer布局系统的工作原理:
# 1 packer最初开始拥有整个父组件容器的可用空间
# 2 随着组件在某条边上被打包,该组件即获得了剩余空间中
# 	要求的一条边,剩余空间缩小
# 3 经过先前的打包要求,空间缩小,后来的打包要求仅获得剩余
# 	空间中的一条边
# 4 组件都分配空间后,expand选项划分所有剩余空间,fill选项
# 	和anchor选项在组件分配的空间内拉伸调整组件
# ===========================================




# ===========================================
# 用anchor替代stretch来定位

# 默认的anchor值是CENTER
# # anchor的八个方位 N E S W ....
# from tkinter import *
# ===========================================



# ===========================================
# 用类实现组件的自定义设置

# from tkinter import *

# class Test(Button):
# 	def __init__(self, parent=None, **config):
# 		super().__init__(parent, **config)
# 		self.pack()
# 		self.config(command=self.qqq)
# 		
# 	def qqq(self):
# 		print("点击了退出按钮")
# 		self.quit()

# root = Tk()
# a = Test(root,text="hahahahaaahhahaha")
# root.mainloop()
# ===========================================




# ===========================================
# 用类复用GUI部件

# 通过将Frame子类话,类成为GUI的封闭环境
# 1 通过将对象依附于self来添加组件,self是Frame容器子类的实例(如Button)
# 2 回调处理器作为self的bound方法注册,并在类中返回代码(如self.message)
# 3 事件间的状态信息通过给self属性保留,在类中对所有回调方法可见
# 4 即便在同一过程中,这样的GUI部件可以产生多个副本,因为每个类实例都有不同
# 	的命名空间
# 5 类天然的支持自定义,即可以继承,也可以组合添加

# from tkinter import *

# class Hello(Frame):

# 	def __init__(self, parent=None,**config):
# 		super().__init__(parent,**config)
# 		self.pack()
# 		self.num = 0
# 		self.make_widgets()
		

# 	def make_widgets(self):
# 		Button(self, text="类服用GUI部件",command=self.add).pack()

# 	def add(self):
		
# 		self.num += 1
# 		print(self.num)

# if __name__ == '__main__':
# 	root = Tk()
# 	h = Hello(root)
# 	h.mainloop()
# ===========================================




# ===========================================
# 独立的容器类
# from tkinter import *

# class Hello:

# 	def __init__(self, parent=None):
# 		self.top=Frame(parent) # 嵌入框架
# 		self.top.pack()
# 		self.data=0
# 		self.make_widgets() #将组件添加到self.top

# 	def make_widgets(self):
# 		Button(self.top, text="bye", command=self.top.quit).pack(side=LEFT)
# 		Button(self.top, text='haha', command=self.message).pack(side=RIGHT)

# 	def message(self):
# 		self.data += 1
# 		print("hello", self.data)

# if __name__ == '__main__':
# 	Hello().top.mainloop()
# ===========================================




# ===========================================
# 配置组件外观

# from tkinter import *
# # padx,pady 文本长和宽
# root = Tk()
# Label(root, text="555", padx=50,pady=30).pack()
# root.mainloop()


# # 类似与hover属性 改变鼠标指针的外观
# root = Tk()
# Label(root, text="6666", padx=50,cursor="gumby").pack()
# root.mainloop()


# # 类似于border bd边框宽度,
# # relief边框类型
		# 扁平FLAT,凹陷SUNKEN,突起RAISED
		# 凹槽GROOVE,加粗SOLID脊状RIDGE
# root = Tk()
# Label(root, text="555", bd=8,  relief=RAISED).pack()
# root.mainloop()


# # bg 背景色 fg文本颜色
# root = Tk()
# Label(root, text="4444444", bg="pink", fg="red").pack()
# root.mainloop()


# # 字体系列,大小,类型
# 字体系列有 正常normal  粗体bold 罗马romam 
# 	斜体italc 下划线underline 加粗overstrike 
# 	也可以组合
# root = Tk()
# Label(root, text="hello我哈哈123",font=("normal bold",24,"")).pack()
# root.mainloop()
# ===========================================



# ===========================================
# 顶层窗口
# Toplevel组件
# 通过创建Toplevel组件对象,可以创建任意数量的独立窗口,
# 这些窗口会根据需求而生成或弹出

# from tkinter import *

# root = Tk()
# win1 = Toplevel()
# win2 = Toplevel()
# Label(win1, text="111111").pack()
# Label(win2, text="222222").pack()
# root.mainloop()
# 独立的窗口toplevel 点击叉 关闭一个自己的窗口
# 点击root窗口 关闭所有的窗口
# 因为在同一个进程之下穿件的窗口若使用sys.exit关闭
# toplevel会关闭所有窗口
# ===========================================



# ===========================================
# Toplevel组件和Tk组件
# Toplevel向Frame,分割与自身的窗口中,有其他方法允许
# 	用户处理顶层窗口属性,有父级
# Tk组件大致像Toplevel,但他用于提供应用窗口的根窗口,
# 	没有父级
# Lable标签有一个默认的父级Tk根窗口
# 创建组件在没有父级的情况下,Tk会成为组件和其他窗口的默认
# 父窗口

# # 使用destroy方法只关闭一个窗口
# Button(win1,text="aaaaa", command=win1.destroy).pack()
# Button(win2,text="bbbbb", command=win2.destroy).pack()
# win1.mainloop()

# ===========================================




# ===========================================
# destroy方法只关闭一个窗口root.quit会关闭所有窗口和程序

# from tkinter import *
# root = Tk()
# win1 = Toplevel()
# win2 = Toplevel()
# Button(win1, text="只关闭一个窗口", command=win1.destroy).pack()
# Button(win2, text="只关闭一个窗口", command=win2.destroy).pack()
# Button(win1, text="关闭所有窗口的按钮", command=win1.quit).pack()
# root.mainloop()
# ===========================================




# ===========================================
# 顶层窗口协议
# Tk和Toplevel组件都会为顶层角色而导出其他的方法和功能
# ===========================================



# ===========================================
# 创建对话框


# 消息框
# tkinter.messagebox模块中
# askokcancel
# askquestion
# askyesno
# showerror
# showinfo
# showwarning

# 消息框的控制参数
# default 	指定消息框的按钮
# icon 		指定消息框的图标
# message 	指定消息框的所显示的消息
# parent 		指定消息框的父组件
# title 		指定消息框的标题
# type 		指定消息框的类型

# from tkinter import *
# import tkinter.messagebox

# def cmd():
# 	global n 			# 使用全局变量n
# 	global buttontext 	# 使用全局便狼buttontext
# 	n = n+1
# 	if n ==1:
# 		tkinter.messagebox.askokcancel("askokcancle消息框","你喜欢黑色码?")
# 		buttontext.set("askquestion") # 更改按钮上的文字

# 	elif n ==2:
# 		tkinter.messagebox.askquestion("askquestion消息框","你喜欢红码?")
# 		buttontext.set("askyesno") # 更改按钮上的文字

# 	elif n ==3:
# 		tkinter.messagebox.askyesno("askyesno消息框","你喜欢绿码?")
# 		buttontext.set("showerror") # 更改按钮上的文字

# 	elif n ==4:
# 		tkinter.messagebox.showerror("showerror消息框","你喜欢蓝码?")
# 		buttontext.set("showinfo") # 更改按钮上的文字

# 	elif n ==5:
# 		tkinter.messagebox.showinfo("showinfo消息框","你喜欢白码?")
# 		buttontext.set("showwarning") # 更改按钮上的文字

# 	else:
# 		n = 0
# 		tkinter.messagebox.showwarning("showwarning消息框","到头了,将n变成了0")
# 		buttontext.set("askokcancel")


# n = 0
# root = Tk()
# buttontext = StringVar()		# 生成关联按钮文字的变量
# buttontext.set("askokcancel") 	# 设置buttontext值
# button = Button(root, 
# 				textvariable=buttontext, # 设置关联变量
# 				command=cmd) 	# 设置事件处理函数
# button.pack()
# root.mainloop()
# ===========================================




# ===========================================
# 使用标准对话框
# tkinter.simpledialog 模块  	# 创建标准的输入对话框
# tkinter.filedialog 模块 		# 文件打开和保存对话框
# tkinter.colorchooser 模块 	# 创建颜色选择对话框
# ===========================================




# ===========================================
# tkinter.simpledialog 模块

# tkinter.simpledialog 的三种类型对话框
# 	askstring	#输入字符串
# 	askinteger	#输入整数
# 	askfloat 	#输入浮点数

# 	相同的可选参数
# 	title 		# 制定对话框标题
# 	prompt 		# 指定对话框中显示的文字
# 	initalvalue # 制定输入框的初始值

# from tkinter import *
# import tkinter.simpledialog

# def instr():
# 	r = tkinter.simpledialog.askstring("askstring对话框",
# 				"输入字符串",
# 				initialvalue="haha")
# 	print(r)

# def inint():
# 	r = tkinter.simpledialog.askinteger("askintger对话框",
# 				"输入整数",
# 				initialvalue=123)
# 	print(r)

# def infloat():
# 	r = tkinter.simpledialog.askfloat("askfloat对话框",
# 				"输入浮点数",
# 				initialvalue=123.123)
# 	print(r)


# root = Tk()

# button1 = Button(root, text="输入字符串", command=instr)
# button2 = Button(root, text="输入整数", command=inint)
# button3 = Button(root, text="输入浮点数", command=infloat)

# button1.pack()
# button2.pack()
# button3.pack()
# root.mainloop()

# ===========================================




# ===========================================
# tkinter.filedialog 模块

# askopenfilename函数的可选参数
# diletypes 		# 指定文件类型
# initialdir 		# 制定默认目录
# initialfile 	# 制定默认文件
# title 			# 制定对话框标题


# 文件打开和保存对话框

# from tkinter import *
# import tkinter.filedialog

# def fileopen():
# 	r = tkinter.filedialog.askopenfilename(
# 		title="打开文件",
# 		filetypes=[("python","*.py *.pyw"),("all files","*")])
# 	print(r) # 返回文件的完整路径
# def filesave():
# 	r = tkinter.filedialog.asksaveasfilename(
# 		title="保存文件",
# 		filetypes=[("all file","*")],
# 		initialdir=r"/home/zhengyu/", 	# 指定初始化目录
# 		initialfile="aa.txt") 	# 指定初始化文件		
# 	print(r) # 返回文件的完整路径

# root = Tk()
# button1 = Button(root, text="打开文件",command=fileopen)
# button2 = Button(root, text="保存文件",command=filesave)
# button1.pack()
# button2.pack()
# root.mainloop()
# ===========================================




# ===========================================
# tkinter.colorchooser 模块

# askcolor函数创建表尊的颜色选择对话框
# 参数
# initialcolor # 制定初始化颜色
# title 	# 制定对话框标题


# 颜色选择对话框

# from tkinter import *
# import tkinter.colorchooser

# def choosecolor():
# 	r = tkinter.colorchooser.askcolor(
# 		title="选择颜色")
# 	print(r) # 返回元祖 ((R,G,B),"#十六进制")


# root = Tk()
# button = Button(root,text="选择颜色", command=choosecolor)
# button.pack()
# root.mainloop()
# ===========================================




# ===========================================
# 创建自定义对话框

# 使用Toplever组件创建一个简单的对话框

# from tkinter import *
# import tkinter.messagebox

# class MyDialog:
# 	def __init__(self,root):
# 		self.top = Toplevel(root)  # 生成top组件
# 		label = Label(self.top, text="请输入") # 生成标签组件
# 		label.pack()
# 		self.entry = Entry(self.top)
# 		self.entry.pack()
# 		self.entry.focus() # 文本获得焦点
# 		button = Button(self.top,text="ok", command=self.ok)
# 		button.pack()

# 	def ok(self):
# 		self.input=self.entry.get() # 获取文本框中的内容,保存为input
# 		self.top.destroy() 	# 销毁对话框

# 	def get(self):
# 		return self.input

# class MyButton:

# 	def __init__(self,root,type):
# 		self.root = root
# 		if type ==0:
# 			self.button = Button(root,text="创建",command=self.create)
# 		else:
# 			self.button = Button(root, text="退出", command=self.quit)
# 		self.button.pack()
		
# 	def create(self):
# 		d = MyDialog(self.root) # 生成对话框
# 		self.button.wait_window(d.top)	# 等待对话框结束
# 		tkinter.messagebox.showinfo("showinfo消息框", "你输入了:"+d.get())

# 	def quit(self):
# 		self.root.quit()

# root = Tk()
# MyButton(root, 0)
# MyButton(root, 1)
# root.mainloop()
# ===========================================







# ===========================================
# 弹出独立窗口,并同时获得焦点
# from tkinter import *

# def add_atoplevel():
	
# 	win = Toplevel(root)
# 	Label(win,text="增加的窗口").pack()
# 	win.focus_set() 
	
# root = Tk()
# Button(root, text="增加一个独立窗口", command=add_atoplevel).pack()
# root.mainloop()
# ===========================================



# ===========================================
# 弹出独立窗口,并禁用其他窗口
# from tkinter import *

# def add_atoplevel():
	
# 	win = Toplevel(root)
# 	Label(win,text="增加的窗口").pack()
# 	win.focus_set() 
# 	win.grab_set()
# 	win.wait_window() # 暂停掉调用直到,win组件被销毁
	
# root = Tk()
# Button(root, text="增加一个独立窗口", command=add_atoplevel).pack()
# root.mainloop()
# ===========================================




# ===========================================
# 其他模态化方法

# from tkinter import *

# def test():

# 	# win = Toplevel()
# 	# Label(win, text="label").pack()
# 	# Button(win, text="win.quit", command=win.quit).pack()
# 	# win.mainloop() # 出现几个窗口就得点击几次退出才能退出

# 	win = Toplevel()
# 	Label(win, text="label").pack()
# 	Button(win, text="win.quit", command=win.quit).pack()
# 	win.protocol("WM_DELETE_WINDOW", win.quit)
# 	win.focus_set()
# 	win.grab_set()
# 	win.mainloop()
# 	win.destroy()

# root = Tk()
# Button(root, text="创建一个窗口", command=test).pack()
# root.mainloop()
# ===========================================



# ===========================================
# 事件

# 事件绑定方法
# bind(sequence,func,add)
# bind_class(className,sequence,func,add) # 类绑定
# bind_all(sequence,func,add) # 将所有组件事件绑定到事件响应函数上
# 参数
# sequence 	# 绑定的事件
# func 		# 所绑定事件处理函数
# add 		# 可选参数
# className  	# 所绑定的类

# # 鼠标事件参数
# <Button-1>  		# 鼠标左键按下,<Button-2>表示中键,<button-3>表示右键
# <ButtonPress-1>		# 表示按下鼠标左键
# <ButtonRelease-1> 	# 鼠标左键释放
# <B1-Motion-1> 		# 按住鼠标左键移动
# <Double-Button-1>   # 双击鼠标左键
# <Enter> 			# 鼠标指针进入某一组件区域
# <Leave> 			# 鼠标指针离开某一组件区域
# <MouseWheel> 		# 鼠标滚轮动作

# 键盘事件 (注意区分大小写)
# <keyPrees-A> 		# 表示按下A键,可用其他字母键代替
# <Alt-keyPrees-A> 	# 表示同时按下Alt和A键
# <Control-keyPrees-A># 表示同时按下Control和A键
# <Shift-keyPrees-A>	# 表示同时按下Shift和A键
# <Double-keyPrees-A> # 表示快速按两下A键
# <Lock-keyPrees-A> 	# 表示Caps Lock打开后按下A键

# 窗口事件
# Activate 	# 当组件由不可用转为可用时触发
# Configure 	# 当组件大小改变时触发
# Deactivate  # 当组件由可用转为不可用时触发
# Destroy 	# 当组件被销毁时触发
# Expose 		# 当组件从被遮挡状态中暴露出来时触发
# FocusOut 	# 当组件获得焦点时触发
# Map 		# 当组件有隐藏状态变为显示状态时触发
# Property 	# 当窗体的属性被删除或改变时触发
# Unmap 		# 当组件由显示状态变为隐藏状态时触发
# Visibility 	# 当组件变为可视状态时触发


# 响应事件
# 窗体事件被绑定到函数后,当该时间被触发后将调用绑定的函数进行
# 处理.事件触发后系统将向改函数传递一个event对象的参数
# event对象的属性
# char 			按键字符,仅对键盘事件有效
# keycode			按键名,仅对键盘事件有效
# keysym			按键编码,仅对键盘事件有效
# num 			鼠标按键,仅对鼠标事件有效
# type 			所触发的事件类型
# widget 			引起事件的组件
# width,height 	组件改变后的大小,仅对Configure有效
# x,y 			鼠标当前位置,相对于窗口
# x_root,y_root 	鼠标当前位置,相对于整个屏幕
# ===========================================




# ===========================================
# Entry组件(
# 简单但行的文本输入框
# 更大的显示区域键入数值
# 高级功能 滚动,用于编辑关键字帮顶 及文本选择)


# 在输入框最开始位置插入文本
# from tkinter import *
# root = Tk()
# ent = Entry(root)
# ent.insert(0,"jajajaj") 
# ent.pack()
# root.mainloop()


# 在输入框尾部位置插入文本
# from tkinter import *
# root = Tk()
# ent = Entry(root)
# ent.insert(END, "ffffff")
# ent.pack()
# root.mainloop()



# x.delete(0,END) # 把原有文本内容全部删除
# 获取文本输入内容,并在获取文本的头部及尾部添加"xx"
# 点击按钮 终端现实文本 输入回车终端显示文本
# from tkinter import *

# def test():
	
# 	r = ent.get()
# 	ent.insert(0,"xx")   
# 	ent.insert(END,"xx")
# 	print(r)

# root = Tk()
# ent = Entry(root)

# ent.pack()
# ent.focus()
# # Return时间地城的回调得到一个参数,使用lambda封装器忽视它
# ent.bind("<Return>", (lambda event:test())) # 会默认向函数中传入event事件参数
# b = Button(root, text="提交", command=test)
# b.pack()
# root.mainloop()
# ===========================================




# ===========================================
# tkinter "变量"和表单布局可选方案
# 改变相关变量可以改变Entry中显示的文本,而改变Entry中
# 的文本会改变变量的值,绑定组件上的变量是变量类的实例
# StringVar, IntVar, DoubleVar,BooleanVar
# 变量类的实例能能够在模态对话框取消之后很长时间内,从
# 中获取输入的值
# from tkinter import *

# root = Tk()
# ent = Entry(root)
# ent.pack()
# # var = StringVar()
# var1 = IntVar()
# ent.config(textvariable=var1)
# var1.set("22222")
# r = var1.get()
# print(r)
# print(type(r))
# root.mainloop()


# from tkinter import *

# def test():
# 	print(var.get())
# root = Tk()
# ent = Entry(root)
# var = StringVar()
# ent.config(textvariable=var)
# ent.bind("<Return>", (lambda event:test()))
# ent.pack()
# root.mainloop()
# ===========================================



# ===========================================
# 对于单选框和复选框, vaiable是比较关键的参数.
# 有variable制定的变量应使用IntVar或StringVar生成
# 生成变量后,可以使用set方法设置变量的初始值.如果该初始
# 值与组件value所指定的值相等,则该组件处于被选中状态,
# 如果其他组件被选中,则变量值将被改为该组件value锁制定的值

# 单选框
# from tkinter import *

# root = Tk()
# r = StringVar() # 使用StringVar生成字符串变量用于单选框组件
# r.set("1") 	#初始化变量值
# radio = Radiobutton(root, 
# 		variable=r, 		# 设置单选框关联的变量
# 		value = "1", 	# 设置选中单选框时所关联的变量值,即r的值
# 		text="a1") 		
# radio.pack()
# radio = Radiobutton(root, 
# 		variable=r, 		# 设置单选框关联的变量
# 		value = "2", 	# 设置选中单选框时所关联的变量值,即r的值
# 		text="a2") 		
# radio.pack()
# radio = Radiobutton(root, 
# 		variable=r, 		# 设置单选框关联的变量
# 		value = "3", 	# 设置选中单选框时所关联的变量值,即r的值
# 		text="a3") 		
# radio.pack()
# root.mainloop()
# print(r.get())




# 复选框

# from tkinter import *

# root = Tk()
# c = IntVar()
# c.set(1)
# check = Checkbutton(root,
# 		text="c1",		
# 		variable=c, 	# 设置复选框关联的变量
# 		onvalue=1, 		# 选中复选框时,c值为1
# 		offvalue=2) 	# 未选中复选框时, c值为2
# check.pack()
# root.mainloop()
# print(c.get())
# ===========================================



# ===========================================
# 创建按钮形式的单选框和复选框

# from tkinter import *

# root = Tk()
# r = StringVar()
# r.set("1")
# radio = Radiobutton(root, 
# 		variable=r, 		
# 		value = "1", 	
# 		indicatoron=0, 	# 将单选框绘制成按钮形式
# 		text="a1") 		
# radio.pack()
# radio = Radiobutton(root, 
# 		variable=r, 		
# 		value = "2", 
# 		indicatoron=0,	
# 		text="a2") 		
# radio.pack()
# radio = Radiobutton(root, 
# 		variable=r, 		
# 		value = "3", 	
# 		text="a3") 		
# radio.pack()
# root.mainloop()

# ===========================================



# ===========================================
# 标尺(滚动条)
# command 默认传入 标尺位置值
# length 滚动条大小,间接调整了滚动精细程度
# orient 设置横轴纵轴,默认纵轴 orient="horizontal" 为横轴
# tickintervar 设置了标尺旁边一般间距的标记单位数量
# 设置了拖动一次或打击一次时候标尺跳跃的值
# showvalue 用于现实因此标尺的滑动条旁边的当前值,默认显示showvalue=YES

# from tkinter import *

# def test_x(position):
# 	print("x", position)
# def text_y(position):
# 	print("y", position)
# root = Tk()
# sc1 = Scale(root, label="x", command=test_x, length=200, tickinterval=1,showvalue=NO)
# sc1.pack()
# sc2 = Scale(root, label="y", command=text_y, orient="horizontal", resolution=10)
# sc2.pack()
# root.mainloop()
# ===========================================



# ===========================================
# 图像
# from tkinter import *
# root = Tk()
# img = PhotoImage(file="osi.png")
# Button(root,image=img).pack()
# root.mainloop()
# ===========================================






# ===========================================
# Canvas(通用绘制图形界面)

# 参数
# bg 		指定绘制图组件的背景色
# db 		指定绘制图组件的边框宽度
# bitmap 	指定绘制图组件的位图
# fg 		指定绘制图组件的前景色
# height 	指定绘制图组件的高度
# image 	指定绘制图组件的图片
# width 	指定绘制图组件的宽度


# Canvas绘图组件的绘图方法
# create_arc 		绘制圆弧
# create_bitmap 	绘制位图,支持XBM
# create_image 	绘制图片,支持GIF
# create_line 	绘制直线
# create_oval 	绘制椭圆
# create_polygon 	绘制多边形
# create_rectangle绘制矩形
# create_text 	绘制文字
# create_window 	绘制窗口
# delete 			删除绘制的图形


# from tkinter import *
# root = Tk()
# canvas = Canvas(root,
# 		width=600, 		# 指定组件宽度
# 		height=480, 	# 指定组件高度
# 		bg="white")
# im = PhotoImage(file="osi.png") # 使用Phontimage打开图片
# canvas.create_image(300,50,image=im) # 使用create_image将图片添加到Canvas组件

# canvas.create_text(302,77, 		# 使用create_text方法绘制文字
# 					text="hahahah", # 绘制文字的内容
# 					fill="gray") 	# 绘制文字的颜色

# canvas.create_polygon(290,114,316,114,330,130,
# 		310,146,284,146,270,130) # 绘制六边形

# canvas.create_oval(280,120,320,140,fill="red") # 绘制椭圆

# canvas.create_line(250,130,230,130) # 绘制直线
# canvas.create_rectangle(90,190,510,410,width=5) #绘制一个矩形,矩形线宽5像素

# canvas.create_arc(100,200,500,400, # 绘制圆弧
# 			start=0, extent=240, # 设置圆弧的起止角度
# 			fill="pink") 		# 设置圆弧填充色

# canvas.pack()
# root.mainloop()
# ===========================================




# ===========================================
# 顶层窗口菜单
# 1 创建顶层Menu作为窗口的子组件 ,并将窗口menu属性设置为心的Menu
# 2 对每个下拉对象,创建一个新 的Menu作为顶层Menu的子组件
# 	并在add_cascade方法中将新的Menu设置为顶层Menu的下拉显示对象
# 3 为步骤2中创建的每个下拉Menu添加菜单选项,使用add_command方法
# 	的command选项来记录选择回调处理器
# 4 通过创建新的Menu作为子菜单,以及使用add_cascade方法连接相应父
# 	菜单和子菜单的方法,添加下拉子菜单

# f.add_separator() # 菜单中相关条目的分割线
# tearoff = False # 下拉菜单中消除顶部的虚线
# underline =0 为菜单中的条目设置一个唯一字母作为键盘上对应的快捷键

# from tkinter import *

# root = Tk() 					
# menu = Menu(root) 				#生成菜单
# submenu = Menu(menu, tearoff=0) #生成下拉菜单
# submenu.add_command(label="aa") #向下拉菜单添加项
# submenu.add_command(label="bb") #向下拉菜单添加项
# menu.add_cascade(label="1111", menu=submenu)
# 								# 将下拉惨淡添加到菜单中
# submenu = Menu(menu, tearoff=0) #生成下拉菜单
# submenu.add_command(label="cc") #向下拉菜单添加项
# submenu.add_command(label="dd") #向下拉菜单添加项
# menu.add_cascade(label="2222", menu=submenu)

# root.config(menu=menu)   
# root.mainloop()
# ===========================================



# ==========================================
# 点击鼠标右键显示菜单

# from tkinter import *

# def test(event):
# 	print(event.x, event.y)
# 	menu.post(event.x_root, event.y_root) #显示菜单

# root = Tk()
# menu = Menu(root)
# menu.add_command(label="aa")
# menu.add_command(label="bb")

# root.bind("<Button-3>", test)
# root.mainloop()

# ==========================================



# ===========================================
# 使用Menubutton
# from tkinter import *

# root = Tk()
# mbutton = Menubutton(root, text="Food")
# top = Menu(mbutton)
# mbutton.config(menu=top)
# top.add_command(label="aa")
# top.add_command(label="bb")
# mbutton.pack()
# root.mainloop()
# ===========================================



# ===========================================
# 使用Optionmenu
# from tkinter import *
# root = Tk()
# var1 = StringVar()
# opt1 = OptionMenu(root,var1,"aaa","bbb")
# opt2 = OptionMenu(root,"ccc","ddd")
# opt1.pack(fill=X)
# opt2.pack(fill=X)
# var1.set("spam")
# root.mainloop()
# ===========================================



# ===========================================
# 列表框代码和滚动条代码
# 列表中各个条目索引从0开始
# li.config(selectmode=模式)
	# 模式分为4中, 前两个单选,后两个多选
		# SINGLE
		# BROWSE(默认)
		# MULTIPLE
		# EXTENDED
# li.yview 是一个内置的列表框方法,可以按比例调节列表
	# 框的显示,调节大小取决于回调处理器接收到的参数
# 垂直移动列表会启动回调处理器,yscrollcommand选项
	# 会有记录, sbar.set内置方法,可以按比例調解滚动条
# 注意填充滚动条 即使窗口在小也让滚动条存在 

# from tkinter import *

# def test(event):
# 	index = li.curselection() # 双击选中的索引
# 	label = li.get(index)	# 选中的内容
# 	print("你选择了%s"%label)

# s = (("我是%s"%i) for i in range(20))
# root = Tk()
# sbar = Scrollbar(root)
# li = Listbox(root)
# sbar.config(command=li.yview)
# li.config(yscrollcommand=sbar.set)
# sbar.pack(side=RIGHT, fill=Y)
# li.pack(side=LEFT,fill=BOTH,expand=YES)
# pos = 0
# for i in s:
# 	li.insert(pos, i)
# 	pos+=1
# li.bind("<Double-1>", test)
# root.mainloop()
# ===========================================



# ===========================================
# AF_INIT IP地址协议
# SOCK_STREAM TCP传输协议
# ===========================================



# ===========================================
# 线程服务器

# 当线程运行函数返回时候,线程会默默的推出,不同于进程的
# fork类型

# import time
# from socket import *
# from threading import Thread

# s = socket(AF_INET, SOCK_STREAM)
# s.bind(("192.168.1.105", 10002))
# s.listen(5)

# def now():
# 	return time.ctime(time.time())

# def handle_client(conn):
# 	time.sleep(5)
# 	while True:
# 		data = conn.recv(1024)
# 		if not data:
# 			break
# 		s_msg = "%s =>%s"%(data.decode("utf-8"),now())
# 		conn.send(s_msg.encode("utf-8"))
# def dispatcher():
# 	while True:
# 		conn,addr = s.accept()
# 		print("客户%s链接"%addr[0],end="")
# 		print("在",now())
# 		Thread(target=handle_client,args=(conn,)).start()

# dispatcher()
# ===========================================




# ===========================================



# ===========================================
# 多路复用选择服务器

# 基于select的响应服务器
# import sys,time
# from select import select
# from socket import *

# def now():
# 	return time.ctime(time.time())

# mainsocks, readsocks, writesocks = [],[],[]
# s = socket(AF_INET, SOCK_STREAM)
# s.bind(("192.168.1.105", 10001))
# s.listen(5)
# mainsocks.append(s)
# readsocks.append(s)

# while True:
# 	readables,writeables,exceptions = select(readsocks, writesocks, [])
# 	for i in readables:
# 		if i in mainsocks:
# 			newsock, address = i.accept()
# 			print("链接", address, id(newsock))
# 			readsocks.append(newsock)
# 		else:
# 			data = i.recv(1024)
# 			print("收到",data)
# 			if not data:
# 				i.close()
# 				readsocks.remove(i)
# 			else:
# 				reply = "%s at %s"%(data.decode("utf-8"), now())
# 				i.send(reply.encode())	
# ===========================================



# ===========================================
# 获取窗口在屏幕的位置(winfo_x(),winfo_y())
# from tkinter import * 
# root = Tk()
# root_x = root.winfo_x()
# root_y = root.winfo_y()
# print(root_x, root_y)
# root.mainloop()
# ===========================================




# ===========================================
# 获取屏幕宽和高
# from tkinter import *
# root = Tk()
# sw = root.winfo_screenwidth()
# sh = root.winfo_screenheight()
# print(sw,sh)
# root.mainloop()
# ===========================================




# ===========================================
# 改变窗口在屏幕中的位置
# from tkinter import *

# def change_tk_posi():
# 	root.geometry("+100+50")

# root = Tk()
# root.geometry("100x100")
# Button(root,text="改变窗口位置",command=change_tk_posi).pack()
# root.mainloop()
# ===========================================



# ===========================================
# 设置窗体在屏幕中间
# 原理 (用屏幕宽度-窗口宽度)/2 = 窗口居中左边的宽度
# 	(用屏幕高度-窗口高度度)/2 = 窗口居中上边的高度

# from tkinter import *

# root = Tk()
# sw = root.winfo_screenwidth()
# sh = root.winfo_screenheight()

# root_x = (sw-300)/2
# root_y = (sh-300)/2
# root.geometry("%dx%d+%d+%d"%(300,300,root_x,root_y))
# root.mainloop()
# ===========================================



# ===========================================
# 是窗口变成透明
# from tkinter import *
# def test():
# 	root.attributes("-alpha","0.0")
# root = Tk()
# Button(root, text="使窗口透明", command=test).pack()
# root.mainloop()

# ===========================================



# ===========================================
# 使主窗口变最小,但还是有一点点占用空间
# from tkinter import *
# def test():
# 	root.geometry("0x0")
# root = Tk()
# Button(root, text="使窗口变最小", command=test).pack()
# root.mainloop()

# ===========================================



# ===========================================
# 点叉不会不会关闭窗口

# from tkinter import *

# root = Tk()
# win1 = Toplevel(root)
# win2 = Toplevel(root)

# Button(win1, text="11111").pack()
# Button(win2, text="22222").pack()
# win1.protocol("WM_DELETE_WINDOW", lambda:None)
# root.mainloop()
# ===========================================



# ===========================================
# 点击叉触发事件
# from tkinter import *

# root = Tk()
# win1 = Toplevel(root)

# def test():
# 	win1.destroy()
# 	print("haha")

# Button(win1, text="11111").pack()

# win1.protocol("WM_DELETE_WINDOW", test)
# root.mainloop()
# ===========================================



# ===========================================
# 弹出独立窗口,并禁用其他窗口
# from tkinter import *

# def add_atoplevel():
	
# 	win = Toplevel(root)
# 	Label(win,text="增加的窗口").pack()
# 	win.focus_set() #
# 	win.grab_set()
# 	win.wait_window() # 暂停掉调用直到,win组件被销毁
	
# root = Tk()
# Button(root, text="增加一个独立窗口", command=add_atoplevel).pack()
# root.mainloop()
# ===========================================



# ===========================================
# 组件成行排列
# from tkinter import *
# root = Tk()
# f = Frame(root)
# f.pack(fill=BOTH)
# f.config(bg="pink")
# Button(f,text="aaaa").grid(row=1, column=1)
# Button(f,text="bbbb").grid(row=1, column=2)
# Button(f,text="cccc").grid(row=1, column=3)
# root.mainloop()
# ===========================================



# ===========================================
# 网格布局grid() 填充

# from tkinter import *

# root = Tk()

# f0 = Frame(root,bg="red")
# root.columnconfigure(0,weight=1) # 横列居中
# # 参数  数字是 哪行哪列,wight是权重
# root.rowconfigure(0,weight=1) # 竖列居中
# Label(f0, text="11111").grid(row=0)
# f1 = Frame(root,bg="yellow")
# Entry(f1).grid(row=1)
# f2 = Frame(root,bg="blue")
# Button(f2, text="3333").grid(row=2,column=0)
# Button(f2, text="3333").grid(row=2,column=1)
# Button(f2, text="3333").grid(row=2,column=2)
# f3 = Frame(root,bg="green")
# Label(f3, text="4444").grid()
# f4 = Frame(root,bg="red")
# Button(f4, text="5").grid(row=4,column=0)
# Button(f4, text="5").grid(row=4,column=1)
# Button(f4, text="5").grid(row=4,column=2)
# f5 = Frame(root,bg="yellow")
# Button(f4, text="6").grid(row=5,column=0)
# Button(f4, text="6").grid(row=5,column=1)
# Button(f4, text="6").grid(row=5,column=2)

# f0.grid(row=0)
# f1.grid(row=1)
# f2.grid(row=2)
# f3.grid(row=3)
# f4.grid(row=4)
# f5.grid(row=5)

# root.mainloop()
# ===========================================