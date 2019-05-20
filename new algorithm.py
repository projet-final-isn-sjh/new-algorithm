import tkinter as tk

def move():
    global counter
    destroy=canvas.find_overlapping(40,0,40,397) #return id of shapes which are on the line (d):x=40 
    if destroy:
        trace((0,0,0),destroy,'')
    canvas.move("map",-40,0)
    available=canvas.find_overlapping(0,0,0,0)
    instruction=texture[counter]
    trace(instruction,available[0],bool(instruction[0])*"map") # if the type of the shape is 0 it returns an empty string, else it returns "map"
    counter+=1
    if lenght-counter:
        root.after(100,move)
    

def trace(shape_properties,n,tag):
    shape,x,y=shape_properties
    points=shapes[shape]
    m=(len(points))//2
    x=[points[2*i]+x for i in range(m)]
    y=[points[2*i+1]+y for i in range(m)]
    points=tuple()
    for i in range(m):
        points+=(x[i],y[i])
    canvas.coords(n,points)
    canvas.itemconfig(n,tag=tag)



root=tk.Tk()
canvas=tk.Canvas(root,width=800,height=450,bg="blue")
canvas.pack()
#maximum number of shapes
n=9
#dictionnary of points for differents shapes
shapes=[(0,0,1,0,1,1,0,1),
        (0,0,40,0,40,40,0,40)]
#create objects which can take all shapes(polygon)
for i in range(n):
    canvas.create_polygon(shapes[0],fill="purple",outline="white",width=2)
#ground
canvas.create_rectangle(0,400,800,450,fill="grey",outline="white",width=3)
#very simple map
texture=[(1,760,250),(1,760,300),(1,760,200),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]*10
lenght=len(texture) #lenght of the map
counter=0 
#detect point
move() #call of the function move
root.mainloop()


