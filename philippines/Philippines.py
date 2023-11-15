#Subscribe to CodeGrah
from turtle import *
#red side
fillcolor('#CE1126')
begin_fill()
forward(400)
right(90)
forward(200)
right(90)
forward(800)
right(150)
forward(400)
right(30)
forward(55)
end_fill()
#blue side
fillcolor('#0038A8')
begin_fill()
forward(399)
left(90)
forward(200)
left(90)
forward(800)
left(150)
forward(400)
left(30)
forward(55)
end_fill()
back(57)

#white side
fillcolor("white")
begin_fill()
right(150)
forward(398)
right(120)
forward(400)
right(120)
forward(400)
end_fill()

left(25)

#star function
def stars(a):
 fillcolor('#FCD116')
 begin_fill()
 forward(a)
 right(140)
 forward(a)
 left(65.5)
 forward(a)
 right(140)
 forward(a)
 left(70)
 forward(a)
 right(141.5)
 forward(a)
 left(67)
 forward(a)
 right(141)
 forward(a)
 left(72.5)
 forward(a)
 right(142)
 forward(a)
 end_fill()
pencolor('#FCD116')
penup()
back(60)
pendown()
#calling star function
stars(15)

left(45)
penup()
back(280)
pendown()
#calling star function
stars(15)

left(9)
penup()
forward(280)
pendown()
#calling star function
stars(15)

penup()
left(40)
back(150)

#Adding Philippines sun
screen = Screen()
screen.addshape("p.gif")   
shape("p.gif")

done()