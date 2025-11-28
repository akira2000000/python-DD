import turtle

def lsystem(axiom, pen_turtle, distance, angle, iterations):
    
    rules={
        "F": "F[+F]F[-F]F"
    }
    string = axiom
   
    for _ in range(iterations):

        new_string = ''
        for letter in string:
            new_string += rules.get(letter,letter)
        string = new_string
       
    print(string)
    
    stack = []
    for letter in string:
       
        if letter == 'F':
            pen_turtle.forward(distance)
        elif letter == '+':
            pen_turtle.right(angle)
        elif letter == '-':
            pen_turtle.left(angle)
        elif letter == '[':
            position=pen_turtle.position()
            heading = pen_turtle.heading()
            stack.append((position, heading))
        elif letter == ']':
            position, heading = stack.pop()
            pen_turtle.penup()
            pen_turtle.goto(position)
            pen_turtle.setheading(heading)
            pen_turtle.pendown()


screen = turtle.Screen()
screen.setup(1920,1080)
screen.tracer(100)
screen.bgcolor('pink')

pen = turtle.Turtle()
pen.speed(0)


pen.penup()
pen.goto(0, -500)
pen.pendown()
pen.left(90)
   
lsystem('F', pen, 1, 35, 6)
screen.mainloop()