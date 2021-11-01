import sys, pygame, random


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 10)
size = width, height = (400,400)
win = pygame.display.set_mode(size)
clock = pygame.time.Clock()
displayName = pygame.display.set_caption("Ping Pong")
#ball variables
x = width/2
y = 50
r = 15
#player variables
playerY = height-30
playerL = 100
score = 0

speed = [random.uniform(-0.5,0.5),random.uniform(-0.5,0.5)]
Game = True


while Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                score = 0
                x, y = width/2, 50
                speed = [random.uniform(-0.5,0.5),random.uniform(-0.5,0.5)]



    dt = clock.tick()
    mousepos = mousex, mousey = pygame.mouse.get_pos()
    playerX = mousex-playerL/2
    win.fill((0,0,0))
    pygame.draw.circle(win,(255,255,255),(x,y),r)
    pygame.draw.rect(win,(255,255,255),(playerX,playerY,playerL,15))
    scr = str(score)
    textsurface = myfont.render(scr, False, (255, 255, 255))
    win.blit(textsurface,(10,10))
    pygame.display.flip()
    x += speed[0]*dt
    y += speed[1]*dt

    if(x+r+speed[0]>width or x-r+speed[0]<0):
        speed[0] = -speed[0]
    if(y-r+speed[1]<0):
        speed[1] = -speed[1]
    if(y+r+speed[1]>playerY and y+r+speed[1]<playerY+15):
        if(x+r+speed[0]>playerX and x+r+speed[0]<playerX+100):
            speed[1] = -speed[1]
            score += 1 

sys.exit()