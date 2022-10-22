import tkinter

window=tkinter.Tk()
def copytext():
  str1=t1.get(1.0, "end-1c")
  t1.delete(1.0,"end-1c")
  t2.insert(1.0,str1)

  
t1=tkinter.Text(window,font = ("Times New Roman",10),bg="orange",fg="red",height=10,width=30)

t1.pack()

b1=tkinter.Button(window,text="Copy text",command=copytext)
b1.pack()
t2=tkinter.Text(window,font =("arial",10),bg="pink",fg="brown",height=10,width=30)

t2.pack()


window.mainloop()


