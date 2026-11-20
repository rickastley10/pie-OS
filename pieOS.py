import turtle as t
import os
apps=["terminal", "settings", "other", "demo"]
commands=["0 start cmd", "0 start cmd", "0 start cmd", "0 start cmd"]
colours=["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
currentstring=""
t.tracer(0, 0)
t.pencolor("Green")
t.penup()
t.hideturtle()
def draw_rect(x, y, w, h, colour, colour2, text, font_size):
    t.penup()
    t.pencolor(colour)
    t.fillcolor(colour)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.goto(x+w, y)
    t.goto(x+w, y-h)
    t.goto(x, y-h)
    t.goto(x, y)
    t.end_fill()
    t.penup()
    t.goto(x+2, y-h)
    t.pencolor(colour2)
    t.write(text, font=("Arial", font_size, "normal"))

def click(x, y):
    for i in range(len(apps)):
        if(x > -200+(i%8)*50 and x < -200+(i%8)*50+40 and y < (200-(i//8)*50) and y > (200-(i//8)*50)-40):
            currentstring=commands[i]
            if currentstring[0] == "0":
                currentstring=currentstring[2:]
                os.system(currentstring)
            elif currentstring[0] == "1":
                currentstring=currentstring[2:]
                exec(open(currentstring,"r").read())
def mainloop():
    t.clear()
    for i in range(len(apps)):
        draw_rect(-200+(i%8)*50, (200-(i//8)*50), 40, 40, colours[i%7], "Black", apps[i], 8)
        
    t.update()
    t.ontimer(mainloop, 10)
t.onscreenclick(click)
mainloop()
t.mainloop()
