import pygame 
import math

wScreen = 1200
hScreen = 500

win = pygame.display.set_mode((wScreen,hScreen))

class ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    
    def draw(self,win):
        pygame.draw.circle(win, (0,0,0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius-1)

    @staticmethod
    def ballPath(startx, starty, power, angle, time):
        velX = math.cos(angle) * power
        velY = math.sin(angle) * power

        distX = velX * time
        distY = (velY*time) + ((-4.9*(time)**2)/2)
        
        newX = round(distX + startx)
        newY = round(starty - distY)

        return(newX, newY)
        
        
    
def redraw_Window():
    win.fill((64,64,64))
    golf_Ball.draw(win)
    pygame.draw.line(win, (255,255,255), line[0], line[1], 1)
    pygame.display.update()

def find_angle(pos):
    sX = golf_Ball.x
    sY = golf_Ball.y
    try: 
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except: 
        angle = math.pi / 2
    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle 
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi*2) - angle

    return angle 

#Ball
golf_Ball = ball(300, 491, 8, (255,255,255))

# Position of Ball after launch
x = 0
y = 0
time = 0 
power = 0
angle = 0
shoot = False

run = True
while run: 

    if shoot: 
        if golf_Ball.y < 500 - golf_Ball.radius:
            time += 0.23
            position = ball.ballPath(x, y, power, angle, time)
            golf_Ball.x = position[0]
            golf_Ball.y = position[1]
        else: 
            shoot = False
            golf_Ball.y = 491

    pos = pygame.mouse.get_pos()
    line = [(golf_Ball.x, golf_Ball.y), pos]


    redraw_Window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shoot == False:
                shoot = True
                x = golf_Ball.x
                y = golf_Ball.y
                time = 0
                #amount of power is determined by length of line 
                power = (math.sqrt(((line[1][1]-line[0][1])**2)+(line[1][0]-line[0][0])**2)) / 10 # length of line formula
                angle = find_angle(pos)

                
                    
      


    





pygame.quit()