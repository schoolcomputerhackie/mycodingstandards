Player = Circle(200,200,7)
Xvel=0
Yvel=0
Gravity=-0.25
Ground = Rect(0,300,400,100)

def moveup():
    Player.centerY += 1
    while Player.contains(Player.centerX,Player.centerY-3.5):
        Player.centerY += 1
    Player.centerY -= 1

#keyLabel = Label('',200,200,size=50)
def onKeyPress(key):
        global Xvel, Yvel, Gravity
        #keyLabel.value=key
        if key=='d':
            Xvel-=-1
        else:
            if key=='a':
                Xvel+=-1
            else: 
                if key == 'w' and Ground.contains(Player.centerX,Player.centerY-3.5):
                    Yvel += 5
                    
                    if Ground.contains(Player.centerX,Player.centerY-3.5):
                        Yvel=0
                    else:
                        Yvel-=Yvel-Gravity
Xvel = Xvel*0.90
Player.centerY == Yvel
Player.centerX += Xvel

    

#Player.CenterX = 20
#sleep(3)
#Player.CenterX
