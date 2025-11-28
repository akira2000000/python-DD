import turtle
import numpy as np

states = ['A', 'B', 'C']

conections = [
    ['AA','AB','AC'],
    ['BA','BB','BC'],
    ['CA','CB','CC']
]

probabilites =[
    [0.33,0.33,0.34],
    [0.33,0.34,0.33],
    [0.34,0.33,0.33]
]

def markov (iterations):
    current = 'A'
    secuencia = [current]
    i = 0
    while i < iterations:
        if current == 'A':
            change = np.random.choice(conections[0], p = probabilites[0])
        elif current == 'B':
            change = np.random.choice(conections[1], p = probabilites[1])
        elif current == 'C':
            change = np.random.choice(conections[2], p = probabilites[2])
        else:
            break

        current = change [1]
        secuencia.append(current)

        i += 1
    return secuencia

cadena = (markov(10))
print(cadena)

screen = turtle.Screen()
screen.setup(1920,1080)
screen.bgcolor('blue')
screen.tracer(10)

pen = turtle.Turtle()
pen.color('white')
pen.speed(0)

for letter in cadena:
    if letter == 'A':
        pen.left(90)
        pen.forward(5)
    elif letter == 'B':
        pen.right(90)
        pen.forward(5)
    elif letter == 'C':
        pen.left(180)
        pen.forward(5)