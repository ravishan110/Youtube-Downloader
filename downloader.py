import Tkinter
from Tkinter import *
import pafy

def down(i,streams):
	streams[i].download()

def func():
	url=var.get()
	video = pafy.new(url)
	Label(frame2,text="").grid(row=1,column=0)
	Label(frame2,text=video.title).grid(row=2,column=0)
	Label(frame2,text=video.duration).grid(row=3,column=0)
	streams=video.streams
	i=0

	for s in streams:
		Label(frame3,text=s.resolution,width=10).grid(row=5+i,column=0)
		Label(frame3,text=s.extension,width=5).grid(row=5+i,column=1)
		size=s.get_filesize()
		size=size/1024
		size=size/1024
		Label(frame3,text=size,width=10).grid(row=5+i,column=2)
		#Label(frame3,text=s.url,width=20).grid(row=5+i,column=3)
		Button(frame3,text="Download",command=lambda i=i :down(i,streams)).grid(row=5+i,column=3)
		i+=1

root =Tk()
root.geometry("500x500+0+200")
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()
frame3=Frame(root)
frame3.pack()
label=Label(frame1,text="Enter url : ",width=15)
label.grid(row=0,column=0)
var = StringVar()
entry=Entry(frame1,width=50,textvariable=var,borderwidth=5)
entry.grid(row=0,column=1)
button=Button(frame1,text="submit",bg="green",fg="red",command=func)
button.grid(row=0,column=2)
root.mainloop()