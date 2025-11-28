import turtle

def lsystem(axiom, pen_turtle, distance, angle, iterations):
    string = axiom
   
    for _ in range(iterations):
        new_string = ''
        for letter in string:
            if letter == 'F':
                new_string += 'F-F++F-F'
            else:
                new_string += letter
        string = new_string
       
    print(string)
   
    for letter in string:
       
        if letter == 'F':
            pen_turtle.forward(distance)
            pen.pencolor('blue')
        if letter == '+':
            pen_turtle.right(angle)
            pen.pencolor('red')
        if letter == '-':
            pen_turtle.left(angle)
            pen.pencolor('black')

screen = turtle.Screen()
screen.setup(1920,1080)
screen.tracer(2)
screen.bgcolor('pink')

pen = turtle.Turtle()
pen.speed(0)


pen.penup()
pen.goto(-100, 200)
pen.pendown()
   
lsystem('F', pen, 1, 60, 7)
screen.mainloop()