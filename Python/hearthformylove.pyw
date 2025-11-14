import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Set up the turtle
t = turtle.Turtle()
t.speed(2)  # Slow speed for animation effect
t.hideturtle()  # Hide the turtle cursor

# Function to draw a heart
def draw_heart():
    t.pencolor("red")  # Set border color to red
    t.begin_fill()
    t.fillcolor("red")
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

# Draw the heart
draw_heart()

# Add a message
t.penup()
t.goto(0, -50)
t.pendown()
t.color("white")  # Set text color to white
t.write("I Love You!", align="center", font=("Arial", 24, "bold"))

# Keep the window open
turtle.mainloop()
