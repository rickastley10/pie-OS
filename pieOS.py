import turtle as t
import os
import subprocess as sub

apps=["cmd", "sh"]
commands=["0 cmd", "0 sh"]
currentstring=""


files = os.listdir(os.path.dirname(os.path.abspath(__file__)))
for i in files:
    if ".py" in i:
        currentstring=i[0:-3]

        apps.append(currentstring)

        currentstring="1 "+i
        commands.append(currentstring)

    if ".gif" in i:
        currentstring=i[0:-4]

        apps.append(currentstring)
        
        currentstring="2 "+i
        commands.append(currentstring)


colours=["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

t.tracer(0, 0)
t.pencolor("Green")
t.penup()
t.hideturtle()
t.setup(450, 450)
t.bgcolor("Black")
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
                sub.Popen(currentstring)
            elif currentstring[0] == "1":
                currentstring=currentstring[2:]
                sub.Popen("py "+currentstring)
            elif currentstring[0] == "2":
                currentstring=currentstring[2:]
                t.bgpic(currentstring)

def mainloop():
    t.clear()

    for i in range(len(apps)):
        draw_rect(-200+(i%8)*50, (200-(i//8)*50), 40, 40, colours[i%7], "Black", apps[i], 8)
        
    t.update()
    t.ontimer(mainloop, 10)

t.onscreenclick(click)
mainloop()
t.mainloop()
