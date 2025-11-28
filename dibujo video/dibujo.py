import turtle
import random
import os

os.makedirs("frames", exist_ok=True)
folder = "frames/"

width = 1920
height = 1080

colors = 'red', 'blue', 'yellow', 'white', 'orange', 'purple', 'white'

screen = turtle.Screen()
screen.setup(width, height)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

canvas = screen.getcanvas()

background = turtle.Turtle()
background.hideturtle()
background.speed(0)
background.penup()
background.goto(-width/2, -height/2)
background.pendown()
background.fillcolor('green')
background.begin_fill()

for _ in range(4):
    background.forward(width if _ % 2 == 0 else height)
    background.left(90)
background.end_fill()

for x in range(50):
    pen.pencolor(random.choice(colors))
    pen.backward(x)
    pen.left(1)
    pen.forward(x)
    pen.right(9)
   
    screen.update()
    filename = f"{folder}frame_{x:03d}.eps"
    canvas.postscript(file=filename)
   
turtle.bye()

# Convertir a imagenes
from PIL import Image

target_size = (width, height)
for filename in os.listdir(folder):
    eps_path = os.path.join(folder, filename)
    jpg_path = os.path.join(folder, filename.replace(".eps", ".jpg"))
   
    with Image.open(eps_path) as img:
        rgb_img = img.convert("RGB")
        resized_img = rgb_img.resize(target_size)
        resized_img.save(jpg_path, "JPEG", quality=95)
       
    os.remove(eps_path)

    #convertir a video

from moviepy import ImageSequenceClip

fps = 10

filelist = [os.path.join(folder, file) for file in os.listdir(folder)]

clip = ImageSequenceClip(filelist, fps=fps)
clip.write_videofile("yaaaa.mp4", fps=fps)