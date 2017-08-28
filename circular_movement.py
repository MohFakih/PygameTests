import sys, pygame, math
pygame.init()

def clearscr():
    pygame.draw.rect(screen, (0, 0, 0), [0,0,640,480])

clock = pygame.time.Clock()
res = 640, 480
screen = pygame.display.set_mode(res, 0, 32)
time = 0
mod = 400
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick()
    time += clock.get_time()/1000
    theta = ((math.floor(time*100) % 1000)/mod)*360/100
    X = 640/2 + math.cos(theta)*200
    Y = 480/2 + math.sin(theta)*200

    clearscr()
    pygame.draw.rect(screen, (255, 0, 0), [X, Y, 10, 10])
    pygame.display.flip()
    pygame.display.update()
