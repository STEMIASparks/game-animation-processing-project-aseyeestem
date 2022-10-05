#variables
x=200
y=250
ballD=23
ogX= 200
ogY= 250
xspeed=3
yspeed=3
score1=0
score2=0
paddle2x=30


def paddle1():
    rect (mouseX, 1, 120,20)
    return paddle1

def paddle2():
    rect (paddle2x, 578, 120,20)
    return paddle2
          


def setup():
    size (500,600)
    background (0)
    
def draw ():
    global paddle1,paddle2, paddle2x, x,y,xspeed,yspeed, score1, score2
    background (0)
    frameRate (60)
    paddleMid1 = mouseX+120/2
    paddleMid2 = paddle2x+120/2
    paddle1 ()
    paddle2 ()
    circle (x, y, ballD)
    text ("Player 1: "+ str(score1), 15,20)
    textSize(15)
    text ("Player 2: " + str(score2), 380,580)
    textSize(15)
    
    # if ball passes bottom paddle, point for player 1 and reset to original point
    if y>=610:
        score1= score1+1
        x= ogX
        y= ogY
        
    # if ball passes top paddle, point for player 2 and reset to original point    
    if y<=-10:
        score2= score2+1
        x= ogX
        y= ogY
    
    if x<=205 and y>=250: # when the ball is in original point, move in certain direction
        x=x-xspeed #first time: towards bottom left corner
        y=y+yspeed
    else: # any other direction after
        x=x-xspeed
        y=y+yspeed
    
    #if the ball hits the left side of the paddle, bounce towards the left
    if x<=(paddleMid2) and x>(paddle2x) and y>= 578: #bottom paddle
        yspeed= yspeed* -1
    if x<=(paddleMid1) and x>(mouseX) and y<= 1: #top paddle
        yspeed= yspeed/ -1

    #if the ball hits the right side of the paddle, bounce towards the right
    if x>=(paddleMid2) and x<(paddle2x+120) and y>= 578: #bottom paddle
        yspeed= yspeed/ -1
    if x>=(paddleMid1) and x<(mouseX+120) and y<= 1: #top paddle
        yspeed= yspeed/ -1


    if x>=495:# if ball hits RIGHT wall:
        xspeed= xspeed /-1 #bounce back
        
    if x<= 4: # if ball hits LEFT wall:
        xspeed= xspeed * -1  #bounce back
    
def keyPressed ():
    global paddle1x, paddle2x
    if key == 'a' or key == 'A':
        paddle1x= paddle1x-20
    elif key == 'd' or key == 'D':
        paddle1x= paddle1x+20
    elif keyCode ==LEFT:
        paddle2x= paddle2x-20
    elif keyCode == RIGHT:
        paddle2x= paddle2x+20
    
        
def mouseClicked ():
    print (x)
    print (y)
    
