import tkinter
root = tkinter.Tk()
root.title("キャンバスにt図形を描く")
cvs= tkinter.Canvas(width=720,height=400,bg="Green")
cvs.create_line(20,40,120,360,fill = "red",width=8)#ここが変わる
cvs.create_rectangle(160,60,260,340,fill="orange",width=0)
cvs.create_oval(300,100,500,300,outline="yellow",width=12)
cvs.create_polygon(600,100,500,300,700,300,fill="black",outline="lime",width= 16)
cvs.pack()
root.mainloop()