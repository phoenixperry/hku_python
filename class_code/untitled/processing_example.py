xpos = 0
ypos = 0

def setup():
    background(0)
    size(1000,1000)
    xpos = 10
    ypos = 10

def draw():
    fill(xpos,ypos,0)
    xpos = xpos + 10
    global xpos
    global ypos
    xpos +=5
    ypos +=5
    ##rect(xposition, yposition, w, h)
    ellipse(xpos,ypos, random(50),random(50))


