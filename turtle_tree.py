import turtle as t

# we will create object for this turtle
tu = t.Turtle()  # Mke Sure to keep this T capital
tu.screen.bgcolor('black')  # background color will change to Black
tu.pensize(2)  # size of pen
tu.color('green')  # initially color of turtle will be green
#  Now we start our turtle will be in right direction
# to make it will go in upward direction, we will make it to turn left at 90
tu.left(90)
# So now it will go in upward direction
# We gonna bring turtle back to start so we can see whole tree which covers the screen
tu.backward(100)
tu.speed(200)  # Speed of the turtle
tu.shape('turtle')  # this turns arrow to the shape turtle


# we will use here recursion function to draw the tree
def tree(i):
    if i < 10:
        return
        # This is base condition to stop recursion because without this condition, turtle draw infinite times
    else:
        tu.forward(i)  # move our tree in forward direction
        tu.color('orange')  # After drawing straight lines, making fruits or flowers
        tu.circle(2)
        # after drawing the fruit or flower, we want turtle back to color Brown.
        tu.color('brown')
        # till here this is drawn this much
        #  now we want to left direction
        tu.left(30)  # When it goes to the left, it will again draw flower and it will go on till the value of i
        # becomes less than 10
        # .
        tree(3*i / 4)  # 3*100/4 = 75, now value of i is 75 again; 3*75/4 = 56.25, goes on....
        tu.right(60)  # Once left part is done, it will come back by backward() then it will go in right direction.
        tree(3*i / 4)
        tu.left(30)
        tu.backward(i)


tree(100)
t.done()