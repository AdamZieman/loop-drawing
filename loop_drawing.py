# loop_drawing.py
# Make a still drawing using loop.

# Course: CSCI 130 (Introduction to Programming)
# Assignment: 6

# Author: Adam Zieman
# Date: April 1, 2021

from graphics import *
from random import randrange

def main():
    # Creates a 500 x 350 (L x H)
    win = GraphWin("Drawing With Loop",500,350)
    win.setBackground("white")

    # UPPER-RIGHT TO LOWER-LEFT DIAGNAL LINE (ANCHORS)
    # initialize variables to zero
    x1 = 0
    y1 = 0
    
    for i in range(3):
        anchorOutterArm = Oval(Point(x1+25,y1+40),Point(x1+85,y1+90))
        anchorOutterArm.setFill("midnight blue")
        anchorOutterArm.setOutline("midnight blue")
        anchorOutterArm.draw(win)

        anchorInnerArm = Oval(Point(x1+30,y1+45),Point(x1+80,y1+85))
        anchorInnerArm.setFill("white")
        anchorInnerArm.setOutline("midnight blue")
        anchorInnerArm.draw(win)

        anchorHideArm = Rectangle(Point(x1+25,y1+40),Point(x1+85,y1+75))
        anchorHideArm.setFill("white")
        anchorHideArm.setOutline("white")
        anchorHideArm.draw(win)

        anchorLeftPalm = Polygon(Point(x1+24,y1+75),Point(x1+38,y1+75),Point(x1+31,y1+70))
        anchorLeftPalm.setFill("midnight blue")
        anchorLeftPalm.setOutline("midnight blue")
        anchorLeftPalm.draw(win)
        
        anchorRightPalm = Polygon(Point(x1+71,y1+75),Point(x1+85,y1+75),Point(x1+78,y1+70))
        anchorRightPalm.setFill("midnight blue")
        anchorRightPalm.setOutline("midnight blue")
        anchorRightPalm.draw(win)

        # <anchorShankStock> comments references the left most Point
        anchorShankStock = Polygon(Point(x1+50,y1+50),Point(x1+50,y1+60),Point(x1+40,y1+60),#top-left corner
                                   Point(x1+40,y1+65),Point(x1+50,y1+65),Point(x1+50,y1+90),#outter-bottom left stock
                                   Point(x1+55,y1+95),Point(x1+60,y1+90),Point(x1+60,y1+65),#crown
                                   Point(x1+70,y1+65),Point(x1+70,y1+60),Point(x1+60,y1+60),#outter-bottom right stock
                                   Point(x1+60,y1+50))#top-right corner
        anchorShankStock.setFill("midnight blue")
        anchorShankStock.setOutline("midnight blue")
        anchorShankStock.draw(win)
        
        anchorStockEndLeft = Oval(Point(x1+32,y1+58),Point(x1+41,y1+67))
        anchorStockEndLeft.setFill("midnight blue")
        anchorStockEndLeft.setOutline("midnight blue")
        anchorStockEndLeft.draw(win)
        
        anchorStockEndRight = Oval(Point(x1+69,y1+58),Point(x1+78,y1+67))
        anchorStockEndRight.setFill("midnight blue")
        anchorStockEndRight.setOutline("midnight blue")
        anchorStockEndRight.draw(win)

        anchorOutterRing = Oval(Point(x1+46,y1+40),Point(x1+64,y1+55))
        anchorOutterRing.setFill("midnight blue")
        anchorOutterRing.setOutline("midnight blue")
        anchorOutterRing.draw(win)

        anchorInnerRing = Oval(Point(x1+50,y1+44),Point(x1+60,y1+51))
        anchorInnerRing.setFill("white")
        anchorInnerRing.setOutline("midnight blue")
        anchorInnerRing.draw(win)

        # repositions the next anchor right 190 pixels, down 110 pixels
        x1 = x1 + 190
        y1 = y1 + 110

    # HORIZONTAL LINE (AIRPLANES)
    # initialize variable to zero
    x2 = 0
    # <y2> excluded

    for k in range(3):
        airplaneCockpit = Oval(Point(x2+150,10),Point(x2+160,30))
        airplaneCockpit.setFill("green")
        airplaneCockpit.setOutline("green")
        airplaneCockpit.draw(win)
        
        # <airplaneBody> comments references the left most Point
        airplaneBody = Polygon(Point(x2+150,20),Point(x2+150,30),Point(x2+120,55),#top-left corner
                           Point(x2+120,60),Point(x2+150,50),Point(x2+150,75),#outter-bottom left wing
                           Point(x2+135,85),Point(x2+135,90),Point(x2+155,80),#top-left left stabilizer
                           Point(x2+175,90),Point(x2+175,85),Point(x2+160,75),#outter-bottom right stablizier
                           Point(x2+160,50),Point(x2+190,60),Point(x2+190,55),#inner-bottom right wing
                           Point(x2+160,30),Point(x2+160,20))#inner-top right wing
        airplaneBody.setFill("green")
        airplaneBody.setOutline("green")
        airplaneBody.draw(win)

        # repositions the next airplane right 100 pixels
        x2 = x2 + 100

    # UPPER-LEFT TO LOWER-RIGHT DIAGNAL LINE (SAILBOATS)
    # intitialize variables to zero
    x3 = 0
    y3 = 0

    for r in range(3):
        sailboatKeel = Oval(Point(x3+200,y3+330),Point(x3+250,y3+340))
        sailboatKeel.setFill("red")
        sailboatKeel.draw(win)

        sailboatHull = Polygon(Point(x3+200,y3+335),Point(x3+195,y3+330),Point(x3+255,y3+330),
                               Point(x3+250,y3+335))
        sailboatHull.setFill("red")
        sailboatHull.draw(win)

        # covers the top half of <sailboatKeel>
        sailboatKeelHide = Rectangle(Point(x3+201,y3+331),Point(x3+250,y3+335))
        sailboatKeelHide.setFill("red")
        sailboatKeelHide.setOutline("red")
        sailboatKeelHide.draw(win)
        
        sailboatMast = Rectangle(Point(x3+224,y3+300),Point(x3+226,y3+330))
        sailboatMast.setFill("slategray3")
        sailboatMast.draw(win)
        
        # random color sails and pennant
        sailboatJib = Polygon(Point(x3+224,y3+304),Point(x3+224,y3+325),Point(x3+204,y3+325))
        # jib will be a random color within the RGB scale
        for a in range(1):
            red = randrange(0,256)
            green = randrange(0,256)
            blue = randrange(0,256)
            myColor = color_rgb(red,green,blue)
            sailboatJib.setFill(myColor)
            sailboatJib.draw(win)

        sailboatMainsail = Polygon(Point(x3+226,y3+306),Point(x3+226,y3+324),Point(x3+241,y3+324))
        # mainsail will be a random color within the RGB scale
        for b in range(1):
            red = randrange(0,256)
            green = randrange(0,256)
            blue = randrange(0,256)
            myColor = color_rgb(red,green,blue)
            sailboatMainsail.setFill(myColor)
            sailboatMainsail.draw(win)

        sailboatPennant = Polygon(Point(x3+226,y3+301),Point(x3+226,y3+305),Point(x3+241,y3+303))
        # Pennant will be a random color within the RGB scale
        for c in range(1):
            red = randrange(0,256)
            green = randrange(0,256)
            blue = randrange(0,256)
            myColor = color_rgb(red,green,blue)
            sailboatPennant.setFill(myColor)
            sailboatPennant.draw(win)

        # repositions the next sailboat right 110 pixels, up 55 pixels
        x3 = x3 + 110
        y3 = y3 - 55

    # VERTICLE LINE (TRAFFIC LIGHTS)
    # utilizes if/elif statement to cycle through the different light "illumination"
    # intitialize variables to zero
    # <x4> excluded
    y4 = 0
    # bright is controlled variable for if/elif statment
    bright = 0

    for p in range(3):
        trafficFrameOutter = Rectangle(Point(90,y4+290),Point(110,y4+326))
        trafficFrameOutter.setFill("gray80")
        trafficFrameOutter.draw(win)
        
        trafficFrameInner = Rectangle(Point(95,y4+295),Point(105,y4+321))
        trafficFrameInner.setFill("gray20")
        trafficFrameInner.draw(win)

        # first run will only have green light (bright < 1, bright = 0)
        if bright < 1:
            trafficRedLight = Circle(Point(100,y4+300),3)
            trafficRedLight.setFill("white")
            trafficRedLight.draw(win)

            trafficYellowLight = Circle(Point(100,y4+308),3)
            trafficYellowLight.setFill("white")
            trafficYellowLight.draw(win)

            trafficGreenLight = Circle(Point(100,y4+316),3)
            trafficGreenLight.setFill("green")
            trafficGreenLight.draw(win)

            # increases the value of bright, making this statement false for future runs
            bright = bright + 1
        
        # second run will only have yellow light (bright == 1, bright = 1)
        elif bright == 1:
            trafficRedLight = Circle(Point(100,y4+300),3)
            trafficRedLight.setFill("white")
            trafficRedLight.draw(win)

            trafficYellowLight = Circle(Point(100,y4+308),3)
            trafficYellowLight.setFill("yellow")
            trafficYellowLight.draw(win)

            trafficGreenLight = Circle(Point(100,y4+316),3)
            trafficGreenLight.setFill("white")
            trafficGreenLight.draw(win)
            
            # increases the value of bright, making this statement false for future runs
            bright = bright + 1
        

        # third run will only have red light (bright > 1, bright = 2)
        elif bright > 1:
            trafficRedLight = Circle(Point(100,y4+300),3)
            trafficRedLight.setFill("red")
            trafficRedLight.draw(win)

            trafficYellowLight = Circle(Point(100,y4+308),3)
            trafficYellowLight.setFill("white")
            trafficYellowLight.draw(win)

            trafficGreenLight = Circle(Point(100,y4+316),3)
            trafficGreenLight.setFill("white")
            trafficGreenLight.draw(win)

        # repositions the next traffic light up 80 pixels
        y4 = y4 - 80


    # user input variable to determine amount of loop runs
    runLoop = int(input("How many circles would you like to draw?"))

    for b in range(runLoop):
        # gathers information from mouse
        click = win.getMouse()
        xClick = click.getX()
        yClick = click.getY()

        # create circle
        clickCircle = Circle(Point(xClick,yClick),30)
        clickCircle.setFill("orange")
        clickCircle.draw(win)

main()
