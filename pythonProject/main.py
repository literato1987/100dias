'''import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('images.jpeg',50)
# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.

rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append((r,g,b))'''

import turtle as t
import random



color_list=[(235, 225, 206), (216, 217, 223), (206, 157, 108), (108, 110, 128), (139, 141, 155), (236, 213, 225), (223, 212, 116), (176, 73, 36), (202, 147, 174), (219, 233, 223), (178, 157, 42), (105, 111, 170), (189, 15, 4), (17, 18, 62), (15, 35, 17), (226, 169, 195), (33, 33, 14), (213, 84, 62), (152, 166, 155), (235, 172, 159), (190, 10, 19), (43, 46, 113), (136, 81, 94), (89, 104, 91), (200, 81, 101), (181, 183, 217), (36, 17, 36), (224, 207, 14), (74, 76, 37), (51, 72, 50), (179, 200, 183), (117, 136, 120), (119, 131, 134), (249, 9, 14), (177, 200, 204)]

screen=t.Screen()
screen.colormode(255)
tim=t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

for j in range(10):
    tim.home()
    tim.setheading(90)
    tim.forward(15 * j)
    tim.right(90)

    for i in range(10):
        tim.dot(10,random.choice(color_list))
        tim.forward(15)

