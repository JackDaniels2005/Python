import sys, pygame

pygame.init()

win = pygame.display.set_mode((400,400))
x = 200
y = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.draw.circle(win,(255,255,255),(x,y),15)
    pygame.display.flip()
