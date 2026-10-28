from turtle import *
t = Turtle()
t.shape("turtle")
t.speed(0)
t.color("forestgreen")

t.left(90)
t.penup()
t.goto(0, -150)
t.pendown()

def draw_tree(branch_length):
    if branch_length < 5:
        return
    
  
    t.forward(branch_length)
    
   
    t.left(30)
    draw_tree(branch_length - 5)
    

 
    t.forward(branch_length - 5)
    t.backward(branch_length - 5)
    t.right(60)
    draw_tree(branch_length - 2)

    t.forward(branch_length - 5)
    t.backward(branch_length - 5)
    t.left(30)
    t.backward(branch_length)
  
        
    
  
draw_tree(50)


