import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

for _ in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-150, 0)
t.pendown()

for _ in range(3):
    t.forward(100)
    t.left(120)

win.mainloop()