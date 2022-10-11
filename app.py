from tkinter import *
from wall import Wall
from mouse import Mouse

class Game():
    def __init__(self):
        self.wall_list = []
        self.root = Tk()
        self.width = 600
        self.height = 400
        self.canevas = Canvas(self.root, width = self.width, height = self.height,background='#FFF')
        self.canevas.pack()
        self.create_wall()
        self.mouse = Mouse()
        self.canevasMouse = self.mouse.draw(self.canevas)
        self.root.bind('<KeyPress>',self.__onKeyPress)
        self.root.mainloop()

    def create_wall(self):
        for i in range(0,self.width,50):
            self.wall_list.append(Wall(i,0))
            self.wall_list[-1].draw(self.canevas)
            self.wall_list.append(Wall(i,self.height-50))
            self.wall_list[-1].draw(self.canevas)
        
        for i in range(0,self.height,50):
            self.wall_list.append(Wall(0,i))
            self.wall_list[-1].draw(self.canevas)
            self.wall_list.append(Wall(self.width-50,i))
            self.wall_list[-1].draw(self.canevas)

        for i in range(100,self.width-100,50):  
            for j in range(100,self.height-100, 50):
                if i == self.width-100-50 and j == 100:
                    continue
                self.wall_list.append(Wall(i,j))
                self.wall_list[-1].draw(self.canevas)
    
    def __verify_colision(self):
        for wall in self.wall_list:
            if wall.isCollision(self.mouse.coordX,self.mouse.coordY):
                return True
        return False

    def doAction(self, numAction):
        oldCoord= (self.mouse.coordX, self.mouse.coordY)
        if  numAction==0:
            self.mouse.forward()
        elif numAction==1:
            self.mouse.turnLeft()
        elif numAction==2:
            self.mouse.turnRight()
        elif numAction==3:
            self.mouse.touchFront()
        elif numAction==4:
            self.mouse.touchLeft()
        elif numAction==5:
            self.mouse.touchRight()
        
        collision= self.__verify_colision()
        if collision or numAction>2:
            self.mouse.coordX, self.mouse.coordY = oldCoord
        self.canevas.delete(self.canevasMouse)
        self.canevasMouse = self.mouse.draw(self.canevas)
        return self.performance(numAction, collision)

    def performance(self, numAction, collision):
        return 0

    def __onKeyPress(self,e):
        if e.keycode==111 or e.char == 'z': #up
            self.doAction(0)
        if e.keycode==113 or e.char == 'q': #left
            self.doAction(1)
        if e.keycode==114 or e.char == 'd': #right
            self.doAction(2)


