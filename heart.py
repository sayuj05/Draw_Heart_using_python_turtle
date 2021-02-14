# Import turtle package 
import turtle
turtle.Screen()
turtle.bgcolor("#E35D86")
sayuj = turtle.Turtle()
sayuj.pensize(8)
sayuj.pencolor("black")




# Defining a method to draw curve 
def curve(): 
	for i in range(200): 

		# Defining step by step curve motion 
        #sayuj.pensize(4)
		sayuj.right(1) 
		sayuj.forward(1) 

# Defining method to draw a full heart 
def heart(): 

	# Set the fill color to red 
	sayuj.fillcolor('red') 

	# Start filling the color 
	sayuj.begin_fill() 

	# Draw the left line 
	sayuj.left(140) 
	sayuj.forward(113) 

	# Draw the left curve 
	curve() 
	sayuj.left(120) 

	# Draw the right curve 
	curve() 

	# Draw the right line 
	sayuj.forward(112) 

	# Ending the filling of the color 
	sayuj.end_fill() 

# Defining method to write text 
def txt(): 

	# Move turtle to air 
	sayuj.up() 

	# Move turtle to a given position 
	sayuj.setpos(-68, 95) 

	# Move the turtle to the ground 
	sayuj.down() 

	# Set the text color to lightgreen 
	sayuj.color('white') 

	# Write the specified text in 
	# specified font style and size 
	sayuj.write(" Happens \u2764\ufe0f",font=( 
	"Adobe Garamond Pro", 15,)) 


# Draw a heart 
heart() 

# Write text 
txt() 

# To hide turtle 
sayuj.hideturtle() 

def main():
    print('Painting Heart For My Love... ')
    turtle.hideturtle()
    turtle.mainloop()


if __name__ == '__main__':
    main()
