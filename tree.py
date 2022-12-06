import turtle
# will be create object fot this turle
tu = turtle.Turtle()  # make sure that this T capial
tu.screen.bgcolor("black") #background color will be change to black
tu.pensize(2) #size of pen
tu.color("green") # initially the color of ture will be green
# now we start our turle will be in right direction
#so make it in upward direction, we will make to to turn left at 90
tu.left(90)
# now we will bring turtle down so we can se  whole tree which cover the screen
tu.backward(100)
tu.speed(200) #speed of turtle
tu.shape('turtle')#this make out arrow in the shape turtle
#we will use here recursion function to draw the tree
def tree(i):
    if i<10:
        return
    #this is base condition to top recursion bcz if we don't give the base condition turtlr will draw it
    #infinite tin\me  as this loop recursion loop is infinite untill   some base condition is not given
    else:
tu.forward(i) #we will move our tree in forward dir
tu.color("orange") #after it has draw the stright line ,we will make fruit and flower of orange color which will be circle
tu.circle(2)
#after the flower and fruits is dran we want our color back as we want to draw branch
tu.color("brown")
# till here it drawn this much
#now we want to draw it is left direction
tu.left(30)# so when it goes to left it will again draw flowe and it will go on till the value of i is
#become less then 10
tree(i/2)

 #3*100/4=75 now valie of i is 75 again 3*75/4=56.25 now value of i is 56.25 again 56.25*3/4 so like this it will go on 
tu.right(60) #once left part is done it will come back by backward() THAN IT WILL go in right dir 
tree(i/2)
tu.left(30)
tu.backward(i)
tree(100)



turtle.done()