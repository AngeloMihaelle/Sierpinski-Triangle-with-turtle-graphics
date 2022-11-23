import turtle
from math import sqrt
import random
import tkinter

def drawTriangle(leng:list, color:list,start:tuple, veronica:turtle,recLvl:int):
    '''
    Draw a triangle
    :param int leng: Length of the triangle sides
    :param list color: A list that contains posible colors for a triangle
    :param tuple start: A tuple with the start cords for a triangle
    :param turtle.Turtle() veronica: veronica (turtle's name)
    :type recLvl: level of recursion (The depth)
    :return: void
    '''
    veronica.penup()
    veronica.goto(start)
    veronica.pencolor(random.choice(color)) # Random color  for the triangle
    angle = 0
    if recLvl > 0:
        veronica.pendown()
        for _ in range(3):

            veronica.forward(leng)
            angle += 120
            veronica.setheading(angle)
        turtle.Screen().update()
        #It call itself 3 times making the 3 inner triangles. 
        drawTriangle(leng/2, color,start, veronica,recLvl-1)
        drawTriangle(leng/2, color,(start[0]+leng/2 ,start[1]), veronica, recLvl-1)
        drawTriangle(leng/2, color,(start[0]+leng/4 ,start[1]+(sqrt((leng**2/4)-(leng**2/16)))), veronica, recLvl-1)
   
        
def main():
    # Set up the graphics parameters and the turtle.
    recLvl = int(input("Enter the recursion level: "))
    color = int(input("Enter the color mode (1 for rainbow, 2 for black): "))
    animation = int(input("Enter the animation mode (1 for animation, 2 for no animation): "))
    res = int(input("Enter the resolution (n * n it is a square so just one integer)): "))
    speed = int(input("Enter the speed (1 - 10 where 10 is fast or 0 for the fastest movement ): "))
    drawing_area = turtle.Screen()
    drawing_area.setup(width=res, height=res)
    drawing_area.title("Sierpinski Triangle")
    if(color == 1): drawing_area.bgcolor("black")
    if(animation == 2): turtle.Screen().tracer(0,0)
    try:
        img = tkinter.Image("photo", file="sierpinski.png")
        turtle._Screen._root.iconphoto(True, img)
    except:
        print("no \"sierpinski.png\" image found for icon")
    veronica = turtle.Turtle() # My turtle's name is Veronica 🐢
   
    
    color = ["black"] if color == 2 else ["red","blue","green","yellow","orange","purple","cyan","white"]
    
    veronica.speed(speed)
    leng  = res - 100 
    vlen = (res - sqrt((leng**2)-(leng**2/2)))/4 # Desperate try to center the 1th triangle
    start = (-1*leng/2,-1*leng/2 + vlen)
    drawTriangle(leng, color, start, veronica,recLvl)
    veronica.hideturtle()
    turtle.Screen().update()
    turtle.done()
    drawing_area.exitonclick()                                                                                                              
    
    
if __name__ == '__main__':
    main()

