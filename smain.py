import turtle

win = turtle.Screen()
pointer = turtle.Turtle()

def draw_square(t, sz):
    t.forward(sz)
    t.left(90)
    draw_square(t, sz)
    
draw_square(pointer, 100)