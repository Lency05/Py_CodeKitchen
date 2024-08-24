import turtle

# Create the turtle object
t = turtle.Turtle()

# Create the screen object
screen = turtle.Screen()

# Set the background color to black
screen.bgcolor("black")

# Set the pen color to violet
t.pencolor("violet")

# Set the turtle speed to the fastest
t.speed(0)

# Define the number of iterations
num_iterations = 150

# Main loop for drawing the spirals
for i in range(num_iterations):
  # Draw the first semi-circle
  t.circle(190 - i, 90)
  
  # Turn left by 90 degrees
  t.left(90)
  
  # Draw the second semi-circle
  t.circle(190 - i, 90)
  
  # Turn left by a smaller angle to create a spiral effect
  t.left(18)

# Keep the window open until closed manually
turtle.done()